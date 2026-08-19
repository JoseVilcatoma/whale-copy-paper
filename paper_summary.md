# Paper trading — resultado de la simulación

Actualizado: 2026-08-18 19:01:16 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $505.69
**Retorno acumulado:** +1.14%
**Peor caída desde un máximo (drawdown):** 4.67%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $260.00 en 52 posiciones abiertas (disponible para nuevas apuestas: $245.69)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 25 | 1 | 5 | +37.49 USD |
| RN1 | 1 | 1 | 0 | +1.91 USD |
| sentrio | 1 | 1 | 1 | +0.39 USD |
| theowalcott | 0 | 0 | 2 | +0.00 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 0 | 0 | 5 | +0.00 USD |
| Sassy-Bucket | 0 | 0 | 2 | +0.00 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| ferrariChampions2026 | 31 | 18 | 37 | -27.28 USD |

## Análisis general

- **Apuestas resueltas:** 82
- **Aciertos:** 59 (72.0%)
- **Cuota promedio de entrada:** 70.5%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $410.00
- **ROI sobre lo apostado:** +1.38%
- **Comisiones pagadas (taker fee):** $6.06 (1.48% del capital apostado)
- **ROI que habría dado SIN comisiones:** +2.86% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 26 | 46.2% | 48.8% | -2.7 pp |
| 60-79% | 27 | 77.8% | 69.1% | +8.7 pp |
| 80-94% | 20 | 85.0% | 88.0% | -3.0 pp |
| 95-99% (casi seguro) | 9 | 100.0% | 98.3% | +1.7 pp |

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
| mlb-tor-tb-2026-08-18 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | Atlanta Braves vs. Minnesota Twins | Minnesota Twins (BUY) | 65% | 5.00 | 6.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Indiana Fever vs. Toronto Tempo: O/U 191 | Over (BUY) | 51% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Milwaukee Brewers (-2.5) | Seattle Mariners (BUY) | 67% | 5.00 | 2.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Athletics vs. Kansas City Royals | Athletics (BUY) | 46% | 5.00 | 2.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Kingston: Joel Schwaerzler vs Kenta Miyo | Kenta Miyoshi (BUY) | 81% | 5.00 | 2.2% | ⏳ pendiente | — |
| Sassy-Bucket | Washington Nationals vs. Texas Rangers:  | Over (BUY) | 44% | 5.00 | 8.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Los Angeles Sparks vs. Connecticut Sun | Connecticut Sun (BUY) | 66% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Juan Manuel Cerundolo v | Felix Auger-Aliassime (BUY) | 73% | 5.00 | 2.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Arizona Diamondbacks vs. Boston Red Sox: | Over (BUY) | 50% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Boston Red Sox (-2.5) | Boston Red Sox (BUY) | 65% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Athletics vs. Kansas City Royals | Kansas City Royals (BUY) | 60% | 5.00 | 6.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Dalibor Svrcina vs Stan Wawrinka | Dalibor Svrcina (BUY) | 76% | 5.00 | 0.2% | ⏳ pendiente | — |
| Sassy-Bucket | New York Liberty vs. Chicago Sky: O/U 17 | Over (BUY) | 52% | 5.00 | 22.4% | ⏳ pendiente | — |
| theowalcott | CD Tolima vs. Independiente del Valle: O | Over (BUY) | 65% | 5.00 | 7.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Kingston: Lucas Da Silva vs Tyler Zink | Tyler Zink (BUY) | 47% | 5.00 | 2.0% | ⏳ pendiente | — |
| ferrariChampions2026 | San Francisco Giants vs. Cleveland Guard | Cleveland Guardians (BUY) | 84% | 5.00 | 5.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Miami Marlins vs. Philadelphia Phillies | Philadelphia Phillies (BUY) | 68% | 5.00 | 0.8% | ⏳ pendiente | — |
| sentrio | Cincinnati Open: Jaime Faria vs Adam Wal | Jaime Faria (BUY) | 47% | 5.00 | 3.1% | ✅ ganada | +5.51 |
| ferrariChampions2026 | Los Angeles Sparks vs. Connecticut Sun:  | Under (BUY) | 52% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Toronto Blue Jays vs. Tampa Bay Rays | Toronto Blue Jays (BUY) | 65% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | New York Yankees vs. Baltimore Orioles | New York Yankees (BUY) | 49% | 5.00 | 9.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Arizona Diamondbacks vs. Boston Red Sox | Boston Red Sox (BUY) | 61% | 5.00 | 7.0% | ⏳ pendiente | — |
| sentrio | Cincinnati Open: Jaime Faria vs Adam Wal | Adam Walton (BUY) | 51% | 5.00 | 0.4% | ❌ perdida | -5.12 |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Miami Marlins vs. Philadelphia Phillies: | Under (BUY) | 47% | 5.00 | 7.9% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Toronto Blue Jays vs. Tampa Bay Rays | Toronto Blue Jays (BUY) | 46% | 5.00 | 12.6% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Miami Marlins vs. Philadelphia Phillies: | Under (BUY) | 54% | 5.00 | 3.8% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Detroit Tigers vs. Pittsburgh Pirates: O | Under (BUY) | 47% | 5.00 | 19.2% | ⏳ pendiente | — |
| sentrio | Cincinnati Open: Learner Tien vs Frances | Frances Tiafoe (BUY) | 47% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Sara Bejlek vs Ekaterin | Sara Bejlek (BUY) | 60% | 5.00 | 3.7% | ✅ ganada | +3.23 |
| ferrariChampions2026 | Washington Nationals vs. Texas Rangers | Washington Nationals (BUY) | 43% | 5.00 | 1.1% | ⏳ pendiente | — |
