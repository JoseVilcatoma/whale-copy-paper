# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 19:22:26 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $457.36
**Retorno acumulado:** -8.53%
**Peor caída desde un máximo (drawdown):** 25.62%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $457.08 en 92 posiciones abiertas (disponible para nuevas apuestas: $0.28)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| SDTrading | 3 | 2 | 6 | +6.04 USD |
| Lakersfan111 | 1 | 0 | 1 | +5.29 USD |
| Satisfied | 1 | 0 | 2 | +4.88 USD |
| sentrio | 3 | 2 | 2 | +3.16 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| BOOMBOYS.Kiritych | 2 | 1 | 0 | +1.22 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| dauntlesswitness | 0 | 0 | 1 | +0.00 USD |
| ChonkyChocolateCake | 1 | 1 | 0 | -0.44 USD |
| predictionlegend | 2 | 2 | 0 | -0.46 USD |
| theowalcott | 1 | 1 | 7 | -1.43 USD |
|  | 3 | 2 | 0 | -3.59 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 1 | -4.12 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 2 | -5.75 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 3 | 3 | 1 | -6.79 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| Sassy-Bucket | 1 | 3 | 3 | -9.87 USD |
| RN1 | 68 | 35 | 5 | -18.39 USD |
| HomeRunHazard | 22 | 12 | 18 | -18.85 USD |
| ferrariChampions2026 | 121 | 73 | 43 | -41.10 USD |

## Análisis general

- **Apuestas resueltas:** 417
- **Aciertos:** 271 (65.0%)
- **Cuota promedio de entrada:** 65.1%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $2,083.37
- **ROI sobre lo apostado:** -2.10%
- **Comisiones pagadas (taker fee):** $36.32 (1.74% del capital apostado)
- **ROI que habría dado SIN comisiones:** -0.35% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 186 | 47.8% | 50.3% | -2.4 pp |
| 60-79% | 138 | 71.0% | 68.1% | +2.9 pp |
| 80-94% | 63 | 85.7% | 87.3% | -1.6 pp |
| 95-99% (casi seguro) | 30 | 100.0% | 97.2% | +2.8 pp |

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
| lal-mad-mala-2026-08-19-mad | RN1, ferrariChampions2026, ic4cream, swisstony |
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
| ucl-cel-lin2-2026-08-19-cel | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, RN1 |
| lol-al-tes-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, ferrariChampions2026, jtwyslljy |
| atp-maxted-brady-2026-08-19 | RN1, ferrariChampions2026 |
| lol-we-edg-2026-08-19-game-handicap-away-1pt5 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, Lakersfan111 |
| atp-giustin-bernet-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-mia-phi-2026-08-19-total-8pt5 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, HomeRunHazard, ferrariChampions2026 |
| atp-molleke-jianu-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-ari-bos-2026-08-19 | , RN1, ferrariChampions2026 |
| mlb-atl-min-2026-08-19 | , RN1, SDTrading, Satisfied, ferrariChampions2026 |
| chi-shp-ygb-2026-07-12-ygb | RN1, ferrariChampions2026 |
| atp-geerts-albot-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-mia-phi-2026-08-19 | HomeRunHazard, SDTrading, ferrariChampions2026 |
| cs2-fut-mgc-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, ferrariChampions2026 |
| atp-papoe-cosano-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| atp-ceban-radulov-2026-08-19 | HomeRunHazard, RN1 |
| itf-ricci-panshin-2026-08-19 | RN1, ferrariChampions2026 |
| atp-durasov-poullai-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| atp-brunold-hemery-2026-08-19 | RN1, ferrariChampions2026 |
| itf-gniewko-pere-2026-08-19 | HVAB, RN1 |
| itf-paszun-zelnick-2026-08-19 | RN1, ferrariChampions2026 |
| atp-almeida-tarvet-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-cws-chc-2026-08-19 | RN1, SDTrading |
| atp-gombos-cuenin-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-det-pit-2026-08-19-total-8pt5 | HomeRunHazard, RN1, SDTrading |
| mlb-stl-cin-2026-08-19 | HomeRunHazard, ferrariChampions2026 |
| mlb-det-pit-2026-08-19 | HomeRunHazard, RN1, SDTrading, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-19 | HomeRunHazard, Satisfied, ferrariChampions2026 |
| atp-jodar-cobolli-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-ari-bos-2026-08-19-total-8pt5 | HomeRunHazard, SDTrading, ferrariChampions2026 |
| wta-swiatek-parry-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| lal-mad-mala-2026-08-19-total-2pt5 | RN1, predictionlegend |
| mlb-sea-mil-2026-08-19 | SDTrading, Satisfied |
| atp-kopp-hassan-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-ari-bos-2026-08-19-spread-home-1pt5 | HomeRunHazard, ferrariChampions2026 |
| mls-phi-mia-2026-08-19-mia | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, RN1, ferrariChampions2026 |
| lol-big1-use1-2026-08-19 | , ferrariChampions2026 |
| mlb-det-pit-2026-08-19-total-7pt5 | HomeRunHazard, RN1 |
| wta-cirstea-pegula-2026-08-19 | HomeRunHazard, RN1 |
| mlb-sd-nym-2026-08-19 | HomeRunHazard, RN1 |
| wta-kostyuk-andreev-2026-08-19 | HomeRunHazard, RN1 |
| atp-tirante-mensik-2026-08-19 | HomeRunHazard, RN1 |
| lal-mad-mala-2026-08-19-spread-home-1pt5 | RN1, predictionlegend |
| ucl-sba-cel1-2026-08-19-sba | RN1, predictionlegend |
| atp-zverev-paul-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| wta-noskova-anisimo-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, RN1, ferrariChampions2026 |
| lal-mad-mala-2026-08-19-total-1pt5 | RN1, ferrariChampions2026 |
| atp-fils-minaur-2026-08-19 | , RN1, ferrariChampions2026 |
| sud-cam-bra-2026-08-19-cam | RN1, theowalcott |
| atp-virtane-echargu-2026-08-18 | HomeRunHazard, ferrariChampions2026 |
| mlb-ari-bos-2026-08-19-total-9pt5 | RN1, ferrariChampions2026 |
| wta-shnaide-rybakin-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-tor-tb-2026-08-19-total-7pt5 | HomeRunHazard, Sassy-Bucket, ferrariChampions2026 |
| mlb-sf-cle-2026-08-19-spread-home-1pt5 | HomeRunHazard, SDTrading, ferrariChampions2026 |
| mls-fcc-nyc-2026-08-19-fcc | ferrariChampions2026, theowalcott |
| atp-jacquet-vukic-2026-08-18 | HomeRunHazard, ferrariChampions2026 |
| atp-borges-nakashi-2026-08-19 | HomeRunHazard, ferrariChampions2026 |
| mls-clb-mim-2026-08-19-clb | ferrariChampions2026, theowalcott |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | Valorant: G2 Esports vs M80 (BO3) - VCT  | G2 Esports (BUY) | 65% | 5.00 | 1.1% | ⏳ pendiente | — |
| Sassy-Bucket | Los Angeles Dodgers vs. Colorado Rockies | Under (BUY) | 53% | 5.00 | 19.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Madison Keys vs Xiyu Wa | Madison Keys (BUY) | 74% | 4.47 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Inter Miami CF win on 2026-08-19? | No (BUY) | 65% | 5.00 | 0.4% | ⏳ pendiente | — |
| dauntlesswitness | Counter-Strike: Team Falcons vs TheMongo | Team Falcons (BUY) | 81% | 5.00 | 9.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Columbus Crew vs. CF Montréal: O/U 4.5 | Under (BUY) | 73% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: G2 Esports vs M80 - Map 1 Winn | M80 (BUY) | 52% | 5.00 | 1.6% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | LoL: Nongshim Red Force vs Kiwoom DRX (B | Kiwoom DRX (BUY) | 42% | 5.00 | 6.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Alexis Galarneau vs Dino Pr | Alexis Galarneau (BUY) | 56% | 5.00 | 0.2% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | LoL: Dplus KIA Challengers vs DN SOOPers | DN SOOPers Challengers (BUY) | 43% | 5.00 | 25.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Toronto FC vs. Charlotte FC: O/U 1.5 | Over (BUY) | 96% | 5.00 | 0.2% | ⏳ pendiente | — |
| theowalcott | Montevideo City Torque vs. CA Tigre: O/U | Over (BUY) | 63% | 5.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Nuno Borges vs Brandon  | Brandon Nakashima (BUY) | 79% | 5.00 | 1.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Set 1 Winner: Keys vs Wang | Wang (BUY) | 55% | 4.36 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: G2 Esports vs M80 - Map 1 Winn | G2 Esports (BUY) | 69% | 5.00 | 3.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Will FC Cincinnati win on 2026-08-19? | No (BUY) | 49% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | San Francisco Giants vs. Cleveland Guard | San Francisco Giants (BUY) | 43% | 5.00 | 1.9% | ⏳ pendiente | — |
| HomeRunHazard | St. Louis Cardinals vs. Cincinnati Reds | Cincinnati Reds (BUY) | 55% | 5.00 | 2.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Will CD Coquimbo Unido win on 2026-08-19 | No (BUY) | 66% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Rodrigo Pacheco vs Tomas Barrios | Rodrigo Pacheco (BUY) | 68% | 5.00 | 2.8% | ⏳ pendiente | — |
| HomeRunHazard | New York Yankees vs. Baltimore Orioles | New York Yankees (BUY) | 57% | 5.00 | 3.1% | ⏳ pendiente | — |
| HomeRunHazard | Quebec City: Soon-Woo Kwon vs Shintaro M | Soon-Woo Kwon (BUY) | 88% | 5.00 | 1.7% | ⏳ pendiente | — |
| HomeRunHazard | Cancun: Otto Virtanen vs Moez Echargui | Moez Echargui (BUY) | 56% | 5.00 | 1.3% | ✅ ganada | +3.82 |
| ferrariChampions2026 | Miami Marlins vs. Philadelphia Phillies | Philadelphia Phillies (BUY) | 89% | 5.00 | 0.1% | ⏳ pendiente | — |
| Sassy-Bucket | Athletics vs. Kansas City Royals: O/U 8. | Over (BUY) | 53% | 5.00 | 8.1% | ⏳ pendiente | — |
| theowalcott | Orlando City SC vs. Chicago Fire FC: O/U | Under (BUY) | 53% | 5.00 | 13.3% | ⏳ pendiente | — |
| theowalcott | Will Columbus Crew win on 2026-08-19? | Yes (BUY) | 59% | 5.00 | 20.9% | ⏳ pendiente | — |
| ferrariChampions2026 | CD Coquimbo Unido vs. CA Platense: O/U 2 | Under (BUY) | 93% | 5.00 | 0.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Cleveland Guardians (-1.5) | San Francisco Giants (BUY) | 50% | 5.00 | 1.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Cleveland Guardians (-2.5) | San Francisco Giants (BUY) | 62% | 5.00 | 1.1% | ⏳ pendiente | — |
