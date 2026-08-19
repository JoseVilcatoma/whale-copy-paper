# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 09:08:04 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $505.05
**Retorno acumulado:** +1.01%
**Peor caída desde un máximo (drawdown):** 8.51%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $295.00 en 59 posiciones abiertas (disponible para nuevas apuestas: $210.05)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 3 | 0 | 0 | +10.20 USD |
| RN1 | 10 | 3 | 16 | +4.55 USD |
| HomeRunHazard | 4 | 1 | 4 | +2.93 USD |
| sentrio | 2 | 2 | 3 | +0.78 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 0 | 0 | 4 | +0.00 USD |
| jtwyslljy | 0 | 0 | 1 | +0.00 USD |
| BOOMBOYS.Kiritych | 0 | 0 | 3 | +0.00 USD |
| Lakersfan111 | 0 | 0 | 2 | +0.00 USD |
| SDTrading | 0 | 0 | 1 | +0.00 USD |
| HVAB | 0 | 0 | 1 | +0.00 USD |
| theowalcott | 1 | 1 | 0 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 1 | -4.12 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 0 | -5.75 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| Sassy-Bucket | 0 | 3 | 0 | -15.38 USD |
| ferrariChampions2026 | 80 | 48 | 22 | -21.80 USD |

## Análisis general

- **Apuestas resueltas:** 199
- **Aciertos:** 133 (66.8%)
- **Cuota promedio de entrada:** 64.8%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $995.00
- **ROI sobre lo apostado:** +0.51%
- **Comisiones pagadas (taker fee):** $17.51 (1.76% del capital apostado)
- **ROI que habría dado SIN comisiones:** +2.27% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 90 | 46.7% | 49.8% | -3.1 pp |
| 60-79% | 65 | 76.9% | 68.5% | +8.4 pp |
| 80-94% | 31 | 90.3% | 87.0% | +3.3 pp |
| 95-99% (casi seguro) | 13 | 100.0% | 97.7% | +2.3 pp |

## Mercados donde coincidieron 2+ vigilados (para calibrar el tope futuro)

| Mercado | Vigilados que coincidieron |
|---|---|
| atp-lajovic-daniel-2026-08-18 | RN1, ferrariChampions2026 |
| atp-sakella-schoolk-2026-08-18 | RN1, ferrariChampions2026 |
| atp-johns-santos-2026-08-18 | ferrariChampions2026, swisstony |
| atp-royer-miguel-2026-08-17 | ferrariChampions2026, swisstony |
| ucl-pls-aek1-2026-08-18-aek1 | ferrariChampions2026, swisstony |
| ucl-fen-lyo-2026-08-18-lyo | ferrariChampions2026, swisstony |
| atp-nakashi-medvede-2026-08-18 | ferrariChampions2026, swisstony |
| mlb-atl-min-2026-08-18 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, ferrariChampions2026 |
| itf-mubarak-boschma-2026-08-19 | ferrariChampions2026, sentrio |
| ucl-fen-lyo-2026-08-18-fen | ferrariChampions2026, swisstony |
| ucl-fen-lyo-2026-08-18-total-1pt5 | ferrariChampions2026, swisstony |
| ucl-fen-lyo-2026-08-18-spread-home-1pt5 | ferrariChampions2026, swisstony |
| ucl-pls-aek1-2026-08-18-pls | ferrariChampions2026, swisstony |
| ucl-fen-lyo-2026-08-18-total-2pt5 | ferrariChampions2026, swisstony |
| ucl-fen-lyo-2026-08-18-spread-home-2pt5 | ferrariChampions2026, swisstony |
| ucl-din-vf-2026-08-18-spread-home-2pt5 | ferrariChampions2026, swisstony |
| wta-bejlek-alexand-2026-08-18 | alaskabaked, ferrariChampions2026 |
| mlb-mia-phi-2026-08-18-total-8pt5 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, ferrariChampions2026 |
| atp-faria-walton-2026-08-18 | alaskabaked, ferrariChampions2026, sentrio, swisstony |
| mlb-lad-col-2026-08-18 | HomeRunHazard, ferrariChampions2026 |
| atp-tien-tiafoe-2026-08-18 | ferrariChampions2026, sentrio |
| mlb-tor-tb-2026-08-18 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, ferrariChampions2026 |
| atp-svrcina-wawrink-2026-08-18 | danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| mlb-wsh-tex-2026-08-18-total-8pt5 | Sassy-Bucket, ferrariChampions2026 |
| mlb-lad-col-2026-08-18-total-11pt5 | Sassy-Bucket, ferrariChampions2026 |
| wta-bouzkov-jovic-2026-08-18 | HomeRunHazard, danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| atp-ruiz-comesan-2026-08-18 | HomeRunHazard, danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| cs2-g2-ast10-2026-08-19 | BOOMBOYS.Kiritych, sentrio |
| lol-al-tes-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, ferrariChampions2026, jtwyslljy |
| atp-maxted-brady-2026-08-19 | RN1, ferrariChampions2026 |
| lol-we-edg-2026-08-19-game-handicap-away-1pt5 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, Lakersfan111 |
| atp-giustin-bernet-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-mia-phi-2026-08-19-total-8pt5 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, HomeRunHazard |
| atp-molleke-jianu-2026-08-19 | RN1, ferrariChampions2026 |
| chi-shp-ygb-2026-07-12-ygb | RN1, ferrariChampions2026 |
| atp-geerts-albot-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-mia-phi-2026-08-19 | SDTrading, ferrariChampions2026 |
| atp-papoe-cosano-2026-08-19 | RN1, ferrariChampions2026 |
| itf-gniewko-pere-2026-08-19 | HVAB, RN1 |
| atp-almeida-tarvet-2026-08-19 | HomeRunHazard, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| HomeRunHazard | Roehampton: Matheus Pucinelli de Almeida | Oliver Tarvet (BUY) | 88% | 5.00 | 3.6% | ⏳ pendiente | — |
| HomeRunHazard | Minnesota Lynx vs. Golden State Valkyrie | Over (BUY) | 49% | 5.00 | 1.9% | ⏳ pendiente | — |
| HomeRunHazard | Miami Marlins vs. Philadelphia Phillies: | Over (BUY) | 51% | 5.00 | 6.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Roehampton: Matheus Pucinelli de Almeida | Oliver Tarvet (BUY) | 86% | 5.00 | 0.6% | ⏳ pendiente | — |
| RN1 | ITF M25 Idanha-a-Nova 2 Men: Mathieu Sca | Maxwell McKennon (BUY) | 69% | 5.00 | 1.0% | ⏳ pendiente | — |
| RN1 | ITF W35 Krakow Women: Amelia Paszun vs R | Radka Zelnickova (BUY) | 47% | 5.00 | 1.9% | ⏳ pendiente | — |
| RN1 | ITF W35 Krakow Women: Oriana Gniewkowska | Oriana Gniewkowska (BUY) | 59% | 5.00 | 0.7% | ⏳ pendiente | — |
| RN1 | ITF W50 Prague Women: Anna Siskova vs Ye | Yelyzaveta Kotliar (BUY) | 42% | 5.00 | 2.1% | ⏳ pendiente | — |
| HVAB | ITF W35 Krakow Women: Oriana Gniewkowska | Oriana Gniewkowska (BUY) | 63% | 5.00 | 1642.1% | ⏳ pendiente | — |
| ferrariChampions2026 | KBO: KT Wiz vs. LG Twins | LG Twins (BUY) | 44% | 5.00 | 0.4% | ⏳ pendiente | — |
| RN1 | ITF M15 Lambermont Men: Nicolas Robert v | Nicolas Robert (BUY) | 47% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: SPARTA vs MOUZ NXT (BO3) | SPARTA (BUY) | 89% | 5.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Team WE vs EDward Gaming - Game 1 W | EDward Gaming (BUY) | 69% | 5.00 | 3.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Sion: Mika Brunold vs Calvin Hemery | Mika Brunold (BUY) | 83% | 5.00 | 7.2% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Team WE vs EDward Gaming (BO3) - LP | Team WE (BUY) | 74% | 5.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Team WE vs EDward Gaming - Game 1 W | Team WE (BUY) | 60% | 5.00 | 0.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Roehampton: Viktor Durasovic vs Lucas Po | Lucas Poullain (BUY) | 63% | 5.00 | 1.7% | ⏳ pendiente | — |
| RN1 | ITF M25 Santander Men: Pedro Rodenas vs  | Pedro Rodenas (BUY) | 66% | 5.00 | 1.7% | ⏳ pendiente | — |
| RN1 | ITF W75 Kursumlijska Banja 3 Women: Beat | Beatrice Ricci (BUY) | 81% | 5.00 | 1.2% | ⏳ pendiente | — |
| RN1 | Roehampton: Mark Ceban vs Iliyan Radulov | Mark Ceban (BUY) | 47% | 5.00 | 0.8% | ⏳ pendiente | — |
| RN1 | Will Dalian Yingbo FC win on 2026-07-12? | No (BUY) | 94% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | Prague 2: Radu Mihai Papoe vs Javier Bar | Radu Mihai Papoe (BUY) | 64% | 5.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Prague 2: Radu Mihai Papoe vs Javier Bar | Radu Mihai Papoe (BUY) | 68% | 5.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Sion: Lorenzo Giustino vs Henry Bernet | Henry Bernet (BUY) | 60% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: SPARTA vs MOUZ NXT - Map | SPARTA (BUY) | 76% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Miami Marlins vs. Philadelphia Phillies | Miami Marlins (BUY) | 46% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | ITF W15 Wanfercée-Baulet Women: Galatea  | Galatea Ferro (BUY) | 84% | 5.00 | 1.4% | ✅ ganada | +0.91 |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | Counter-Strike: FUT Esports vs magic (BO | FUT Esports (BUY) | 66% | 5.00 | 7.4% | ⏳ pendiente | — |
| RN1 | ITF W50 Prague Women: Anna Siskova vs Ye | Anna Siskova (BUY) | 61% | 5.00 | 0.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Roehampton: Michael Geerts vs Radu Albot | Radu Albot (BUY) | 69% | 5.00 | 1.9% | ⏳ pendiente | — |
