# Paper trading — resultado de la simulación

Actualizado: 2026-08-18 20:43:53 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $536.69
**Retorno acumulado:** +7.34%
**Peor caída desde un máximo (drawdown):** 4.67%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $265.00 en 53 posiciones abiertas (disponible para nuevas apuestas: $271.69)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| theowalcott | 1 | 0 | 1 | +3.66 USD |
| RN1 | 1 | 1 | 0 | +1.91 USD |
| sentrio | 1 | 1 | 1 | +0.39 USD |
| ferrariChampions2026 | 45 | 22 | 43 | +0.35 USD |
| Sassy-Bucket | 0 | 0 | 3 | +0.00 USD |
| danielwolfmorales3pddb6dl6 | 0 | 0 | 2 | +0.00 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 1 | 2 | 2 | -4.74 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |

## Análisis general

- **Apuestas resueltas:** 108
- **Aciertos:** 79 (73.1%)
- **Cuota promedio de entrada:** 68.6%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $540.00
- **ROI sobre lo apostado:** +6.80%
- **Comisiones pagadas (taker fee):** $8.50 (1.57% del capital apostado)
- **ROI que habría dado SIN comisiones:** +8.37% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 40 | 55.0% | 49.4% | +5.7 pp |
| 60-79% | 34 | 76.5% | 69.1% | +7.4 pp |
| 80-94% | 24 | 87.5% | 87.5% | +0.0 pp |
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
| atp-tien-tiafoe-2026-08-18 | ferrariChampions2026, sentrio |
| mlb-tor-tb-2026-08-18 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, ferrariChampions2026 |
| atp-svrcina-wawrink-2026-08-18 | danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| mlb-wsh-tex-2026-08-18-total-8pt5 | Sassy-Bucket, ferrariChampions2026 |
| mlb-lad-col-2026-08-18-total-11pt5 | Sassy-Bucket, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | São Paulo FC vs. Club Bolívar: O/U 2.5 | Under (BUY) | 63% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Benjamin Bonzi vs Justin Bo | Benjamin Bonzi (BUY) | 60% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Learner Tien vs Frances | Learner Tien (BUY) | 64% | 5.00 | 3.3% | ⏳ pendiente | — |
| ferrariChampions2026 | New York Liberty vs. Chicago Sky | Chicago Sky (BUY) | 44% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Kits Esports vs 3v Team (BO5) - LRN | 3v Team (BUY) | 83% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: New York Liberty (-3.5) | New York Liberty (BUY) | 48% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Los Angeles Dodgers vs. Colorado Rockies | Over (BUY) | 53% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Washington Nationals vs. Texas Rangers:  | Under (BUY) | 56% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Learner Tien vs Frances | Frances Tiafoe (BUY) | 64% | 5.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Los Angeles Angels vs. Houston Astros | Los Angeles Angels (BUY) | 65% | 5.00 | 2.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Atlanta Dream vs. Las Vegas Aces | Las Vegas Aces (BUY) | 66% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Chicago White Sox vs. Chicago Cubs | Chicago White Sox (BUY) | 49% | 5.00 | 0.2% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Cincinnati Open: Marie Bouzkova vs Iva J | Iva Jovic (BUY) | 53% | 5.00 | 34.6% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Cancun: Dalibor Svrcina vs Stan Wawrinka | Stan Wawrinka (BUY) | 52% | 5.00 | 29.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Atlanta Dream vs. Las Vegas Aces: O/U 17 | Over (BUY) | 52% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Atlanta Dream vs. Las Vegas Aces | Atlanta Dream (BUY) | 45% | 5.00 | 0.5% | ⏳ pendiente | — |
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
| ferrariChampions2026 | Atlanta Braves vs. Minnesota Twins | Minnesota Twins (BUY) | 65% | 5.00 | 8.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Indiana Fever vs. Toronto Tempo: O/U 191 | Over (BUY) | 51% | 5.00 | 0.1% | ✅ ganada | +4.68 |
| ferrariChampions2026 | Spread: Milwaukee Brewers (-2.5) | Seattle Mariners (BUY) | 67% | 5.00 | 2.8% | ⏳ pendiente | — |
