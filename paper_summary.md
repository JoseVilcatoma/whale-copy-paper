# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 10:31:22 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $493.07
**Retorno acumulado:** -1.39%
**Peor caída desde un máximo (drawdown):** 10.44%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $478.25 en 96 posiciones abiertas (disponible para nuevas apuestas: $14.82)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 3 | 0 | 0 | +10.20 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| RN1 | 14 | 6 | 20 | +0.79 USD |
| sentrio | 2 | 2 | 3 | +0.78 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 0 | 0 | 4 | +0.00 USD |
| jtwyslljy | 0 | 0 | 1 | +0.00 USD |
| Lakersfan111 | 0 | 0 | 2 | +0.00 USD |
| SDTrading | 0 | 0 | 7 | +0.00 USD |
| Satisfied | 0 | 0 | 3 | +0.00 USD |
| predictionlegend | 0 | 0 | 1 | +0.00 USD |
| HomeRunHazard | 6 | 2 | 10 | -0.48 USD |
| theowalcott | 1 | 1 | 0 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 1 | -4.12 USD |
| BOOMBOYS.Kiritych | 0 | 1 | 2 | -5.14 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 0 | -5.75 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| Sassy-Bucket | 0 | 3 | 0 | -15.38 USD |
| ferrariChampions2026 | 85 | 50 | 41 | -22.50 USD |

## Análisis general

- **Apuestas resueltas:** 217
- **Aciertos:** 144 (66.4%)
- **Cuota promedio de entrada:** 65.1%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $1,085.00
- **ROI sobre lo apostado:** -0.73%
- **Comisiones pagadas (taker fee):** $18.92 (1.74% del capital apostado)
- **ROI que habría dado SIN comisiones:** +1.02% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 93 | 46.2% | 49.6% | -3.4 pp |
| 60-79% | 77 | 74.0% | 68.5% | +5.5 pp |
| 80-94% | 33 | 90.9% | 87.2% | +3.7 pp |
| 95-99% (casi seguro) | 14 | 100.0% | 97.8% | +2.2 pp |

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
| itf-ricci-panshin-2026-08-19 | RN1, ferrariChampions2026 |
| atp-durasov-poullai-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| atp-brunold-hemery-2026-08-19 | RN1, ferrariChampions2026 |
| itf-gniewko-pere-2026-08-19 | HVAB, RN1 |
| itf-paszun-zelnick-2026-08-19 | RN1, ferrariChampions2026 |
| atp-almeida-tarvet-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| atp-gombos-cuenin-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-det-pit-2026-08-19-total-8pt5 | HomeRunHazard, SDTrading |
| mlb-det-pit-2026-08-19 | HomeRunHazard, SDTrading, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-19 | Satisfied, ferrariChampions2026 |
| atp-jodar-cobolli-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| wta-swiatek-parry-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| Satisfied | Seattle Mariners vs. Milwaukee Brewers | Seattle Mariners (BUY) | 47% | 5.00 | 1.7% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Rafael Jodar vs Flavio  | Rafael Jodar (BUY) | 60% | 5.00 | 2.2% | ⏳ pendiente | — |
| RN1 | Roehampton: Matheus Pucinelli de Almeida | Oliver Tarvet (BUY) | 74% | 5.00 | 0.5% | ⏳ pendiente | — |
| predictionlegend | Club Atlético de Madrid vs. Málaga CF: O | Over (BUY) | 58% | 5.00 | 15.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: FUT Esports vs magic - M | FUT Esports (BUY) | 62% | 5.00 | 0.4% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Rafael Jodar vs Flavio  | Rafael Jodar (BUY) | 70% | 5.00 | 6.9% | ⏳ pendiente | — |
| SDTrading | Washington Nationals vs. Texas Rangers | Washington Nationals (BUY) | 46% | 3.25 | 0.7% | ⏳ pendiente | — |
| Satisfied | Atlanta Braves vs. Minnesota Twins | Minnesota Twins (BUY) | 50% | 5.00 | 217.5% | ⏳ pendiente | — |
| SDTrading | Atlanta Braves vs. Minnesota Twins | Atlanta Braves (BUY) | 52% | 5.00 | 19.9% | ⏳ pendiente | — |
| ferrariChampions2026 | ITF W35 Krakow Women: Amelia Paszun vs R | Amelia Paszun (BUY) | 53% | 5.00 | 0.6% | ⏳ pendiente | — |
| HomeRunHazard | Minnesota Lynx vs. Golden State Valkyrie | Under (BUY) | 53% | 5.00 | 5.2% | ⏳ pendiente | — |
| SDTrading | Detroit Tigers vs. Pittsburgh Pirates: O | Under (BUY) | 53% | 5.00 | 38.6% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Iga Swiatek vs Diane Pa | Iga Swiatek (BUY) | 87% | 5.00 | 9.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Iga Swiatek vs Diane Pa | Iga Swiatek (BUY) | 87% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: G2 vs Astralis - Map 2 W | G2 (BUY) | 70% | 5.00 | 2.8% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Iga Swiatek vs Diane Pa | Iga Swiatek (BUY) | 93% | 5.00 | 3.0% | ⏳ pendiente | — |
| HomeRunHazard | Detroit Tigers vs. Pittsburgh Pirates | Detroit Tigers (BUY) | 41% | 5.00 | 4.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Detroit Tigers vs. Pittsburgh Pirates | Detroit Tigers (BUY) | 41% | 5.00 | 9.2% | ⏳ pendiente | — |
| SDTrading | Arizona Diamondbacks vs. Boston Red Sox: | Over (BUY) | 47% | 5.00 | 3.2% | ⏳ pendiente | — |
| RN1 | Sion: Mika Brunold vs Calvin Hemery | Mika Brunold (BUY) | 62% | 5.00 | 2.0% | ⏳ pendiente | — |
| RN1 | Prague 2: Norbert Gombos vs Sean Cuenin | Sean Cuenin (BUY) | 60% | 5.00 | 2.2% | ⏳ pendiente | — |
| ferrariChampions2026 | ITF W35 Krakow Women: Amelia Paszun vs R | Radka Zelnickova (BUY) | 65% | 5.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Team WE vs EDward Gaming - Game 2 W | EDward Gaming (BUY) | 57% | 5.00 | 1.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Rafael Jodar vs Flavio  | Rafael Jodar (BUY) | 72% | 5.00 | 1.5% | ⏳ pendiente | — |
| RN1 | ITF W15 Logrono Women: Jordina Font vs S | Jordina Font (BUY) | 65% | 5.00 | 0.4% | ⏳ pendiente | — |
| Satisfied | New York Yankees vs. Baltimore Orioles | Baltimore Orioles (BUY) | 48% | 5.00 | 300.2% | ⏳ pendiente | — |
| ferrariChampions2026 | New York Yankees vs. Baltimore Orioles | New York Yankees (BUY) | 54% | 5.00 | 1.7% | ⏳ pendiente | — |
| SDTrading | Detroit Tigers vs. Pittsburgh Pirates | Detroit Tigers (BUY) | 41% | 5.00 | 44.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: G2 vs Astralis (BO3) - E | Astralis (BUY) | 46% | 5.00 | 5.0% | ⏳ pendiente | — |
| RN1 | ITF M25 Lesa Men: Stefano Reitano vs Fed | Federico Arnaboldi (BUY) | 58% | 5.00 | 0.7% | ⏳ pendiente | — |
