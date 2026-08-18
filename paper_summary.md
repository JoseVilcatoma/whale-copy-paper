# Paper trading — resultado de la simulación

Actualizado: 2026-08-18 16:57:26 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $498.04
**Retorno acumulado:** -0.39%
**Peor caída desde un máximo (drawdown):** 4.67%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $180.00 en 36 posiciones abiertas (disponible para nuevas apuestas: $318.04)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 22 | 1 | 8 | +31.60 USD |
| RN1 | 1 | 1 | 0 | +1.91 USD |
| theowalcott | 0 | 0 | 1 | +0.00 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 0 | 0 | 1 | +0.00 USD |
| alaskabaked | 0 | 1 | 2 | -5.09 USD |
| ferrariChampions2026 | 24 | 13 | 24 | -30.40 USD |

## Análisis general

- **Apuestas resueltas:** 63
- **Aciertos:** 47 (74.6%)
- **Cuota promedio de entrada:** 74.2%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $315.00
- **ROI sobre lo apostado:** -0.63%
- **Comisiones pagadas (taker fee):** $4.07 (1.29% del capital apostado)
- **ROI que habría dado SIN comisiones:** +0.66% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 14 | 42.9% | 48.1% | -5.2 pp |
| 60-79% | 22 | 77.3% | 70.0% | +7.3 pp |
| 80-94% | 19 | 84.2% | 88.2% | -4.0 pp |
| 95-99% (casi seguro) | 8 | 100.0% | 98.2% | +1.8 pp |

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
| atp-faria-walton-2026-08-18 | alaskabaked, ferrariChampions2026, swisstony |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | Los Angeles Dodgers vs. Colorado Rockies | Los Angeles Dodgers (BUY) | 65% | 5.00 | 5.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Luis Carlos Alvarez vs Rio Noguc | Luis Carlos Alvarez (BUY) | 49% | 5.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Dali Blanch vs Felipe Meligeni A | Dali Blanch (BUY) | 60% | 5.00 | 1.0% | ⏳ pendiente | — |
| swisstony | Cincinnati Open: Jaime Faria vs Adam Wal | Jaime Faria (BUY) | 65% | 5.00 | 0.4% | ⏳ pendiente | — |
| swisstony | Will Deportivo Riestra AFBC win on 2026- | No (BUY) | 82% | 5.00 | 0.2% | ⏳ pendiente | — |
| swisstony | Will Gimnasia y Esgrima La Plata win on  | No (BUY) | 72% | 5.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Set 1 Winner: Faria vs Walton | Faria (BUY) | 49% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Jaime Faria vs Adam Wal | Jaime Faria (BUY) | 56% | 5.00 | 6.3% | ⏳ pendiente | — |
| swisstony | Deportivo Riestra AFBC vs. Gimnasia y Es | Under (BUY) | 96% | 5.00 | 1.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Dali Blanch vs Felipe Meligeni A | Felipe Meligeni Alves (BUY) | 69% | 5.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Chicago White Sox vs. Chicago Cubs: O/U  | Over (BUY) | 59% | 5.00 | 1.2% | ⏳ pendiente | — |
| swisstony | Deportivo Riestra AFBC vs. Gimnasia y Es | Under (BUY) | 78% | 5.00 | 0.2% | ⏳ pendiente | — |
| alaskabaked | Cincinnati Open: Jaime Faria vs Adam Wal | Jaime Faria (BUY) | 59% | 5.00 | 23.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Jaime Faria vs Adam Wal | Adam Walton (BUY) | 44% | 5.00 | 9.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Miami Marlins vs. Philadelphia Phillies: | Over (BUY) | 49% | 5.00 | 0.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Andrea Pellegrino vs Nishes | Andrea Pellegrino (BUY) | 44% | 5.00 | 0.4% | ✅ ganada | +6.22 |
| ferrariChampions2026 | Cincinnati Open: Sara Bejlek vs Ekaterin | Ekaterina Alexandrova (BUY) | 51% | 5.00 | 3.4% | ⏳ pendiente | — |
| alaskabaked | Cincinnati Open: Sara Bejlek vs Ekaterin | Ekaterina Alexandrova (BUY) | 50% | 5.00 | 40.3% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: INTZ e-Sports vs 7REX (BO3) - Circu | INTZ e-Sports (BUY) | 93% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Fenerbahçe SK vs. Olympique Lyonnais: O/ | Under (BUY) | 99% | 5.00 | 0.4% | ✅ ganada | +0.05 |
| ferrariChampions2026 | Kingston: Lucas Da Silva vs Tyler Zink | Lucas Da Silva (BUY) | 66% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Fenerbahçe SK vs. Olympique Lyonnais: O/ | Under (BUY) | 44% | 5.00 | 4.3% | ✅ ganada | +6.22 |
| ferrariChampions2026 | Spread: GNK Dinamo Zagreb (-2.5) | Viking FK (BUY) | 98% | 5.00 | 0.4% | ✅ ganada | +0.10 |
| ferrariChampions2026 | Cincinnati Open: Marta Kostyuk vs Sloane | Marta Kostyuk (BUY) | 86% | 5.00 | 2.7% | ✅ ganada | +0.78 |
| ferrariChampions2026 | Will PFK Levski Sofia win on 2026-08-18? | No (BUY) | 82% | 5.00 | 1.2% | ✅ ganada | +1.05 |
| alaskabaked | Set Handicap: Gauff (-1.5) vs Li (+1.5) | Li (BUY) | 65% | 5.00 | 4.9% | ❌ perdida | -5.09 |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Atlanta Braves vs. Minnesota Twins | Atlanta Braves (BUY) | 56% | 5.00 | 139.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Jurij Rodionov vs Rei Sakam | Rei Sakamoto (BUY) | 63% | 5.00 | 1.2% | ✅ ganada | +2.84 |
| ferrariChampions2026 | Will Fenerbahçe SK win on 2026-08-18? | No (BUY) | 83% | 5.00 | 0.8% | ✅ ganada | +0.98 |
| ferrariChampions2026 | Cincinnati Open: Coco Gauff vs Ann Li | Coco Gauff (BUY) | 98% | 5.00 | 4.2% | ✅ ganada | +0.10 |
