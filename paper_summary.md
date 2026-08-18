# Paper trading — resultado de la simulación

Actualizado: 2026-08-18 15:12:55 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $507.18
**Retorno acumulado:** +1.44%
**Peor caída desde un máximo (drawdown):** 1.00%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $335.00 en 67 posiciones abiertas (disponible para nuevas apuestas: $172.18)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| RN1 | 1 | 0 | 1 | +7.05 USD |
| swisstony | 2 | 0 | 24 | +1.28 USD |
| theowalcott | 0 | 0 | 1 | +0.00 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 0 | 0 | 1 | +0.00 USD |
| ferrariChampions2026 | 2 | 1 | 40 | -1.14 USD |

## Análisis general

- **Apuestas resueltas:** 6
- **Aciertos:** 5 (83.3%)
- **Cuota promedio de entrada:** 71.0%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $30.00
- **ROI sobre lo apostado:** +23.97%
- **Comisiones pagadas (taker fee):** $0.44 (1.45% del capital apostado)
- **ROI que habría dado SIN comisiones:** +25.42% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 1 | 100.0% | 41.0% | +59.0 pp |
| 60-79% | 3 | 66.7% | 69.0% | -2.3 pp |
| 80-94% | 1 | 100.0% | 81.0% | +19.0 pp |
| 95-99% (casi seguro) | 1 | 100.0% | 97.0% | +3.0 pp |

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
| ucl-fen-lyo-2026-08-18-total-2pt5 | ferrariChampions2026, swisstony |
| ucl-fen-lyo-2026-08-18-spread-home-2pt5 | ferrariChampions2026, swisstony |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | Atlanta Braves vs. Minnesota Twins | Atlanta Braves (BUY) | 56% | 5.00 | 139.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Jurij Rodionov vs Rei Sakam | Rei Sakamoto (BUY) | 63% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Fenerbahçe SK win on 2026-08-18? | No (BUY) | 83% | 5.00 | 0.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Coco Gauff vs Ann Li | Coco Gauff (BUY) | 98% | 5.00 | 2.8% | ⏳ pendiente | — |
| ferrariChampions2026 | New York Yankees vs. Baltimore Orioles | Baltimore Orioles (BUY) | 50% | 5.00 | 0.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Andrea Pellegrino vs Nishes | Nishesh Basavareddy (BUY) | 88% | 5.00 | 3.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Will GNK Dinamo Zagreb win on 2026-08-18 | Yes (BUY) | 79% | 5.00 | 0.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: Donstu Esports vs MOUZ N | MOUZ NXT (BUY) | 93% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Fenerbahçe SK vs. Olympique Lyonnais: O/ | Under (BUY) | 41% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Arizona Diamondbacks vs. Boston Red Sox | Arizona Diamondbacks (BUY) | 41% | 5.00 | 1.9% | ⏳ pendiente | — |
| theowalcott | Deportivo Riestra AFBC vs. Gimnasia y Es | Over (BUY) | 57% | 5.00 | 99.8% | ⏳ pendiente | — |
| swisstony | GNK Dinamo Zagreb vs. Viking FK: O/U 3.5 | Over (BUY) | 71% | 5.00 | 0.1% | ⏳ pendiente | — |
| swisstony | Will Fenerbahçe SK win on 2026-08-18? | No (BUY) | 51% | 5.00 | 0.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Set 1 Winner: Kostyuk vs Stephens | Stephens (BUY) | 56% | 5.00 | 0.2% | ⏳ pendiente | — |
| swisstony | Spread: Fenerbahçe SK (-1.5) | Olympique Lyonnais (BUY) | 78% | 5.00 | 0.2% | ⏳ pendiente | — |
| swisstony | Fenerbahçe SK vs. Olympique Lyonnais: Fe | Under (BUY) | 87% | 5.00 | 0.2% | ⏳ pendiente | — |
| swisstony | Fenerbahçe SK vs. Olympique Lyonnais: Fe | Under (BUY) | 61% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: Fire Flux Esports vs WRA | WRAITH PCIFIC (BUY) | 47% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Viking FK win on 2026-08-18? | No (BUY) | 99% | 5.00 | 0.3% | ⏳ pendiente | — |
| swisstony | Kingston: Valentin Royer vs Luis Guto Mi | Valentin Royer (BUY) | 82% | 5.00 | 0.1% | ⏳ pendiente | — |
| swisstony | Will Al Diraiyah Saudi Club vs. Al Nassr | No (BUY) | 99% | 5.00 | 0.2% | ⏳ pendiente | — |
| swisstony | Fenerbahçe SK vs. Olympique Lyonnais: O/ | Under (BUY) | 62% | 5.00 | 0.3% | ⏳ pendiente | — |
| swisstony | ITF M25 Ueberlingen Men: Calvin Mueller  | Daniel Masur (BUY) | 97% | 5.00 | 1.9% | ✅ ganada | +0.15 |
| ferrariChampions2026 | St. Louis Cardinals vs. Cincinnati Reds | Cincinnati Reds (BUY) | 49% | 5.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | St. Louis Cardinals vs. Cincinnati Reds: | Under (BUY) | 58% | 5.00 | 0.5% | ⏳ pendiente | — |
| swisstony | Will Club Atlético de Madrid win on 2026 | Yes (BUY) | 74% | 5.00 | 0.4% | ⏳ pendiente | — |
| swisstony | GNK Dinamo Zagreb vs. Viking FK: Both Te | Yes (BUY) | 67% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Set 1 Winner: Nakashima vs Medvedev | Nakashima (BUY) | 89% | 5.00 | 0.7% | ⏳ pendiente | — |
| swisstony | Spread: Fenerbahçe SK (-2.5) | Olympique Lyonnais (BUY) | 92% | 5.00 | 0.6% | ⏳ pendiente | — |
| swisstony | Spread: GNK Dinamo Zagreb (-2.5) | Viking FK (BUY) | 52% | 5.00 | 0.1% | ⏳ pendiente | — |
