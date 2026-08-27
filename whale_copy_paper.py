"""
whale_copy_paper.py — SIMULADOR de copy-trading (paper trading, sin dinero real)

Qué hace, en criollo:
  1. Cada cierto tiempo arma una lista de candidatos (el mismo pool que ya usa
     whale_alert_bot.py: top N por PnL en dólares, semana + mes combinados).
  2. Para cada candidato calcula su % DE RENDIMIENTO (no PnL en dólares):
         roi = pnl_del_periodo / valor_actual_de_su_portafolio
     y se queda con los 5 mejores por ese %. Estos son los "vigilados".
  3. Escucha el mismo chorro en vivo de trades de Polymarket. Cuando alguno
     de los 5 vigilados hace una apuesta, calcula qué % de SU PROPIO
     portafolio representó esa apuesta, y replica ese mismo % pero sobre
     un bankroll simulado (arranca en INITIAL_BANKROLL, ver abajo).
  4. Guarda cada apuesta simulada como "pending" y, cuando el mercado
     resuelve, calcula si esa posición de papel ganó o perdió y ACTUALIZA
     el bankroll simulado.
  5. No aplica tope por mercado ni límite de pérdida todavía —eso se define
     después de ver los datos de las primeras semanas—, pero SÍ deja
     registrado cuándo dos o más vigilados apostaron al mismo mercado el
     mismo día, para poder calibrar ese tope más adelante con datos reales.
     SÍ aplica un tope de seguridad por posición individual (ver
     MAX_SINGLE_POSITION_PCT abajo) para blindarse de datos de portafolio
     erróneos o desactualizados de la API de Polymarket.
  6. No toca ninguna wallet real, no firma nada, no gasta nada. Es 100%
     simulación — todo el "dinero" de este script es un número en un
     archivo JSON.

Variables de entorno (todas opcionales, tienen default):
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID   - si están, manda avisos "🧪 PAPER"
                                            (podés reusar las mismas que ya
                                            tenés, o poner otro chat aparte)
  INITIAL_BANKROLL           - bankroll simulado inicial en USD (default 1000)
  TOP_N_CANDIDATES           - candidatos por período antes de filtrar por
                                % de rendimiento (default 20, igual que el
                                bot de alertas)
  TOP_K_REPLICATE            - a cuántos de los mejores por % replicar
                                (default 5)
  MIN_TRADE_PCT              - ignora apuestas del vigilado que representen
                                menos de este % de SU portafolio, para no
                                replicar "ruido" de apuestas chiquitas
                                (default 0.1)
  SIZING_MODE                - FIJO (default) apuesta siempre el mismo monto
                                (FIXED_STAKE_USD) sin importar cuánto metió la
                                ballena — así todas las señales pesan igual y
                                el resultado mide la CALIDAD de la señal, no el
                                tamaño ni el orden de llegada.
                                PORCENTAJE usa el viejo modo proporcional al
                                % del portafolio de la ballena.
  FIXED_STAKE_USD            - monto fijo por apuesta en modo FIJO (default 10)
  MAX_SINGLE_POSITION_PCT    - tope de seguridad SOLO en modo PORCENTAJE:
                                ninguna posición puede superar este % del
                                bankroll (protege contra datos de portafolio
                                erróneos/desactualizados) (default 25)
  LB_CATEGORY                 - igual que el bot de alertas (default OVERALL)
  LEADERBOARD_REFRESH_SECONDS - cada cuánto se recalculan los 5 vigilados
                                 (default 900 = 15 min)
  MIN_WATCH_DAYS              - mínimo de días que se sigue vigilando a
                                 alguien aunque salga del top 5 (default 7)
  MAX_RUNTIME_SECONDS         - cuándo cortar solo (default 21000 = 5h50m)
"""

import json
import os
import socket
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import websocket
import urllib3.util.connection as urllib3_cn


def _allowed_gai_family():
    return socket.AF_INET

urllib3_cn.allowed_gai_family = _allowed_gai_family

DATA_API = "https://data-api.polymarket.com"
GAMMA_API = "https://gamma-api.polymarket.com"
RTDS_URL = "wss://ws-live-data.polymarket.com"

TRADES_FILE = Path(__file__).parent / "paper_trades.json"
STATE_FILE = Path(__file__).parent / "paper_state.json"
SUMMARY_FILE = Path(__file__).parent / "paper_summary.md"
WATCHED_FILE = Path(__file__).parent / "paper_watched.json"

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "").strip()

INITIAL_BANKROLL = float(os.environ.get("INITIAL_BANKROLL", "1000"))
TOP_N_CANDIDATES = int(os.environ.get("TOP_N_CANDIDATES", "30"))
TOP_K_REPLICATE = int(os.environ.get("TOP_K_REPLICATE", "10"))
MIN_TRADE_PCT = float(os.environ.get("MIN_TRADE_PCT", "0.1"))
# Filtro de cuota mínima: por debajo de este precio (%), no replicamos.
# Motivo: en los primeros 207 resultados de la simulación, las apuestas de cuota
# baja ("bombas") fueron las únicas claramente perdedoras (-6.6 pp en el rango
# 20-39%, -14.7 pp por debajo de 20%), mientras que de 40% para arriba el
# resultado era positivo. Tiene lógica: entrar tarde y unos centavos peor que la
# ballena duele mucho más en una apuesta a 25% que en una a 80%.
# OJO: sale de una muestra chica (día y medio). Puede ser ventaja real o
# casualidad — por eso se mide de acá en adelante antes de darlo por bueno.
MIN_ODDS_PCT = float(os.environ.get("MIN_ODDS_PCT", "40"))
# SLIPPAGE: en la vida real NUNCA conseguís el mismo precio que la ballena.
# Su propia orden mueve el mercado, y vos entrás segundos después, siempre peor.
# Sin esto, la simulación sale artificialmente optimista. Se aplica como un
# encarecimiento relativo del precio de entrada: con 2%, una cuota de 50% se
# convierte en 51% para nosotros (compramos más caro = ganamos menos si acierta).
# El 2% es una ESTIMACIÓN prudente, no un dato medido — ajustable según lo que
# veas al comparar con operaciones reales.
SLIPPAGE_PCT = float(os.environ.get("SLIPPAGE_PCT", "2"))
# COMISIÓN DE POLYMARKET (taker fee). Solo la paga quien "toma" el precio del
# mercado — que es exactamente lo que hacemos al copiar rápido a una ballena.
# Fórmula oficial: fee = coeficiente x acciones x precio x (1 - precio)
# Como acciones = stake / precio, se simplifica a: fee = coeficiente x stake x (1 - precio)
# Coeficiente por categoría (vigente desde julio 2026): deportes 0.05, cripto 0.07,
# política/finanzas/tech 0.04, economía/cultura/clima 0.05, geopolítica 0 (sin fee).
# Como este bot solo opera mercados deportivos/esports, usamos 0.05.
# OJO: Polymarket cambia estas tasas cada tanto (deportes pasó de 0.03 a 0.05 en
# julio 2026), así que conviene reverificar antes de operar con plata real.
TAKER_FEE_COEF = float(os.environ.get("TAKER_FEE_COEF", "0.05"))
# Polymarket rechaza órdenes por debajo de un mínimo de ACCIONES (no de dólares).
# El valor típico es 5, pero se define por mercado (campo minimum_order_size), así
# que si algún día operás en real conviene consultarlo por mercado en vez de asumirlo.
# Como acciones = stake / precio, con $5 se cubre todo el rango de cuotas que usamos
# (a cuota 95% hacen falta $4.75); con $1 no se llega en ninguna.
MIN_SHARES = float(os.environ.get("MIN_SHARES", "5"))
# Días que esperamos antes de dar por ANULADO un mercado cerrado cuyo precio no
# llegó a los extremos. Polymarket cierra el mercado cuando arranca el partido,
# pero la resolución la hace un oráculo DESPUÉS, y puede demorar. Un precio ~0.50
# casi siempre significa "todavía sin resolver", no "anulado" — sobre todo en
# partidos parejos, donde el último precio operado queda naturalmente en la mitad.
# Solo después de este plazo asumimos que de verdad quedó anulado y liberamos el
# capital, para no perder resoluciones legítimas por apurarnos.
VOID_AFTER_DAYS = float(os.environ.get("VOID_AFTER_DAYS", "3"))


def taker_fee(stake_usd, precio_pct):
    """Comisión que Polymarket cobra al entrar. Se paga SIEMPRE, gane o pierda."""
    p = precio_pct / 100.0
    return TAKER_FEE_COEF * stake_usd * (1 - p)
# Monto mínimo EN DÓLARES que debe tener la operación de la ballena para
# considerarla una señal. Filtra los fragmentos de ejecución (fills de
# centavos) que no representan una decisión, solo el motor casando órdenes.
MIN_WHALE_USD = float(os.environ.get("MIN_WHALE_USD", "500"))
SIZING_MODE = os.environ.get("SIZING_MODE", "FIJO").upper()   # FIJO o PORCENTAJE
FIXED_STAKE_USD = float(os.environ.get("FIXED_STAKE_USD", "10"))
MAX_SINGLE_POSITION_PCT = float(os.environ.get("MAX_SINGLE_POSITION_PCT", "25"))
MIN_WHALE_PORTFOLIO = float(os.environ.get("MIN_WHALE_PORTFOLIO", "2000"))
MAX_DAYS_TO_RESOLUTION = float(os.environ.get("MAX_DAYS_TO_RESOLUTION", "1"))  # solo mercados que resuelven el mismo día
MIN_SHORT_TERM_SHARE = float(os.environ.get("MIN_SHORT_TERM_SHARE", "0.3"))  # % mínimo de sus apuestas recientes que deben ser de corto plazo
ACTIVITY_SAMPLE_SIZE = int(os.environ.get("ACTIVITY_SAMPLE_SIZE", "10"))  # cuántas apuestas recientes de cada candidato se revisan
FILL_MERGE_WINDOW_SECONDS = float(os.environ.get("FILL_MERGE_WINDOW_SECONDS", "15"))  # fusiona fills de la misma compra dentro de esta ventana
LB_CATEGORY = os.environ.get("LB_CATEGORY", "OVERALL")
LB_PERIODS = ["WEEK", "MONTH"]

LEADERBOARD_REFRESH_SECONDS = int(os.environ.get("LEADERBOARD_REFRESH_SECONDS", "900"))
MIN_WATCH_DAYS = float(os.environ.get("MIN_WATCH_DAYS", "0"))  # 0 = solo los 5 del momento, sin colchón
MAX_RUNTIME_SECONDS = int(os.environ.get("MAX_RUNTIME_SECONDS", str(5 * 3600 + 50 * 60)))

watched = {}        # wallet (minúsculas) -> username   (los 5 vigilados actuales)
watched_meta = {}    # wallet -> {"username":..., "added_at": ts, "roi_pct": ...}
msg_count = 0
last_msg_at = time.time()
current_ws = None
seen_keys = set()
lock = threading.Lock()
run_start = time.time()
stop_flag = threading.Event()

trades = []           # cada posición simulada: {..., "status": "pending"/"won"/"lost"}
trades_dirty = False
_market_cache = {}
_portfolio_cache = {}   # wallet -> (valor, timestamp) — para no pedir de más

bankroll = INITIAL_BANKROLL
bankroll_history = []   # [{"timestamp":..., "bankroll":..., "event":...}, ...]


# ---------- utilidades básicas ----------
def load_json(path, default=None):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return default
    return default


def get_portfolio_value(wallet, max_age=60):
    """Valor total del portafolio de una wallet, con cache corto (1 min)
    para no pedirle de más a la API pero mantener el % lo más al día posible."""
    now = time.time()
    cached = _portfolio_cache.get(wallet)
    if cached and now - cached[1] < max_age:
        return cached[0]
    try:
        r = requests.get(f"{DATA_API}/value", params={"user": wallet}, timeout=8)
        data = r.json() if r.ok else None
        value = data[0].get("value") if data else None
    except Exception as e:
        print(f"Error trayendo portafolio: {e}", file=sys.stderr)
        value = None
    _portfolio_cache[wallet] = (value, now)
    return value


def get_market(slug, max_age=300):
    """Trae los datos de un mercado. Si ya está cerrado, el dato no cambia
    más y se cachea para siempre. Si todavía está abierto, se vuelve a
    consultar cada max_age segundos en vez de quedarse pegado con la
    primera respuesta."""
    if not slug:
        return None
    cached = _market_cache.get(slug)
    if cached:
        m, fetched_at = cached
        if m and m.get("closed"):
            return m
        if time.time() - fetched_at < max_age:
            return m
    try:
        r = requests.get(f"{GAMMA_API}/markets/slug/{slug}", params={"include_tag": "true"}, timeout=8)
        m = r.json() if r.ok else None
    except Exception:
        m = None
    _market_cache[slug] = (m, time.time())
    return m


def days_to_resolution(market):
    """Cuántos días faltan para que el mercado resuelva.

    OJO: en mercados deportivos, el 'endDate' de Polymarket suele tener mucho
    margen administrativo de sobra (una semana o más) aunque el partido se
    juegue hoy mismo. Por eso, si el mercado trae la hora real de inicio del
    partido (gameStartTime), usamos ESA — si no, caemos al endDate como antes.
    Sin este arreglo se descartaban partidos del día por creer que resolvían
    en 7 días.

    Si no se puede determinar, devuelve None (y en ese caso se deja pasar la
    apuesta, para no perdernos algo válido por un dato faltante)."""
    if not market:
        return None
    fecha = (market.get("gameStartTime") or market.get("game_start_time")
             or market.get("endDate") or market.get("endDateIso") or market.get("end_date"))
    if not fecha:
        return None
    try:
        dt = datetime.fromisoformat(str(fecha).replace("Z", "+00:00"))
        now_dt = datetime.now(timezone.utc)
        return (dt - now_dt).total_seconds() / 86400
    except Exception:
        return None


SPORT_KEYWORDS = [
    "soccer", "futbol", "fútbol", "football", "premier league", "champions league",
    "la liga", "serie a", "bundesliga", "mls", "libertadores", "sudamericana",
    "dota", "cs2", "csgo", "counter-strike", "counter strike",
    "league of legends", "lol:", "valorant",
    "esports", "e-sports",
    "baseball", "mlb",
    "nba", "basketball",
    "nfl",
    "nhl", "hockey",
    "tennis", "atp", "wta",
    "cricket",
]


def is_sports_market(market):
    """Detecta si un mercado es de deportes/esports. Polymarket marca
    internamente los mercados deportivos con un campo 'sports' — si está
    presente, es 100% seguro que es deporte, sin importar el idioma del
    título o de qué liga se trate. Las etiquetas y palabras clave quedan
    como respaldo por si ese campo no viene en la respuesta."""
    if not market:
        return False
    if market.get("sports"):
        return True
    tags = market.get("tags") or []
    for t in tags:
        label = (t.get("label") or t.get("slug") or "") if isinstance(t, dict) else str(t)
        label = label.lower()
        if label in ("sports", "esports", "e-sports") or any(k in label for k in SPORT_KEYWORDS):
            return True
    text = f"{market.get('title','')} {market.get('slug','')}".lower()
    return any(k in text for k in SPORT_KEYWORDS)


def market_result(market, outcome):
    if not market or not market.get("closed"):
        return "open" if market else None
    try:
        outcomes = json.loads(market["outcomes"])
        prices = json.loads(market["outcomePrices"])
        idx = next((i for i, o in enumerate(outcomes) if (o or "").lower() == (outcome or "").lower()), -1)
        if idx == -1:
            return None
        p = float(prices[idx])
        if p >= 0.99:
            return "won"
        if p <= 0.01:
            return "lost"
        # Cerrado pero SIN ganador claro. Pasa sobre todo en tenis: si un jugador
        # abandona o hay walkover, Polymarket anula y los precios quedan cerca de
        # 0.50 en vez de definirse. Antes esto devolvía None y la posición quedaba
        # colgada para siempre, con el capital trabado sin liberarse nunca.
        return ("ambiguo", p)
    except Exception:
        return None


# ---------- selección de los 5 vigilados por % de rendimiento, ----------
# ---------- pero solo entre los que de verdad operan en corto plazo -----
def get_leaderboard_period(period):
    r = requests.get(
        f"{DATA_API}/v1/leaderboard",
        params={"category": LB_CATEGORY, "timePeriod": period, "orderBy": "PNL", "limit": TOP_N_CANDIDATES},
        timeout=15,
    )
    r.raise_for_status()
    return r.json()


def get_alltime_realized_pnl(wallet, max_positions=200):
    """Trae las posiciones ya CERRADAS (resueltas) de toda la vida de esa
    wallet y suma su ganancia/pérdida realizada. La API solo deja pedir
    hasta 50 por página, así que pagino. Ordeno por fecha (no por PnL) para
    no sesgar: si alguien tiene más de max_positions posiciones cerradas en
    su vida, me quedo con las más RECIENTES, no con "las que más le
    convienen mostrar".
    Devuelve (pnl_total, ganadas, perdidas) o None si falla la consulta."""
    pnl_total = 0.0
    ganadas = perdidas = 0
    offset = 0
    pagina = 50
    try:
        while offset < max_positions:
            r = requests.get(
                f"{DATA_API}/closed-positions",
                params={"user": wallet, "limit": pagina, "offset": offset,
                        "sortBy": "TIMESTAMP", "sortDirection": "DESC"},
                timeout=15,
            )
            if not r.ok:
                return None if offset == 0 else (pnl_total, ganadas, perdidas)
            positions = r.json()
            if not isinstance(positions, list) or not positions:
                break
            for p in positions:
                pnl_pos = p.get("realizedPnl", 0) or 0
                pnl_total += pnl_pos
                if pnl_pos > 0:
                    ganadas += 1
                elif pnl_pos < 0:
                    perdidas += 1
            if len(positions) < pagina:
                break  # ya no hay más páginas
            offset += pagina
        return pnl_total, ganadas, perdidas
    except Exception as e:
        print(f"Error trayendo historial cerrado de {wallet}: {e}", file=sys.stderr)
        return None


def get_recent_trades(wallet, limit=ACTIVITY_SAMPLE_SIZE):
    try:
        r = requests.get(
            f"{DATA_API}/activity",
            params={"user": wallet, "limit": limit, "type": "TRADE"},
            timeout=10,
        )
        return r.json() if r.ok else []
    except Exception:
        return []


def short_term_trade_ratio(wallet):
    """Mira las últimas apuestas reales de la wallet y calcula qué % de
    ellas fueron en deportes/esports Y en mercados que resolvían en
    MAX_DAYS_TO_RESOLUTION días o menos desde el momento en que apostó.
    Devuelve None si no hay datos suficientes para opinar."""
    acts = get_recent_trades(wallet)
    if not acts:
        return None
    short, counted = 0, 0
    for a in acts:
        slug = a.get("slug")
        ts = a.get("timestamp")
        if not slug or not ts:
            continue
        market = get_market(slug)
        if not market:
            continue
        end = (market.get("gameStartTime") or market.get("game_start_time")
               or market.get("endDate") or market.get("endDateIso") or market.get("end_date"))
        if not end:
            continue
        try:
            end_dt = datetime.fromisoformat(str(end).replace("Z", "+00:00"))
            trade_dt = datetime.fromtimestamp(ts, tz=timezone.utc)
            days = (end_dt - trade_dt).total_seconds() / 86400
        except Exception:
            continue
        counted += 1
        if days <= MAX_DAYS_TO_RESOLUTION and is_sports_market(market):
            short += 1
    if counted == 0:
        return None
    return short / counted


def compute_top5_by_roi():
    """Junta candidatos de semana+mes (por PnL en $, igual que el bot de
    alertas), descarta a los de portafolio muy chico (artefacto de %), a
    los que no operan mayormente en corto plazo, y a los que no tienen un
    historial ganador sostenido a largo plazo. De los que quedan, se queda
    con los 5 mejores por % de rendimiento reciente."""
    candidates = {}
    for period in LB_PERIODS:
        try:
            for t in get_leaderboard_period(period):
                w = (t.get("proxyWallet") or "").lower()
                if not w:
                    continue
                candidates.setdefault(w, t)
        except Exception as e:
            print(f"Error trayendo ranking de {period}: {e}", file=sys.stderr)

    total_candidatos = len(candidates)
    descartados_portafolio = 0
    descartados_historico = 0
    descartados_cortoplazo = 0

    scored = []
    for w, t in candidates.items():
        pnl = t.get("pnl")
        value = get_portfolio_value(w)
        if pnl is None or not value or value < MIN_WHALE_PORTFOLIO:
            descartados_portafolio += 1
            continue

        historico = get_alltime_realized_pnl(w)
        if historico is not None and historico[0] <= 0:
            descartados_historico += 1
            continue

        ratio = short_term_trade_ratio(w)
        if ratio is None or ratio < MIN_SHORT_TERM_SHARE:
            descartados_cortoplazo += 1
            continue

        roi_pct = pnl / value * 100
        scored.append((w, t.get("userName", "anon"), roi_pct, ratio))

    print(f"[ranking][diagnóstico] candidatos totales: {total_candidatos} | "
          f"descartados por portafolio chico (<${MIN_WHALE_PORTFOLIO:.0f}): {descartados_portafolio} | "
          f"descartados por historial completo negativo: {descartados_historico} | "
          f"descartados por no ser mayormente corto plazo/deportes (<{MIN_SHORT_TERM_SHARE*100:.0f}%): {descartados_cortoplazo} | "
          f"sobrevivientes finales: {len(scored)}")

    scored.sort(key=lambda x: x[2], reverse=True)
    return scored[:TOP_K_REPLICATE]


# ---------- reporte ----------
def max_drawdown_pct():
    peak = INITIAL_BANKROLL
    worst = 0.0
    for h in bankroll_history:
        peak = max(peak, h["bankroll"])
        dd = (peak - h["bankroll"]) / peak * 100 if peak > 0 else 0
        worst = max(worst, dd)
    return worst


def build_summary_md():
    per_wallet = {}
    for tr in trades:
        w = tr["wallet"]
        per_wallet.setdefault(w, {"username": tr["username"], "won": 0, "lost": 0, "pending": 0, "pnl_usd": 0.0})
        if tr["status"] == "won" or (tr["status"] in ("cerrada_venta", "anulado") and tr.get("profit_usd", 0.0) >= 0):
            per_wallet[w]["won"] += 1
            per_wallet[w]["pnl_usd"] += tr.get("profit_usd", 0.0)
        elif tr["status"] == "lost" or (tr["status"] in ("cerrada_venta", "anulado") and tr.get("profit_usd", 0.0) < 0):
            per_wallet[w]["lost"] += 1
            per_wallet[w]["pnl_usd"] += tr.get("profit_usd", 0.0)
        else:
            per_wallet[w]["pending"] += 1

    total_return_pct = (bankroll - INITIAL_BANKROLL) / INITIAL_BANKROLL * 100

    overlaps = {}
    for tr in trades:
        key = tr["slug"]
        overlaps.setdefault(key, set()).add(tr["username"])
    overlap_markets = {k: v for k, v in overlaps.items() if len(v) > 1}

    recortados_tope = sum(1 for tr in trades if tr.get("recortado_por_tope"))

    hora_peru = time.gmtime(time.time() - 5 * 3600)
    lines = [
        "# Paper trading — resultado de la simulación",
        "",
        f"Actualizado: {time.strftime('%Y-%m-%d %H:%M:%S', hora_peru)} (hora de Perú)",
        "",
        f"**Bankroll inicial:** ${INITIAL_BANKROLL:,.2f}",
        f"**Bankroll actual:** ${bankroll:,.2f}",
        f"**Retorno acumulado:** {total_return_pct:+.2f}%",
        f"**Peor caída desde un máximo (drawdown):** {max_drawdown_pct():.2f}%",
        f"**Posiciones recortadas por el tope de seguridad ({MAX_SINGLE_POSITION_PCT:.0f}% máx. por posición):** {recortados_tope}",
        "",
        f"**Modo de apuesta:** " + ("monto fijo de ${:,.2f} por apuesta".format(FIXED_STAKE_USD)
          if SIZING_MODE == "FIJO" else f"proporcional al % de la ballena (tope {MAX_SINGLE_POSITION_PCT:.0f}%)"),
        "",
        f"**Filtro de cuota mínima:** solo se replican apuestas de {MIN_ODDS_PCT:.0f}% o más",
        f"**Comisión de Polymarket:** taker fee con coeficiente {TAKER_FEE_COEF} (deportes) — "
        f"se paga al entrar gane o pierda, y otra vez al vender anticipadamente. "
        f"Mínimo de orden: {MIN_SHARES:.0f} acciones.",
        f"**Slippage aplicado:** {SLIPPAGE_PCT:.1f}% — entramos siempre a peor precio que la ballena "
        f"(su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.",
        f"**Capital comprometido ahora mismo:** ${sum(t.get('paper_stake_usd',0) for t in trades if t['status']=='pending'):,.2f} "
        f"en {sum(1 for t in trades if t['status']=='pending')} posiciones abiertas "
        f"(disponible para nuevas apuestas: ${max(0.0, bankroll - sum(t.get('paper_stake_usd',0) for t in trades if t['status']=='pending')):,.2f})",
        "",
        "_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._",
        "",
        "## Por vigilado",
        "",
        "| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |",
        "|---|---|---|---|---|",
    ]
    for w, d in sorted(per_wallet.items(), key=lambda kv: -kv[1]["pnl_usd"]):
        lines.append(f"| {d['username']} | {d['won']} | {d['lost']} | {d['pending']} | {d['pnl_usd']:+,.2f} USD |")

    # --- Métricas de calibración: ¿acierta más o menos de lo que dice la cuota? ---
    resueltas = [t for t in trades if t["status"] in ("won", "lost")]
    if resueltas:
        def rango(o):
            if o < 20: return "1-19% (bomba)"
            if o < 40: return "20-39%"
            if o < 60: return "40-59%"
            if o < 80: return "60-79%"
            if o < 95: return "80-94%"
            return "95-99% (casi seguro)"

        cubos = {}
        for t in resueltas:
            o = t.get("odds_at_bet", 0)
            c = cubos.setdefault(rango(o), {"won": 0, "lost": 0, "odds_sum": 0.0})
            c["won" if t["status"] == "won" else "lost"] += 1
            c["odds_sum"] += o

        stakes = [t.get("paper_stake_usd", 0) for t in resueltas]
        stake_prom = sum(stakes) / len(stakes)
        total_apostado = sum(stakes)
        pnl_resueltas = sum(t.get("profit_usd", 0) for t in resueltas)
        roi = pnl_resueltas / total_apostado * 100 if total_apostado else 0
        cuota_prom = sum(t.get("odds_at_bet", 0) for t in resueltas) / len(resueltas)
        ganadas_tot = sum(1 for t in resueltas if t["status"] == "won")

        lines += [
            "", "## Análisis general", "",
            f"- **Apuestas resueltas:** {len(resueltas)}",
            f"- **Aciertos:** {ganadas_tot} ({ganadas_tot/len(resueltas)*100:.1f}%)",
            f"- **Cuota promedio de entrada:** {cuota_prom:.1f}%",
            f"- **Stake promedio:** ${stake_prom:,.2f}",
            f"- **Total apostado (suma de stakes):** ${total_apostado:,.2f}",
            f"- **ROI sobre lo apostado:** {roi:+.2f}%",
            f"- **Comisiones pagadas (taker fee):** ${sum(t.get('fee_usd',0) for t in resueltas):,.2f} "
            f"({sum(t.get('fee_usd',0) for t in resueltas)/total_apostado*100:.2f}% del capital apostado)",
            f"- **ROI que habría dado SIN comisiones:** "
            f"{(pnl_resueltas + sum(t.get('fee_usd',0) for t in resueltas))/total_apostado*100:+.2f}% "
            f"_(referencia: cuánto pesan las comisiones)_",
            "",
            "### ¿Aciertan más o menos de lo que promete la cuota?",
            "",
            "_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. "
            "Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._",
            "",
            "| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |",
            "|---|---|---|---|---|",
        ]
        for r in ["1-19% (bomba)", "20-39%", "40-59%", "60-79%", "80-94%", "95-99% (casi seguro)"]:
            if r not in cubos:
                continue
            c = cubos[r]
            n = c["won"] + c["lost"]
            real = c["won"] / n * 100
            esperado = c["odds_sum"] / n
            lines.append(f"| {r} | {n} | {real:.1f}% | {esperado:.1f}% | {real-esperado:+.1f} pp |")

    lines += ["", "## Mercados donde coincidieron 2+ vigilados (para calibrar el tope futuro)", ""]
    if overlap_markets:
        lines.append("| Mercado | Vigilados que coincidieron |")
        lines.append("|---|---|")
        for slug, names in overlap_markets.items():
            lines.append(f"| {slug} | {', '.join(sorted(names))} |")
    else:
        lines.append("_Todavía no hubo coincidencias._")

    lines += ["", "## Últimas 30 apuestas de papel (detalle)", "",
               "| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |",
               "|---|---|---|---|---|---|---|---|"]
    for tr in sorted(trades, key=lambda t: t["timestamp_added"], reverse=True)[:30]:
        estado = {"pending": "⏳ pendiente", "won": "✅ ganada", "lost": "❌ perdida",
                  "cerrada_venta": "💰 vendida anticipada", "anulado": "⚖️ anulada/devuelta"}.get(tr["status"], tr["status"])
        resultado = f"{tr['profit_usd']:+,.2f}" if tr["status"] != "pending" else "—"
        titulo = (tr.get("title") or "(sin título)")[:40]
        marca_tope = " ⚠️" if tr.get("recortado_por_tope") else ""
        lines.append(
            f"| {tr.get('username','')} | {titulo} | {tr.get('outcome','')} ({tr.get('side','')}) | "
            f"{tr.get('odds_at_bet',0)}% | {tr.get('paper_stake_usd',0):,.2f}{marca_tope} | "
            f"{tr.get('whale_pct',0):.1f}% | {estado} | {resultado} |"
        )

    SUMMARY_FILE.write_text("\n".join(lines) + "\n")


def send_telegram(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": text, "disable_web_page_preview": True},
            timeout=10,
        )
    except Exception as e:
        print(f"Error mandando a Telegram: {e}", file=sys.stderr)


# ---------- registrar y resolver posiciones de papel ----------
def log_paper_trade(username, wallet, trade, whale_usd, whale_pct, paper_stake, odds, odds_ballena=None,
                     recortado_bankroll=False, recortado_tope=False, whale_value_at_open=None):
    global trades_dirty
    slug = trade.get("slug")
    same_day_others = sorted({
        tr["username"] for tr in trades
        if tr["slug"] == slug and tr["username"] != username
        and time.time() - tr["timestamp_added"] < 86400
    })
    with lock:
        trades.append({
            "timestamp": trade.get("timestamp"),
            "timestamp_added": time.time(),
            "username": username,
            "wallet": wallet,
            "slug": slug or "",
            "title": trade.get("title") or "(sin título)",
            "outcome": trade.get("outcome") or "",
            "side": trade.get("side") or "",
            "whale_usd": whale_usd,
            "whale_pct": round(whale_pct, 3),
            "whale_value_at_open": whale_value_at_open,
            "paper_stake_usd": round(paper_stake, 2),
            "odds_at_bet": odds,
            "fee_usd": round(taker_fee(paper_stake, odds), 3),
            "odds_ballena": odds_ballena if odds_ballena is not None else odds,
            "status": "pending",
            "profit_usd": 0.0,
            "overlaps_with": same_day_others,
            "recortado_por_bankroll": recortado_bankroll,
            "recortado_por_tope": recortado_tope,
            "last_fill_at": time.time(),
            "fills": 1,
        })
        trades_dirty = True

    aviso = f"🧪 PAPER — {username} apostó {whale_pct:.2f}% de su portafolio\n"
    aviso += f"Réplica simulada: ${paper_stake:,.2f} (comisión: ${taker_fee(paper_stake, odds):.3f})\n"
    aviso += f"Mercado: {trade.get('title','')}\n"
    aviso += f"Apuesta a: {trade.get('outcome','')} ({trade.get('side','')})\n"
    if odds_ballena is not None and odds_ballena != odds:
        aviso += f"Precio de la ballena: {odds_ballena}% -> nuestro precio real: {odds}% (slippage)\n"
    else:
        aviso += f"Precio al momento de apostar: {odds}%\n"
    if recortado_tope:
        aviso += f"⚠️ Recortado por tope de seguridad ({MAX_SINGLE_POSITION_PCT:.0f}% máx. por posición)\n"
    if recortado_bankroll:
        aviso += "⚠️ Recortado: no había suficiente bankroll disponible para replicar el % completo\n"
    if same_day_others:
        aviso += f"⚠️ Coincide hoy con: {', '.join(same_day_others)}\n"
    send_telegram(aviso)


def resolve_pending_trades():
    global trades_dirty, bankroll
    with lock:
        pending = [tr for tr in trades if tr["status"] == "pending"]
    if pending:
        print(f"[resolver] revisando {len(pending)} posiciones pendientes...")
    for tr in pending:
        market = get_market(tr["slug"])
        result = market_result(market, tr["outcome"])

        # Mercado cerrado con precio ambiguo -> lo liquidamos al precio final,
        # igual que haría Polymarket al anular/devolver, para liberar el capital.
        if isinstance(result, tuple) and result[0] == "ambiguo":
            precio_final = result[1]
            dias_abierta = (time.time() - tr["timestamp_added"]) / 86400
            if dias_abierta < VOID_AFTER_DAYS:
                print(f"  … {tr['slug']}: cerrado pero el oráculo todavía no resolvió "
                      f"(precio {precio_final:.2f}, lleva {dias_abierta:.1f} días) — "
                      f"seguimos esperando hasta {VOID_AFTER_DAYS:.0f} días")
                time.sleep(0.1)
                continue
            stake = tr["paper_stake_usd"]
            entry = tr["odds_at_bet"] / 100.0
            valor = stake * (precio_final / entry) if entry > 0 else 0
            fee = tr.get("fee_usd") or taker_fee(stake, tr["odds_at_bet"])
            profit = valor - stake - fee
            with lock:
                tr["status"] = "anulado"
                tr["profit_usd"] = round(profit, 2)
                tr["closed_price"] = round(precio_final * 100)
                bankroll += profit
                bankroll_history.append({
                    "timestamp": time.time(),
                    "bankroll": round(bankroll, 2),
                    "event": f"anulado tras {VOID_AFTER_DAYS:.0f}+ días sin resolver (precio {precio_final:.2f}): {tr['username']} — {tr['title']}",
                })
            trades_dirty = True
            print(f"  ⚖ {tr['slug']}: lleva {dias_abierta:.1f} días cerrado sin resolver "
                  f"(precio {precio_final:.2f}) -> se da por anulado, liquidado a {profit:+.2f} USD, capital liberado")
            time.sleep(0.1)
            continue

        if result not in ("won", "lost"):
            if market is None:
                print(f"  ⚠ {tr['slug']}: no se pudo consultar el mercado (posible error de red o slug incorrecto)")
            elif not market.get("closed"):
                print(f"  … {tr['slug']}: todavía abierto/sin resolver en Polymarket")
            else:
                print(f"  ⚠ {tr['slug']}: cerrado pero no pude determinar won/lost para el outcome '{tr['outcome']}' — revisar formato de outcomes/outcomePrices")
            time.sleep(0.1)
            continue
        stake = tr["paper_stake_usd"]
        odds = tr["odds_at_bet"] / 100.0
        if result == "won" and odds > 0:
            profit = stake * (1 - odds) / odds
        else:
            profit = -stake
        # La comisión de entrada se paga SIEMPRE, gane o pierda la apuesta.
        fee = tr.get("fee_usd") or taker_fee(stake, tr["odds_at_bet"])
        profit -= fee
        with lock:
            tr["status"] = result
            tr["profit_usd"] = round(profit, 2)
            bankroll += profit
            bankroll_history.append({
                "timestamp": time.time(),
                "bankroll": round(bankroll, 2),
                "event": f"{result}: {tr['username']} — {tr['title']}",
            })
        trades_dirty = True
        time.sleep(0.1)


# ---------- websocket en vivo (idéntico patrón al bot de alertas) ----------
def on_ws_open(ws):
    global last_msg_at
    last_msg_at = time.time()
    print("[paper] conectado — escuchando trades de los 5 vigilados por % de rendimiento")
    ws.send(json.dumps({"action": "subscribe", "subscriptions": [{"topic": "activity", "type": "trades"}]}))


def close_position_early(username, wallet, trade, sell_price_pct):
    """Cuando la ballena vende (SELL), busca las posiciones de papel
    pendientes que tengamos abiertas para esa misma wallet+mercado+resultado
    y las cierra YA, al precio actual."""
    global bankroll, trades_dirty
    slug = trade.get("slug")
    outcome = trade.get("outcome")
    with lock:
        abiertas = [tr for tr in trades if tr["status"] == "pending" and tr["wallet"] == wallet
                    and tr["slug"] == slug and tr["outcome"] == outcome]
        if not abiertas:
            return False
        total_profit = 0.0
        for tr in abiertas:
            entry = tr["odds_at_bet"] / 100.0
            stake = tr["paper_stake_usd"]
            profit = stake * (sell_price_pct / 100.0 / entry - 1) if entry > 0 else -stake
            # Dos comisiones: la de entrada + la de salida (vender también es tomar precio)
            valor_salida = stake * (sell_price_pct / 100.0 / entry) if entry > 0 else 0
            fee_total = (tr.get("fee_usd") or taker_fee(stake, tr["odds_at_bet"])) + taker_fee(valor_salida, sell_price_pct)
            profit -= fee_total
            tr["fee_total_usd"] = round(fee_total, 3)
            tr["status"] = "cerrada_venta"
            tr["profit_usd"] = round(profit, 2)
            tr["closed_price"] = sell_price_pct
            total_profit += profit
        bankroll += total_profit
        bankroll_history.append({
            "timestamp": time.time(),
            "bankroll": round(bankroll, 2),
            "event": f"venta anticipada: {username} — {trade.get('title')} ({total_profit:+.2f} USD)",
        })
        trades_dirty = True
    print(f"🧪 PAPER — {username}: VENDE y cierra {len(abiertas)} posición(es) de papel en "
          f"{trade.get('title')} al {sell_price_pct}% -> {total_profit:+,.2f} USD")
    send_telegram(f"🧪 PAPER — {username} vendió (toma ganancia/corta pérdida)\n"
                   f"Cerramos la réplica en {trade.get('title')} — {trade.get('outcome')}\n"
                   f"Resultado: {total_profit:+,.2f} USD")
    return True


def on_ws_message(ws, message):
    global last_msg_at, msg_count
    last_msg_at = time.time()
    if message == "PONG":
        return
    try:
        msg = json.loads(message)
    except Exception:
        return
    is_trade = (msg.get("topic") == "activity" and msg.get("type") == "trades") or msg.get("type") == "trades"
    if not is_trade:
        return
    trade = msg.get("payload") or msg.get("data") or msg
    wallet_raw = trade.get("proxyWallet")
    wallet = wallet_raw.lower() if wallet_raw else None

    msg_count += 1
    if not wallet or wallet not in watched:
        return

    key = f"{trade.get('transactionHash','')}_{trade.get('timestamp')}_{trade.get('asset')}_{trade.get('size')}"
    if key in seen_keys:
        return
    seen_keys.add(key)
    if len(seen_keys) > 5000:
        seen_keys.clear()

    username = watched.get(wallet, "anon")
    odds = round((trade.get("price") or 0) * 100)
    side = (trade.get("side") or "").upper()

    if side == "SELL":
        cerro_algo = close_position_early(username, wallet, trade, odds)
        if not cerro_algo:
            print(f"🧪 PAPER — {username}: vendió en {trade.get('title')} pero no teníamos "
                  f"posición de papel abierta ahí — se ignora")
        return

    whale_usd = (trade.get("size") or 0) * (trade.get("price") or 0)
    whale_value = get_portfolio_value(wallet)
    if not whale_value or whale_value <= 0:
        return
    # Piso ABSOLUTO en dólares: una orden grande se ejecuta contra el libro y
    # genera fragmentos minúsculos ($0,69, $3,31...). Sin este piso, el primer
    # fragmento que llegue dispara una posición de papel completa — o sea,
    # apostaríamos $10 copiando una migaja de $0,69.
    if whale_usd < MIN_WHALE_USD:
        return

    whale_pct = whale_usd / whale_value * 100
    if whale_pct < MIN_TRADE_PCT:
        return

    if odds < MIN_ODDS_PCT:
        print(f"🧪 PAPER — {username}: se ignora, cuota de {odds}% por debajo del mínimo "
              f"de {MIN_ODDS_PCT:.0f}% — {trade.get('title')}")
        return

    # Precio realista de ENTRADA nuestro: peor que el de la ballena por el slippage.
    odds_ballena = odds
    odds = min(99, round(odds * (1 + SLIPPAGE_PCT / 100)))

    market = get_market(trade.get("slug"))
    days_left = days_to_resolution(market)
    if days_left is not None and days_left > MAX_DAYS_TO_RESOLUTION:
        print(f"🧪 PAPER — {username}: se ignora, el mercado resuelve en ~{days_left:.0f} días "
              f"(más del límite de {MAX_DAYS_TO_RESOLUTION:.0f}) — {trade.get('title')}")
        return
    if not is_sports_market(market):
        print(f"🧪 PAPER — {username}: se ignora, no es un mercado de deportes/esports — {trade.get('title')}")
        return

    merge_or_open_position(username, wallet, trade, whale_usd, whale_pct, odds, whale_value, odds_ballena)


def merge_or_open_position(username, wallet, trade, whale_usd, whale_pct, odds, whale_value_now, odds_ballena=None):
    """Si la misma ballena ya tiene una compra reciente (dentro de
    FILL_MERGE_WINDOW_SECONDS) en el mismo mercado+resultado, la suma a esa
    posición en vez de abrir una nueva.

    IMPORTANTE (acá estaba el bug que inflaba el % por encima de 100%):
    para el % combinado de varios fills SIEMPRE se usa el valor del
    portafolio de la ballena tomado en el momento en que se abrió la
    posición (whale_value_at_open) — nunca uno más nuevo. Si en vez de eso
    se vuelve a consultar /value en cada fill, ese valor ya refleja la
    plata que la ballena gastó en los fills anteriores (más baja), y dividir
    el monto TOTAL acumulado entre un número cada vez más chico produce
    porcentajes sin sentido (se vieron casos de más de 100%, imposibles en
    la realidad).

    Además, sin importar cómo dé el cálculo, se aplica un tope de seguridad
    (MAX_SINGLE_POSITION_PCT) para que ninguna posición individual pueda
    comerse una porción irracional del bankroll simulado."""
    global trades_dirty
    slug = trade.get("slug")
    outcome = trade.get("outcome")
    now = time.time()

    with lock:
        # UNA POSICIÓN POR APOSTADOR + MERCADO + RESULTADO, sin ventana de tiempo.
        # Polymarket ejecuta una orden grande contra el libro y eso genera
        # decenas de operaciones sueltas (vimos fills de $0,69 y $8.200 de la
        # misma orden, repartidos en más de una hora). Cualquier ventana de
        # tiempo deja fragmentos afuera; mientras la posición siga abierta,
        # todo lo que la ballena ponga ahí es la MISMA señal.
        existente = next((tr for tr in trades if tr["status"] == "pending" and tr["wallet"] == wallet
                           and tr["slug"] == slug and tr["outcome"] == outcome
                           and tr.get("side") == "BUY"), None)
        allocated = sum(tr["paper_stake_usd"] for tr in trades if tr["status"] == "pending")

    if existente:
        combined_whale_usd = existente["whale_usd"] + whale_usd
        # Usamos el valor de portafolio congelado en el fill 1, NO uno nuevo.
        whale_value_base = existente.get("whale_value_at_open") or whale_value_now
        combined_pct = combined_whale_usd / whale_value_base * 100 if whale_value_base else whale_pct

        if SIZING_MODE == "FIJO":
            # En modo fijo, los fills extra NO agrandan la posición: ya
            # apostamos nuestro monto fijo en el primer fill. Solo actualizamos
            # el dato de cuánto metió la ballena en total (informativo).
            with lock:
                existente["whale_usd"] = combined_whale_usd
                existente["whale_pct"] = round(combined_pct, 3)
                existente["last_fill_at"] = now
                existente["fills"] = existente.get("fills", 1) + 1
                trades_dirty = True
            print(f"🧪 PAPER — {username}: fill adicional en {trade.get('title')} "
                  f"(la ballena lleva ${combined_whale_usd:,.0f} = {combined_pct:.1f}% suyo; "
                  f"nuestra réplica sigue fija en ${existente['paper_stake_usd']:,.2f})")
            return

        capped_pct = min(combined_pct, MAX_SINGLE_POSITION_PCT)
        recortado_tope = capped_pct < combined_pct

        desired_total = capped_pct / 100 * bankroll
        available = max(0.0, bankroll - allocated)
        faltante = max(0.0, desired_total - existente["paper_stake_usd"])
        adicional = min(faltante, available)
        nuevo_stake_total = existente["paper_stake_usd"] + adicional
        recortado_bankroll = adicional < faltante
        nuevo_odds = odds
        if nuevo_stake_total > 0:
            nuevo_odds = round((existente["paper_stake_usd"] * existente["odds_at_bet"] + adicional * odds) / nuevo_stake_total)
        with lock:
            existente["paper_stake_usd"] = round(nuevo_stake_total, 2)
            existente["whale_usd"] = combined_whale_usd
            existente["whale_pct"] = round(combined_pct, 3)  # se guarda el % real (sin recortar), para que quede a la vista
            existente["odds_at_bet"] = nuevo_odds
            existente["last_fill_at"] = now
            existente["fills"] = existente.get("fills", 1) + 1
            if recortado_bankroll:
                existente["recortado_por_bankroll"] = True
            if recortado_tope:
                existente["recortado_por_tope"] = True
            trades_dirty = True
        nota = ""
        if recortado_tope:
            nota += f" [% real {combined_pct:.1f}%, recortado a {MAX_SINGLE_POSITION_PCT:.0f}% por tope de seguridad]"
        print(f"🧪 PAPER — {username}: fill adicional fusionado en {trade.get('title')} "
              f"(+${adicional:,.2f}, total ${nuevo_stake_total:,.2f}, {existente['fills']} fills){nota}")
        return

    with lock:
        available = max(0.0, bankroll - allocated)

    if SIZING_MODE == "FIJO":
        # Monto fijo: todas las señales pesan igual. No depende del dato de
        # portafolio de la ballena (que ya demostró ser poco confiable) ni del
        # orden de llegada. El % de la ballena se sigue guardando como dato,
        # pero no influye en cuánto arriesgamos.
        desired_stake = FIXED_STAKE_USD
        recortado_tope = False
    else:
        capped_pct = min(whale_pct, MAX_SINGLE_POSITION_PCT)
        recortado_tope = capped_pct < whale_pct
        desired_stake = capped_pct / 100 * bankroll

    recortado_bankroll = desired_stake > available
    paper_stake = min(desired_stake, available)

    acciones = paper_stake / (odds / 100.0) if odds > 0 else 0
    if 0 < paper_stake and acciones < MIN_SHARES:
        print(f"🧪 PAPER — {username}: se ignora, ${paper_stake:,.2f} a cuota {odds}% son solo "
              f"{acciones:.1f} acciones y Polymarket exige un mínimo de {MIN_SHARES:.0f} "
              f"(harían falta ${MIN_SHARES*odds/100:,.2f}) — {trade.get('title')}")
        return

    if paper_stake <= 0:
        print(f"🧪 PAPER — {username}: se ignora, no queda bankroll disponible "
              f"(${allocated:,.2f} ya comprometidos en posiciones pendientes)")
        return

    nota = ""
    if recortado_tope:
        nota += f" [% real {whale_pct:.1f}%, recortado a {MAX_SINGLE_POSITION_PCT:.0f}% por tope de seguridad]"
    if recortado_bankroll:
        nota += " [recortado por falta de bankroll disponible]"
    print(f"🧪 PAPER — {username}: {whale_pct:.2f}% -> ${paper_stake:,.2f} en {trade.get('title')}{nota}")
    log_paper_trade(username, wallet, trade, whale_usd, whale_pct, paper_stake, odds, odds_ballena,
                     recortado_bankroll=recortado_bankroll, recortado_tope=recortado_tope,
                     whale_value_at_open=whale_value_now)


def on_ws_error(ws, error):
    print(f"[paper] error de conexión: {error}", file=sys.stderr)


def on_ws_close(ws, code, msg):
    print("[paper] conexión cerrada, reconectando...")


# ---------- hilo de fondo ----------
def save_and_commit():
    global trades_dirty
    try:
        with lock:
            TRADES_FILE.write_text(json.dumps(trades, indent=2))
            STATE_FILE.write_text(json.dumps({"bankroll": bankroll, "history": bankroll_history}, indent=2))
            build_summary_md()
            WATCHED_FILE.write_text(json.dumps(watched_meta, indent=2))
        os.system('git config user.name "whale-copy-paper-bot"')
        os.system('git config user.email "actions@github.com"')
        os.system("git add paper_trades.json paper_state.json paper_summary.md paper_watched.json")
        os.system('git diff --staged --quiet || git commit -m "actualizar simulación de paper trading"')

        # OJO: el bot de alertas (whale_alert_bot.py) escribe en ESTE MISMO repo
        # al mismo tiempo (results.json / results.md). Cuando los dos hacen push
        # a la vez, uno de los dos se lleva un "rejected (fetch first)". Por eso
        # acá reintentamos con espera creciente y trayendo primero lo del otro
        # bot, quedándonos siempre con NUESTRA versión de los paper_* si hay
        # choque (se regeneran enteros en cada ciclo, no hay nada que perder).
        for intento in range(5):
            if os.system("git push") == 0:
                if intento:
                    print(f"[save_and_commit] push OK en el intento {intento+1}")
                break
            espera = 2 ** intento  # 1s, 2s, 4s, 8s, 16s
            print(f"[save_and_commit] push rechazado (intento {intento+1}/5) — probablemente el bot de "
                  f"alertas escribió al mismo tiempo. Trayendo sus cambios y reintentando en {espera}s...",
                  file=sys.stderr)
            time.sleep(espera)
            if os.system("git fetch origin main") != 0:
                continue
            if os.system('git merge --no-edit -X ours origin/main') != 0:
                os.system("git merge --abort")
                print("[save_and_commit] no se pudo fusionar automáticamente, se reintenta en el próximo ciclo",
                      file=sys.stderr)
                break
        else:
            print("[save_and_commit] no se logró hacer push tras 5 intentos — los datos quedan guardados "
                  "en disco y se vuelven a intentar en el próximo ciclo (no se pierde nada)", file=sys.stderr)
        trades_dirty = False
    except Exception as e:
        import traceback
        print(f"[save_and_commit] error al guardar, se reintenta en el próximo ciclo: {e}", file=sys.stderr)
        traceback.print_exc()


def ranking_worker():
    """Hilo aparte para el análisis pesado (revisar el historial de cada
    candidato). Corre en su propio ciclo y JAMÁS bloquea el guardado de
    archivos, aunque tarde varios minutos en completar una vuelta."""
    last_lb_refresh = 0
    while not stop_flag.is_set():
        try:
            now = time.time()
            if now - last_lb_refresh > LEADERBOARD_REFRESH_SECONDS or not watched:
                print("[ranking] arrancando análisis de candidatos (puede tardar varios minutos)...")
                top5 = compute_top5_by_roi()
                cutoff = time.time() - MIN_WATCH_DAYS * 86400
                with lock:
                    current_wallets = {w for w, _, _, _ in top5}
                    for w, name, roi, ratio in top5:
                        if w not in watched_meta:
                            watched_meta[w] = {"username": name, "added_at": time.time(), "roi_pct": round(roi, 2),
                                                "short_term_pct": round(ratio * 100, 1)}
                        else:
                            watched_meta[w]["username"] = name
                            watched_meta[w]["roi_pct"] = round(roi, 2)
                            watched_meta[w]["short_term_pct"] = round(ratio * 100, 1)
                    for w in list(watched_meta.keys()):
                        if w not in current_wallets and watched_meta[w]["added_at"] < cutoff:
                            del watched_meta[w]
                    watched.clear()
                    watched.update({w: m["username"] for w, m in watched_meta.items()})
                print(f"[ranking] top {TOP_K_REPLICATE} por %% de rendimiento (corto plazo): "
                      + ", ".join(f"{m['username']} ({m['roi_pct']:+.1f}%, {m['short_term_pct']:.0f}% corto plazo)"
                                  for m in watched_meta.values()))
                last_lb_refresh = time.time()
        except Exception as e:
            import traceback
            print(f"[ranking_worker] error, se ignora y se reintenta en el próximo ciclo: {e}", file=sys.stderr)
            traceback.print_exc()
        time.sleep(10)


def background_worker():
    """Hilo liviano: guarda, resuelve apuestas pendientes y cuida la
    conexión. Corre siempre a tiempo, sin depender de lo que tarde el
    análisis de ranking (ese vive en ranking_worker, aparte)."""
    global last_msg_at
    last_resolve_check = 0
    last_save = time.time()
    while not stop_flag.is_set():
        try:
            now = time.time()

            if now - last_resolve_check > 60:
                resolve_pending_trades()
                last_resolve_check = now

            if now - last_msg_at > 60 and current_ws is not None:
                try:
                    current_ws.close()
                except Exception:
                    pass
                last_msg_at = time.time()

            if now - last_save > 120:
                save_and_commit()
                last_save = now

            if now - run_start > MAX_RUNTIME_SECONDS and current_ws is not None:
                print("[paper] tiempo máximo alcanzado, cerrando para terminar prolijo...")
                try:
                    current_ws.close()
                except Exception:
                    pass
                stop_flag.set()

        except Exception as e:
            import traceback
            print(f"[background_worker] error en un ciclo, se ignora y se sigue: {e}", file=sys.stderr)
            traceback.print_exc()

        time.sleep(5)


def main():
    global bankroll
    state = load_json(STATE_FILE)
    if state:
        bankroll = state.get("bankroll", INITIAL_BANKROLL)
        bankroll_history.extend(state.get("history", []))
        print(f"[paper] bankroll cargado: ${bankroll:,.2f}")

    loaded_trades = load_json(TRADES_FILE, [])
    trades.extend(loaded_trades)

    loaded_watched = load_json(WATCHED_FILE, {})
    watched_meta.update(loaded_watched)
    watched.update({w: m["username"] for w, m in watched_meta.items()})

    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        send_telegram(f"✅ Paper trading bot conectado — bankroll simulado: ${bankroll:,.2f}")

    bg = threading.Thread(target=background_worker, daemon=True)
    bg.start()
    rk = threading.Thread(target=ranking_worker, daemon=True)
    rk.start()

    while not watched and time.time() - run_start < 60:
        time.sleep(1)

    global current_ws, last_msg_at
    ws = websocket.WebSocketApp(
        RTDS_URL, on_open=on_ws_open, on_message=on_ws_message,
        on_error=on_ws_error, on_close=on_ws_close,
    )
    current_ws = ws
    last_msg_at = time.time()

    while time.time() - run_start < MAX_RUNTIME_SECONDS:
        ws.run_forever(ping_interval=30, ping_timeout=10)
        if time.time() - run_start >= MAX_RUNTIME_SECONDS:
            break
        print("[paper] reintentando conexión en 5s...")
        time.sleep(5)

    stop_flag.set()
    resolve_pending_trades()
    save_and_commit()
    print("Ciclo terminado — GitHub va a arrancar uno nuevo con el cron.")


if __name__ == "__main__":
    main()
