# Paper trading — resultado de la simulación

Actualizado: 2026-08-18 23:33:51 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $511.44
**Retorno acumulado:** +2.29%
**Peor caída desde un máximo (drawdown):** 6.23%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $75.00 en 15 posiciones abiertas (disponible para nuevas apuestas: $436.44)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| sentrio | 2 | 1 | 2 | +5.90 USD |
| HomeRunHazard | 3 | 0 | 2 | +3.91 USD |
| RN1 | 1 | 1 | 0 | +1.91 USD |
| danielwolfmorales3pddb6dl6 | 1 | 1 | 1 | -0.62 USD |
| theowalcott | 1 | 1 | 0 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 0 | -4.12 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| ferrariChampions2026 | 71 | 43 | 9 | -13.78 USD |
| Sassy-Bucket | 0 | 3 | 0 | -15.38 USD |

## Análisis general

- **Apuestas resueltas:** 167
- **Aciertos:** 111 (66.5%)
- **Cuota promedio de entrada:** 64.5%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $835.00
- **ROI sobre lo apostado:** +1.38%
- **Comisiones pagadas (taker fee):** $14.83 (1.78% del capital apostado)
- **ROI que habría dado SIN comisiones:** +3.16% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 77 | 49.4% | 49.6% | -0.2 pp |
| 60-79% | 54 | 74.1% | 68.1% | +5.9 pp |
| 80-94% | 24 | 87.5% | 87.5% | +0.0 pp |
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

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| sentrio | Counter-Strike: G2 vs Astralis (BO3) - E | G2 (BUY) | 67% | 5.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Pablo Llamas Ruiz vs Francisco C | Pablo Llamas Ruiz (BUY) | 69% | 5.00 | 1.0% | ⏳ pendiente | — |
| HomeRunHazard | Los Angeles Dodgers vs. Colorado Rockies | Los Angeles Dodgers (BUY) | 95% | 5.00 | 3.0% | ✅ ganada | +0.25 |
| HomeRunHazard | Spread: Pittsburgh Pirates (-1.5) | Detroit Tigers (BUY) | 60% | 5.00 | 0.2% | ⏳ pendiente | — |
| HomeRunHazard | Cancun: Pablo Llamas Ruiz vs Francisco C | Pablo Llamas Ruiz (BUY) | 54% | 5.00 | 2.4% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Cancun: Pablo Llamas Ruiz vs Francisco C | Francisco Comesana (BUY) | 46% | 5.00 | 84.9% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Marie Bouzkova vs Iva J | Marie Bouzkova (BUY) | 74% | 5.00 | 0.5% | ✅ ganada | +1.69 |
| HomeRunHazard | Spread: Los Angeles Dodgers (-2.5) | Colorado Rockies (BUY) | 71% | 5.00 | 4.2% | ✅ ganada | +1.97 |
| ferrariChampions2026 | Cancun: Gauthier Onclin vs Alejandro Mor | Alejandro Moro Canas (BUY) | 55% | 5.00 | 0.6% | ❌ perdida | -5.11 |
| sentrio | Spread: Milwaukee Brewers (-2.5) | Seattle Mariners (BUY) | 78% | 5.00 | 2.1% | ⏳ pendiente | — |
| ferrariChampions2026 | New York Liberty vs. Chicago Sky | New York Liberty (BUY) | 46% | 5.00 | 0.3% | ❌ perdida | -5.13 |
| ferrariChampions2026 | Cancun: Gauthier Onclin vs Alejandro Mor | Gauthier Onclin (BUY) | 98% | 5.00 | 0.2% | ✅ ganada | +0.10 |
| ferrariChampions2026 | Cincinnati Open: Marie Bouzkova vs Iva J | Marie Bouzkova (BUY) | 71% | 5.00 | 2.1% | ✅ ganada | +1.97 |
| ferrariChampions2026 | Will São Paulo FC vs. Club Bolívar end i | Yes (BUY) | 42% | 5.00 | 0.2% | ❌ perdida | -5.14 |
| ferrariChampions2026 | Spread: Los Angeles Dodgers (-4.5) | Colorado Rockies (BUY) | 50% | 5.00 | 0.2% | ✅ ganada | +4.88 |
| ferrariChampions2026 | Cincinnati Open: Marie Bouzkova vs Iva J | Iva Jovic (BUY) | 67% | 5.00 | 0.1% | ❌ perdida | -5.08 |
| ferrariChampions2026 | Los Angeles Angels vs. Houston Astros: O | Over (BUY) | 56% | 5.00 | 0.2% | ❌ perdida | -5.11 |
| ferrariChampions2026 | Will Independiente del Valle win on 2026 | Yes (BUY) | 68% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Los Angeles Dodgers (-1.5) | Los Angeles Dodgers (BUY) | 53% | 5.00 | 0.2% | ❌ perdida | -5.12 |
| ferrariChampions2026 | Los Angeles Dodgers vs. Colorado Rockies | Over (BUY) | 50% | 5.00 | 0.4% | ❌ perdida | -5.12 |
| ferrariChampions2026 | Spread: Los Angeles Dodgers (-1.5) | Colorado Rockies (BUY) | 48% | 5.00 | 0.9% | ✅ ganada | +5.29 |
| ferrariChampions2026 | São Paulo FC vs. Club Bolívar: O/U 2.5 | Under (BUY) | 63% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Benjamin Bonzi vs Justin Bo | Benjamin Bonzi (BUY) | 60% | 5.00 | 0.8% | ✅ ganada | +3.23 |
| ferrariChampions2026 | Cincinnati Open: Learner Tien vs Frances | Learner Tien (BUY) | 64% | 5.00 | 3.3% | ❌ perdida | -5.09 |
| ferrariChampions2026 | New York Liberty vs. Chicago Sky | Chicago Sky (BUY) | 44% | 5.00 | 0.1% | ✅ ganada | +6.22 |
| ferrariChampions2026 | LoL: Kits Esports vs 3v Team (BO5) - LRN | 3v Team (BUY) | 83% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: New York Liberty (-3.5) | New York Liberty (BUY) | 48% | 5.00 | 0.2% | ❌ perdida | -5.13 |
| ferrariChampions2026 | Los Angeles Dodgers vs. Colorado Rockies | Over (BUY) | 53% | 5.00 | 0.8% | ✅ ganada | +4.32 |
| ferrariChampions2026 | Washington Nationals vs. Texas Rangers:  | Under (BUY) | 56% | 5.00 | 0.2% | ✅ ganada | +3.82 |
| ferrariChampions2026 | Cincinnati Open: Learner Tien vs Frances | Frances Tiafoe (BUY) | 64% | 5.00 | 3.1% | ✅ ganada | +2.72 |
