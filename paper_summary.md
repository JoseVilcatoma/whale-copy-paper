# Paper trading — resultado de la simulación

Actualizado: 2026-08-18 20:23:40 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $525.45
**Retorno acumulado:** +5.09%
**Peor caída desde un máximo (drawdown):** 4.67%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $255.00 en 51 posiciones abiertas (disponible para nuevas apuestas: $270.45)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| theowalcott | 1 | 0 | 1 | +3.66 USD |
| RN1 | 1 | 1 | 0 | +1.91 USD |
| sentrio | 1 | 1 | 1 | +0.39 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 1 | 1 | 3 | +0.38 USD |
| Sassy-Bucket | 0 | 0 | 3 | +0.00 USD |
| danielwolfmorales3pddb6dl6 | 0 | 0 | 1 | +0.00 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| ferrariChampions2026 | 37 | 20 | 41 | -16.02 USD |

## Análisis general

- **Apuestas resueltas:** 97
- **Aciertos:** 71 (73.2%)
- **Cuota promedio de entrada:** 69.6%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $485.00
- **ROI sobre lo apostado:** +5.25%
- **Comisiones pagadas (taker fee):** $7.38 (1.52% del capital apostado)
- **ROI que habría dado SIN comisiones:** +6.77% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 32 | 53.1% | 48.8% | +4.3 pp |
| 60-79% | 33 | 75.8% | 69.2% | +6.6 pp |
| 80-94% | 22 | 86.4% | 87.4% | -1.0 pp |
| 95-99% (casi seguro) | 10 | 100.0% | 98.1% | +1.9 pp |

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
| atp-svrcina-wawrink-2026-08-18 | danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| mlb-lad-col-2026-08-18-total-11pt5 | Sassy-Bucket, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| danielwolfmorales3pddb6dl6 | Cancun: Dalibor Svrcina vs Stan Wawrinka | Stan Wawrinka (BUY) | 52% | 5.00 | 29.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Atlanta Dream vs. Las Vegas Aces: O/U 17 | Over (BUY) | 52% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Atlanta Dream vs. Las Vegas Aces | Atlanta Dream (BUY) | 45% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Washington Nationals vs. Texas Rangers:  | Under (BUY) | 52% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Chicago Cubs (-2.5) | Chicago White Sox (BUY) | 48% | 5.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Boston Red Sox (-1.5) | Boston Red Sox (BUY) | 52% | 5.00 | 1.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Toronto Blue Jays (-4.5) | Tampa Bay Rays (BUY) | 54% | 5.00 | 1.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Milwaukee Brewers (-1.5) | Seattle Mariners (BUY) | 45% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Los Angeles Dodgers vs. Colorado Rockies | Over (BUY) | 52% | 5.00 | 0.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Atlanta Braves vs. Minnesota Twins: O/U  | Under (BUY) | 44% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Miami Marlins vs. Philadelphia Phillies | Miami Marlins (BUY) | 41% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Indiana Fever (-10.5) | Indiana Fever (BUY) | 55% | 5.00 | 0.2% | ⏳ pendiente | — |
| Sassy-Bucket | Los Angeles Dodgers vs. Colorado Rockies | Under (BUY) | 50% | 5.00 | 42.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Washington Nationals vs. Texas Rangers | Texas Rangers (BUY) | 58% | 5.00 | 1.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Atlanta Braves vs. Minnesota Twins | Minnesota Twins (BUY) | 65% | 5.00 | 6.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Indiana Fever vs. Toronto Tempo: O/U 191 | Over (BUY) | 51% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Milwaukee Brewers (-2.5) | Seattle Mariners (BUY) | 67% | 5.00 | 2.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Athletics vs. Kansas City Royals | Athletics (BUY) | 46% | 5.00 | 2.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Kingston: Joel Schwaerzler vs Kenta Miyo | Kenta Miyoshi (BUY) | 81% | 5.00 | 3.3% | ✅ ganada | +1.13 |
| Sassy-Bucket | Washington Nationals vs. Texas Rangers:  | Over (BUY) | 44% | 5.00 | 14.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Los Angeles Sparks vs. Connecticut Sun | Connecticut Sun (BUY) | 66% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Juan Manuel Cerundolo v | Felix Auger-Aliassime (BUY) | 73% | 5.00 | 3.7% | ✅ ganada | +1.78 |
| ferrariChampions2026 | Arizona Diamondbacks vs. Boston Red Sox: | Over (BUY) | 50% | 5.00 | 0.1% | ✅ ganada | +4.88 |
| ferrariChampions2026 | Spread: Boston Red Sox (-2.5) | Boston Red Sox (BUY) | 65% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Athletics vs. Kansas City Royals | Kansas City Royals (BUY) | 60% | 5.00 | 7.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Dalibor Svrcina vs Stan Wawrinka | Dalibor Svrcina (BUY) | 76% | 5.00 | 0.2% | ⏳ pendiente | — |
| Sassy-Bucket | New York Liberty vs. Chicago Sky: O/U 17 | Over (BUY) | 52% | 5.00 | 22.4% | ⏳ pendiente | — |
| theowalcott | CD Tolima vs. Independiente del Valle: O | Over (BUY) | 65% | 5.00 | 7.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Kingston: Lucas Da Silva vs Tyler Zink | Tyler Zink (BUY) | 47% | 5.00 | 2.0% | ✅ ganada | +5.51 |
| ferrariChampions2026 | San Francisco Giants vs. Cleveland Guard | Cleveland Guardians (BUY) | 84% | 5.00 | 5.2% | ⏳ pendiente | — |
