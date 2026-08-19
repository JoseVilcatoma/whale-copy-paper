# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 07:35:42 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $507.46
**Retorno acumulado:** +1.49%
**Peor caída desde un máximo (drawdown):** 8.35%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $185.00 en 37 posiciones abiertas (disponible para nuevas apuestas: $322.46)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 2 | 0 | 1 | +9.36 USD |
| sentrio | 2 | 1 | 4 | +5.90 USD |
| RN1 | 2 | 1 | 11 | +4.40 USD |
| HomeRunHazard | 4 | 1 | 1 | +2.93 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 0 | 0 | 3 | +0.00 USD |
| jtwyslljy | 0 | 0 | 1 | +0.00 USD |
| BOOMBOYS.Kiritych | 0 | 0 | 3 | +0.00 USD |
| Lakersfan111 | 0 | 0 | 2 | +0.00 USD |
| theowalcott | 1 | 1 | 0 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 1 | -4.12 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 0 | -5.75 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| Sassy-Bucket | 0 | 3 | 0 | -15.38 USD |
| ferrariChampions2026 | 75 | 47 | 9 | -23.51 USD |

## Análisis general

- **Apuestas resueltas:** 181
- **Aciertos:** 119 (65.7%)
- **Cuota promedio de entrada:** 64.0%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $905.00
- **ROI sobre lo apostado:** +0.83%
- **Comisiones pagadas (taker fee):** $16.30 (1.80% del capital apostado)
- **ROI que habría dado SIN comisiones:** +2.63% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 86 | 48.8% | 49.8% | -0.9 pp |
| 60-79% | 58 | 74.1% | 68.0% | +6.1 pp |
| 80-94% | 25 | 88.0% | 87.3% | +0.7 pp |
| 95-99% (casi seguro) | 12 | 100.0% | 97.8% | +2.2 pp |

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
| lol-we-edg-2026-08-19-game-handicap-away-1pt5 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, Lakersfan111 |
| atp-giustin-bernet-2026-08-19 | RN1, ferrariChampions2026 |
| atp-molleke-jianu-2026-08-19 | RN1, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | Roehampton: Elmer Moeller vs Anton Matus | Anton Matusevich (BUY) | 51% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | ITF W35 Bistrita Women: Giulia Safina Po | Teodora Miron (BUY) | 71% | 5.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: HANJIN BRION vs DN SOOPers - Game 2 | HANJIN BRION (BUY) | 68% | 5.00 | 2.2% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Anyone's Legend vs Top Esports (BO3 | Anyone's Legend (BUY) | 81% | 5.00 | 11.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Shanghai Haigang FC win on 2026-07- | No (BUY) | 66% | 5.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Prague 2: Rudolf Molleker vs Filip Jianu | Filip Jianu (BUY) | 75% | 5.00 | 2.5% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: HANJIN BRION vs DN SOOPers (BO3) -  | HANJIN BRION (BUY) | 87% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Sion: Lorenzo Giustino vs Henry Bernet | Lorenzo Giustino (BUY) | 71% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Prague 2: Rudolf Molleker vs Filip Jianu | Filip Jianu (BUY) | 75% | 5.00 | 3.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Prague 2: Cezar Cretu vs Maxim Mrva | Maxim Mrva (BUY) | 87% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | ITF W75 Kursumlijska Banja 3 Women: Rada | Rada Zolotareva (BUY) | 80% | 5.00 | 1.6% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Miami Marlins vs. Philadelphia Phillies: | Under (BUY) | 51% | 5.00 | 15.3% | ⏳ pendiente | — |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | Game Handicap: WE (-1.5) vs EDward Gamin | EDward Gaming (BUY) | 50% | 5.00 | 3.7% | ⏳ pendiente | — |
| RN1 | ITF M25 Ueberlingen Men: Manuel Plunger  | Adrian Oetzbach (BUY) | 92% | 5.00 | 0.8% | ⏳ pendiente | — |
| RN1 | Roehampton: Gabi Boitan vs Alastair Gray | Gabi Boitan (BUY) | 96% | 5.00 | 1.1% | ⏳ pendiente | — |
| RN1 | Sion: Lorenzo Giustino vs Henry Bernet | Lorenzo Giustino (BUY) | 66% | 5.00 | 14.5% | ⏳ pendiente | — |
| Lakersfan111 | Dota 2: Iron Wing vs Team Spirit (BO3) - | Team Spirit (BUY) | 47% | 5.00 | 1.0% | ⏳ pendiente | — |
| RN1 | Sion: Jeffrey von der Schulenburg vs Geo | Geoffrey Blancaneaux (BUY) | 69% | 5.00 | 2.8% | ⏳ pendiente | — |
| Lakersfan111 | Game Handicap: WE (-1.5) vs EDward Gamin | EDward Gaming (BUY) | 48% | 5.00 | 1.2% | ⏳ pendiente | — |
| RN1 | Roehampton: Lui Maxted vs Patrick Brady | Lui Maxted (BUY) | 72% | 5.00 | 7.2% | ⏳ pendiente | — |
| BOOMBOYS.Kiritych | LoL: Anyone's Legend vs Top Esports - Ga | Anyone's Legend (BUY) | 55% | 5.00 | 36.0% | ⏳ pendiente | — |
| BOOMBOYS.Kiritych | LoL: HANJIN BRION vs DN SOOPers - Game 1 | DN SOOPers (BUY) | 44% | 5.00 | 20.7% | ⏳ pendiente | — |
| BOOMBOYS.Kiritych | Counter-Strike: G2 vs Astralis (BO3) - E | G2 (BUY) | 67% | 5.00 | 5.7% | ⏳ pendiente | — |
| RN1 | Prague 2: Juan Bautista Torres vs Chun-H | Chun-Hsin Tseng (BUY) | 79% | 5.00 | 33.7% | ⏳ pendiente | — |
| RN1 | ITF M15 Arad Men: Jacopo Bilardo vs Jere | Jeremy Gschwendtner (BUY) | 42% | 5.00 | 11.5% | ⏳ pendiente | — |
| RN1 | Sion: Luca Staeheli vs Juan Manuel La Se | Juan Manuel La Serna (BUY) | 66% | 5.00 | 11.8% | ✅ ganada | +2.49 |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | LoL: Gen.G vs KT Rolster - Game 1 Winner | Gen.G (BUY) | 85% | 5.00 | 33.1% | ⏳ pendiente | — |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | LoL: Anyone's Legend vs Top Esports (BO3 | Anyone's Legend (BUY) | 59% | 5.00 | 5.1% | ⏳ pendiente | — |
| jtwyslljy | LoL: Anyone's Legend vs Top Esports (BO3 | Anyone's Legend (BUY) | 59% | 5.00 | 365.5% | ⏳ pendiente | — |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | Will Celtic FC win on 2026-08-19? | No (BUY) | 45% | 5.00 | 2.9% | ⏳ pendiente | — |
