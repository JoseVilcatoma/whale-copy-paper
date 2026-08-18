# Paper trading — resultado de la simulación

Actualizado: 2026-08-18 17:45:15 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $498.41
**Retorno acumulado:** -0.32%
**Peor caída desde un máximo (drawdown):** 4.67%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $205.00 en 41 posiciones abiertas (disponible para nuevas apuestas: $293.41)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 24 | 1 | 6 | +34.88 USD |
| RN1 | 1 | 1 | 0 | +1.91 USD |
| theowalcott | 0 | 0 | 1 | +0.00 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 0 | 0 | 5 | +0.00 USD |
| sentrio | 0 | 0 | 2 | +0.00 USD |
| alaskabaked | 0 | 1 | 2 | -5.09 USD |
| ferrariChampions2026 | 27 | 16 | 25 | -33.32 USD |

## Análisis general

- **Apuestas resueltas:** 71
- **Aciertos:** 52 (73.2%)
- **Cuota promedio de entrada:** 73.1%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $355.00
- **ROI sobre lo apostado:** -0.46%
- **Comisiones pagadas (taker fee):** $4.78 (1.35% del capital apostado)
- **ROI que habría dado SIN comisiones:** +0.89% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 18 | 44.4% | 48.3% | -3.8 pp |
| 60-79% | 24 | 75.0% | 69.8% | +5.2 pp |
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

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| sentrio | Cincinnati Open: Jaime Faria vs Adam Wal | Adam Walton (BUY) | 51% | 5.00 | 0.4% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Miami Marlins vs. Philadelphia Phillies: | Under (BUY) | 47% | 5.00 | 6.0% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Toronto Blue Jays vs. Tampa Bay Rays | Toronto Blue Jays (BUY) | 46% | 5.00 | 12.6% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Miami Marlins vs. Philadelphia Phillies: | Under (BUY) | 54% | 5.00 | 1.1% | ⏳ pendiente | — |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Detroit Tigers vs. Pittsburgh Pirates: O | Under (BUY) | 47% | 5.00 | 19.2% | ⏳ pendiente | — |
| sentrio | Cincinnati Open: Learner Tien vs Frances | Frances Tiafoe (BUY) | 47% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Sara Bejlek vs Ekaterin | Sara Bejlek (BUY) | 60% | 5.00 | 2.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Washington Nationals vs. Texas Rangers | Washington Nationals (BUY) | 43% | 5.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Luis Carlos Alvarez vs Rio Noguc | Rio Noguchi (BUY) | 58% | 5.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Roman Safiullin vs Sebastian Ofn | Roman Safiullin (BUY) | 66% | 5.00 | 1.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Arizona Diamondbacks vs. Boston Red Sox: | Over (BUY) | 45% | 5.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Fluminense FC win on 2026-08-18? | No (BUY) | 72% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Jesper de Jong vs Dane Swee | Jesper de Jong (BUY) | 42% | 5.00 | 5.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Los Angeles Dodgers vs. Colorado Rockies | Los Angeles Dodgers (BUY) | 65% | 5.00 | 5.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Luis Carlos Alvarez vs Rio Noguc | Luis Carlos Alvarez (BUY) | 49% | 5.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Dali Blanch vs Felipe Meligeni A | Dali Blanch (BUY) | 60% | 5.00 | 1.0% | ⏳ pendiente | — |
| swisstony | Cincinnati Open: Jaime Faria vs Adam Wal | Jaime Faria (BUY) | 65% | 5.00 | 0.4% | ⏳ pendiente | — |
| swisstony | Will Deportivo Riestra AFBC win on 2026- | No (BUY) | 82% | 5.00 | 0.2% | ⏳ pendiente | — |
| swisstony | Will Gimnasia y Esgrima La Plata win on  | No (BUY) | 72% | 5.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Set 1 Winner: Faria vs Walton | Faria (BUY) | 49% | 5.00 | 0.5% | ❌ perdida | -5.13 |
| ferrariChampions2026 | Cincinnati Open: Jaime Faria vs Adam Wal | Jaime Faria (BUY) | 56% | 5.00 | 8.0% | ⏳ pendiente | — |
| swisstony | Deportivo Riestra AFBC vs. Gimnasia y Es | Under (BUY) | 96% | 5.00 | 1.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Dali Blanch vs Felipe Meligeni A | Felipe Meligeni Alves (BUY) | 69% | 5.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Chicago White Sox vs. Chicago Cubs: O/U  | Over (BUY) | 59% | 5.00 | 1.2% | ⏳ pendiente | — |
| swisstony | Deportivo Riestra AFBC vs. Gimnasia y Es | Under (BUY) | 78% | 5.00 | 0.2% | ⏳ pendiente | — |
| alaskabaked | Cincinnati Open: Jaime Faria vs Adam Wal | Jaime Faria (BUY) | 59% | 5.00 | 23.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Jaime Faria vs Adam Wal | Adam Walton (BUY) | 44% | 5.00 | 17.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Miami Marlins vs. Philadelphia Phillies: | Over (BUY) | 49% | 5.00 | 0.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Andrea Pellegrino vs Nishes | Andrea Pellegrino (BUY) | 44% | 5.00 | 0.4% | ✅ ganada | +6.22 |
| ferrariChampions2026 | Cincinnati Open: Sara Bejlek vs Ekaterin | Ekaterina Alexandrova (BUY) | 51% | 5.00 | 4.4% | ⏳ pendiente | — |
