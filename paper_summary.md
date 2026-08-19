# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 11:27:30 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $490.39
**Retorno acumulado:** -1.92%
**Peor caída desde un máximo (drawdown):** 10.57%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $463.25 en 93 posiciones abiertas (disponible para nuevas apuestas: $27.14)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 3 | 0 | 0 | +10.20 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| sentrio | 2 | 2 | 3 | +0.78 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 0 | 0 | 5 | +0.00 USD |
| jtwyslljy | 0 | 0 | 1 | +0.00 USD |
| Lakersfan111 | 0 | 0 | 2 | +0.00 USD |
| SDTrading | 0 | 0 | 7 | +0.00 USD |
| Satisfied | 0 | 0 | 3 | +0.00 USD |
| predictionlegend | 0 | 0 | 1 | +0.00 USD |
| ChonkyChocolateCake | 0 | 0 | 2 | +0.00 USD |
| ic4cream | 0 | 0 | 1 | +0.00 USD |
| HomeRunHazard | 7 | 2 | 12 | -0.33 USD |
| BOOMBOYS.Kiritych | 1 | 1 | 1 | -1.16 USD |
| theowalcott | 1 | 1 | 0 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 1 | -4.12 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 0 | -5.75 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| RN1 | 20 | 10 | 15 | -7.03 USD |
| Sassy-Bucket | 0 | 3 | 0 | -15.38 USD |
| ferrariChampions2026 | 90 | 52 | 38 | -21.50 USD |

## Análisis general

- **Apuestas resueltas:** 236
- **Aciertos:** 157 (66.5%)
- **Cuota promedio de entrada:** 65.4%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $1,180.00
- **ROI sobre lo apostado:** -0.90%
- **Comisiones pagadas (taker fee):** $20.41 (1.73% del capital apostado)
- **ROI que habría dado SIN comisiones:** +0.83% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 99 | 46.5% | 49.8% | -3.4 pp |
| 60-79% | 85 | 74.1% | 68.3% | +5.8 pp |
| 80-94% | 36 | 88.9% | 87.1% | +1.8 pp |
| 95-99% (casi seguro) | 16 | 100.0% | 97.6% | +2.4 pp |

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
| lal-mad-mala-2026-08-19-mad | ic4cream, swisstony |
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
| cs2-g2-ast10-2026-08-19 | BOOMBOYS.Kiritych, ferrariChampions2026, sentrio |
| lol-al-tes-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, ferrariChampions2026, jtwyslljy |
| atp-maxted-brady-2026-08-19 | RN1, ferrariChampions2026 |
| lol-we-edg-2026-08-19-game-handicap-away-1pt5 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, Lakersfan111 |
| atp-giustin-bernet-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-mia-phi-2026-08-19-total-8pt5 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, HomeRunHazard |
| atp-molleke-jianu-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-atl-min-2026-08-19 | SDTrading, Satisfied, ferrariChampions2026 |
| chi-shp-ygb-2026-07-12-ygb | RN1, ferrariChampions2026 |
| atp-geerts-albot-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-mia-phi-2026-08-19 | SDTrading, ferrariChampions2026 |
| cs2-fut-mgc-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, ferrariChampions2026 |
| atp-papoe-cosano-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| atp-ceban-radulov-2026-08-19 | HomeRunHazard, RN1 |
| itf-ricci-panshin-2026-08-19 | RN1, ferrariChampions2026 |
| atp-durasov-poullai-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| atp-brunold-hemery-2026-08-19 | RN1, ferrariChampions2026 |
| itf-gniewko-pere-2026-08-19 | HVAB, RN1 |
| itf-paszun-zelnick-2026-08-19 | RN1, ferrariChampions2026 |
| atp-almeida-tarvet-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| atp-gombos-cuenin-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-det-pit-2026-08-19-total-8pt5 | HomeRunHazard, SDTrading |
| mlb-det-pit-2026-08-19 | HomeRunHazard, SDTrading, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-19 | Satisfied, ferrariChampions2026 |
| atp-jodar-cobolli-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| wta-swiatek-parry-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| atp-kopp-hassan-2026-08-19 | RN1, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ic4cream | Will Club Atlético de Madrid win on 2026 | Yes (BUY) | 73% | 5.00 | 3.8% | ⏳ pendiente | — |
| RN1 | Sion: Sandro Kopp vs Benjamin Hassan | Sandro Kopp (BUY) | 69% | 5.00 | 2.2% | ⏳ pendiente | — |
| RN1 | ITF W35 Krakow Women: Marcelina Podlinsk | Dalila Jakupovic (BUY) | 91% | 5.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: BIG vs Unicorns Of Love Sexy Editio | Unicorns Of Love Sexy Edition (BUY) | 50% | 5.00 | 0.1% | ⏳ pendiente | — |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | Will Inter Miami CF win on 2026-08-19? | No (BUY) | 65% | 5.00 | 6.2% | ⏳ pendiente | — |
| HomeRunHazard | Roehampton: Mark Ceban vs Iliyan Radulov | Mark Ceban (BUY) | 96% | 5.00 | 4.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: Black Phoenix vs Bushido | Black Phoenix (BUY) | 85% | 5.00 | 0.5% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Boston Red Sox (-1.5) | Arizona Diamondbacks (BUY) | 59% | 5.00 | 4.1% | ⏳ pendiente | — |
| ChonkyChocolateCake | LoL: Vitality.Bee vs Ici Japon Corp. Esp | Ici Japon Corp. Esport (BUY) | 51% | 5.00 | 5.6% | ⏳ pendiente | — |
| ChonkyChocolateCake | LoL: UCAM Esports Club vs Team Heretics  | UCAM Esports Club (BUY) | 51% | 5.00 | 11.5% | ⏳ pendiente | — |
| RN1 | Prague 2: Norbert Gombos vs Sean Cuenin | Norbert Gombos (BUY) | 78% | 5.00 | 1.8% | ⏳ pendiente | — |
| RN1 | ITF M25 Santander Men: Bernardo Munk Mes | Sergi Perez Contri (BUY) | 75% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | ITF M25 Ueberlingen Men: Moritz Hoffmann | Christian Djonov (BUY) | 51% | 5.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: UCAM Esports Club vs Team Heretics  | Team Heretics Academy (BUY) | 66% | 5.00 | 0.2% | ⏳ pendiente | — |
| HomeRunHazard | Prague 2: Norbert Gombos vs Sean Cuenin | Sean Cuenin (BUY) | 62% | 5.00 | 1.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Sion: Sandro Kopp vs Benjamin Hassan | Sandro Kopp (BUY) | 53% | 5.00 | 0.1% | ⏳ pendiente | — |
| Satisfied | Seattle Mariners vs. Milwaukee Brewers | Seattle Mariners (BUY) | 47% | 5.00 | 1.7% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Rafael Jodar vs Flavio  | Rafael Jodar (BUY) | 60% | 5.00 | 7.6% | ⏳ pendiente | — |
| RN1 | Roehampton: Matheus Pucinelli de Almeida | Oliver Tarvet (BUY) | 74% | 5.00 | 2.3% | ⏳ pendiente | — |
| predictionlegend | Club Atlético de Madrid vs. Málaga CF: O | Over (BUY) | 58% | 5.00 | 15.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: FUT Esports vs magic - M | FUT Esports (BUY) | 62% | 5.00 | 0.4% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Rafael Jodar vs Flavio  | Rafael Jodar (BUY) | 70% | 5.00 | 9.7% | ⏳ pendiente | — |
| SDTrading | Washington Nationals vs. Texas Rangers | Washington Nationals (BUY) | 46% | 3.25 | 0.7% | ⏳ pendiente | — |
| Satisfied | Atlanta Braves vs. Minnesota Twins | Minnesota Twins (BUY) | 50% | 5.00 | 217.5% | ⏳ pendiente | — |
| SDTrading | Atlanta Braves vs. Minnesota Twins | Atlanta Braves (BUY) | 52% | 5.00 | 19.9% | ⏳ pendiente | — |
| ferrariChampions2026 | ITF W35 Krakow Women: Amelia Paszun vs R | Amelia Paszun (BUY) | 53% | 5.00 | 0.6% | ⏳ pendiente | — |
| HomeRunHazard | Minnesota Lynx vs. Golden State Valkyrie | Under (BUY) | 53% | 5.00 | 6.8% | ⏳ pendiente | — |
| SDTrading | Detroit Tigers vs. Pittsburgh Pirates: O | Under (BUY) | 53% | 5.00 | 38.6% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Iga Swiatek vs Diane Pa | Iga Swiatek (BUY) | 87% | 5.00 | 18.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Iga Swiatek vs Diane Pa | Iga Swiatek (BUY) | 87% | 5.00 | 0.2% | ⏳ pendiente | — |
