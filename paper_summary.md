# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 04:32:28 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $513.01
**Retorno acumulado:** +2.60%
**Peor caída desde un máximo (drawdown):** 8.35%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $80.00 en 16 posiciones abiertas (disponible para nuevas apuestas: $433.01)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| HomeRunHazard | 4 | 0 | 2 | +8.05 USD |
| sentrio | 2 | 1 | 4 | +5.90 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 1 | 0 | 2 | +4.68 USD |
| RN1 | 2 | 1 | 2 | +4.40 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 0 | 0 | 2 | +0.00 USD |
| jtwyslljy | 0 | 0 | 1 | +0.00 USD |
| theowalcott | 1 | 1 | 0 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 0 | -4.12 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 0 | -5.75 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| Sassy-Bucket | 0 | 3 | 0 | -15.38 USD |
| ferrariChampions2026 | 75 | 46 | 2 | -18.39 USD |

## Análisis general

- **Apuestas resueltas:** 178
- **Aciertos:** 118 (66.3%)
- **Cuota promedio de entrada:** 64.2%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $890.00
- **ROI sobre lo apostado:** +1.47%
- **Comisiones pagadas (taker fee):** $15.94 (1.79% del capital apostado)
- **ROI que habría dado SIN comisiones:** +3.26% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 83 | 49.4% | 49.7% | -0.3 pp |
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
| lol-al-tes-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, jtwyslljy |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | ITF M15 Arad Men: Jacopo Bilardo vs Jere | Jeremy Gschwendtner (BUY) | 42% | 5.00 | 11.5% | ⏳ pendiente | — |
| RN1 | Sion: Luca Staeheli vs Juan Manuel La Se | Juan Manuel La Serna (BUY) | 66% | 5.00 | 11.8% | ✅ ganada | +2.49 |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | LoL: Gen.G vs KT Rolster - Game 1 Winner | Gen.G (BUY) | 85% | 5.00 | 33.1% | ⏳ pendiente | — |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | LoL: Anyone's Legend vs Top Esports (BO3 | Anyone's Legend (BUY) | 59% | 5.00 | 5.1% | ⏳ pendiente | — |
| jtwyslljy | LoL: Anyone's Legend vs Top Esports (BO3 | Anyone's Legend (BUY) | 59% | 5.00 | 324.1% | ⏳ pendiente | — |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | Will Celtic FC win on 2026-08-19? | No (BUY) | 45% | 5.00 | 2.9% | ⏳ pendiente | — |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | LoL: Hanwha Life Esports Challengers vs  | BNK FearX Youth (BUY) | 51% | 5.00 | 37.0% | ✅ ganada | +4.68 |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | LoL: KT Rolster Challengers vs T1 Academ | KT Rolster Challengers (BUY) | 51% | 5.00 | 9.2% | ⏳ pendiente | — |
| sentrio | ITF M25 Idanha-a-Nova 2 Men: Abdulhamid  | Tiago Boschmans (BUY) | 54% | 5.00 | 2.0% | ⏳ pendiente | — |
| RN1 | Will AL Ahly SC (EGY) win on 2026-08-19? | No (BUY) | 97% | 5.00 | 2.9% | ⏳ pendiente | — |
| sentrio | Seattle Mariners vs. Milwaukee Brewers:  | Over (BUY) | 45% | 5.00 | 1.5% | ⏳ pendiente | — |
| HomeRunHazard | Nippon Ham Fighters vs. Fukuoka SoftBank | Fukuoka SoftBank Hawks (BUY) | 53% | 5.00 | 0.5% | ⏳ pendiente | — |
| sentrio | Counter-Strike: G2 vs Astralis (BO3) - E | G2 (BUY) | 67% | 5.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Pablo Llamas Ruiz vs Francisco C | Pablo Llamas Ruiz (BUY) | 69% | 5.00 | 1.0% | ✅ ganada | +2.17 |
| HomeRunHazard | Los Angeles Dodgers vs. Colorado Rockies | Los Angeles Dodgers (BUY) | 95% | 5.00 | 3.0% | ✅ ganada | +0.25 |
| HomeRunHazard | Spread: Pittsburgh Pirates (-1.5) | Detroit Tigers (BUY) | 60% | 5.00 | 0.2% | ⏳ pendiente | — |
| HomeRunHazard | Cancun: Pablo Llamas Ruiz vs Francisco C | Pablo Llamas Ruiz (BUY) | 54% | 5.00 | 2.4% | ✅ ganada | +4.14 |
| danielwolfmorales3pddb6dl6 | Cancun: Pablo Llamas Ruiz vs Francisco C | Francisco Comesana (BUY) | 46% | 5.00 | 84.9% | ❌ perdida | -5.13 |
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
| ferrariChampions2026 | Will Independiente del Valle win on 2026 | Yes (BUY) | 68% | 5.00 | 0.3% | ✅ ganada | +2.27 |
