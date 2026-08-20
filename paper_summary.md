# Paper trading — resultado de la simulación

Actualizado: 2026-08-20 14:45:02 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $512.09
**Retorno acumulado:** +2.42%
**Peor caída desde un máximo (drawdown):** 25.62%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $165.00 en 33 posiciones abiertas (disponible para nuevas apuestas: $347.09)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| Lakersfan111 | 3 | 0 | 1 | +16.77 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| IMAREALPERSON | 12 | 1 | 1 | +12.78 USD |
| sentrio | 5 | 2 | 0 | +10.49 USD |
| casualbet2020 | 2 | 0 | 1 | +7.37 USD |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | 3 | 1 | 1 | +7.07 USD |
| SDTrading | 8 | 6 | 2 | +5.37 USD |
| Satisfied | 2 | 1 | 0 | +5.26 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 5 | 3 | 0 | +2.04 USD |
| sulumos | 1 | 0 | 0 | +1.96 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| BOOMBOYS.Kiritych | 2 | 1 | 0 | +1.22 USD |
| dauntlesswitness | 1 | 0 | 0 | +1.13 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 3 | 0 | +0.56 USD |
| CORGI8 | 0 | 0 | 3 | +0.00 USD |
| theowalcott | 5 | 4 | 0 | -0.44 USD |
| predictionlegend | 2 | 2 | 2 | -0.46 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 1 | 2 | 0 | -5.33 USD |
| ChonkyChocolateCake | 1 | 2 | 4 | -5.54 USD |
| ferrariChampions2026 | 166 | 95 | 2 | -6.06 USD |
| Sassy-Bucket | 3 | 4 | 3 | -6.36 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| danielwolfmorales3pddb6dl6 | 6 | 7 | 4 | -9.93 USD |
| SineNooneEI | 0 | 2 | 0 | -10.26 USD |
|  | 11 | 7 | 8 | -12.06 USD |
| HomeRunHazard | 36 | 20 | 0 | -12.70 USD |
| RN1 | 105 | 50 | 1 | -38.22 USD |

## Análisis general

- **Apuestas resueltas:** 624
- **Aciertos:** 407 (65.2%)
- **Cuota promedio de entrada:** 64.1%
- **Stake promedio:** $4.99
- **Total apostado (suma de stakes):** $3,115.45
- **ROI sobre lo apostado:** -0.31%
- **Comisiones pagadas (taker fee):** $55.86 (1.79% del capital apostado)
- **ROI que habría dado SIN comisiones:** +1.48% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 295 | 48.1% | 50.2% | -2.0 pp |
| 60-79% | 204 | 74.5% | 68.1% | +6.4 pp |
| 80-94% | 80 | 86.2% | 86.9% | -0.6 pp |
| 95-99% (casi seguro) | 45 | 97.8% | 97.3% | +0.5 pp |

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
| dota2-ironwi-ts8-2026-08-19 | , Lakersfan111 |
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
| mlb-nyy-bal-2026-08-19 | HomeRunHazard, RN1, Satisfied, ferrariChampions2026 |
| atp-jodar-cobolli-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-ari-bos-2026-08-19-total-8pt5 | HomeRunHazard, SDTrading, ferrariChampions2026 |
| wta-swiatek-parry-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-wsh-tex-2026-08-19 | RN1, SDTrading |
| lal-mad-mala-2026-08-19-total-2pt5 | RN1, predictionlegend |
| mlb-sea-mil-2026-08-19 | RN1, SDTrading, Satisfied |
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
| mlb-lad-col-2026-08-19 | RN1, ferrariChampions2026 |
| lol-lgd-blg-2026-08-20-game-handicap-home-1pt5 | Lakersfan111, danielwolfmorales3pddb6dl6 |
| wta-sabalen-bejlek-2026-08-19 | , 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653, RN1 |
| dota2-ironwi-ts8-2026-08-19-game2 | , ferrariChampions2026 |
| dota2-vsn2-boombo-2026-08-20-game1 | , ferrariChampions2026 |
| wta-anisimo-pegula-2026-08-21 | 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653, CORGI8, danielwolfmorales3pddb6dl6 |
| dota2-vsn2-boombo-2026-08-20 | , ferrariChampions2026 |
| atp-compagn-serna-2026-08-20 | 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653, RN1, danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| dota2-vsn2-boombo-2026-08-20-game2 | IMAREALPERSON, ferrariChampions2026 |
| lol-dk-hle1-2026-08-20-game1 | SineNooneEI, danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| lol-dk-hle1-2026-08-20-game2 | danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| itf-poljica-dominko-2026-08-20 | , RN1 |
| dota2-liquid-ty-2026-08-20 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, IMAREALPERSON, ferrariChampions2026 |
| itf-kotliar-lovric-2026-08-20 | RN1, ferrariChampions2026 |
| atp-tarvet-broom-2026-08-20 | RN1, ferrariChampions2026 |
| dota2-liquid-ty-2026-08-20-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON, ferrariChampions2026 |
| atp-hassan-blancan-2026-08-20 | RN1, danielwolfmorales3pddb6dl6 |
| atp-giustin-kuzmano-2026-08-20 | RN1, danielwolfmorales3pddb6dl6 |
| lol-lgd-blg-2026-08-20 | danielwolfmorales3pddb6dl6, sulumos |
| cs2-g2-furia-2026-08-20 | CORGI8, casualbet2020 |
| cs2-faze-vit-2026-08-20-game2 | , casualbet2020 |
| mlb-oak-kc-2026-08-20-total-8pt5 | SDTrading, Sassy-Bucket |
| dota2-ngx-flc-2026-08-20 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, ChonkyChocolateCake, IMAREALPERSON |
| lol-koia-hrts-2026-08-20 | ChonkyChocolateCake, danielwolfmorales3pddb6dl6 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| Lakersfan111 | Dota 2: Iron Wing vs BoomBoys (BO3) - Th | Iron Wing (BUY) | 46% | 5.00 | 31.6% | ⏳ pendiente | — |
| ChonkyChocolateCake | LoL: ⁠Movistar KOI Fénix vs Team Heretic | ⁠Movistar KOI Fénix (BUY) | 55% | 5.00 | 21.5% | ⏳ pendiente | — |
| Sassy-Bucket | Athletics vs. Kansas City Royals: O/U 8. | Over (BUY) | 48% | 5.00 | 0.3% | ⏳ pendiente | — |
| SDTrading | Seattle Mariners vs. Milwaukee Brewers:  | Over (BUY) | 54% | 5.00 | 17.9% | ✅ ganada | +4.14 |
| IMAREALPERSON | Valorant: Team Liquid vs FUT Esports (BO | FUT Esports (BUY) | 44% | 5.00 | 2.5% | ⏳ pendiente | — |
| predictionlegend | Will Rayo Vallecano de Madrid win on 202 | No (BUY) | 61% | 5.00 | 124.3% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | LoL: ⁠Movistar KOI Fénix vs Team Heretic | Team Heretics Academy (BUY) | 47% | 5.00 | 11.2% | ⏳ pendiente | — |
| IMAREALPERSON | Dota 2: Nigma Galaxy vs Team Falcons (BO | Nigma Galaxy (BUY) | 49% | 5.00 | 21.1% | ✅ ganada | +5.08 |
| CORGI8 | Counter-Strike: G2 vs FURIA - Map 2 Winn | G2 (BUY) | 41% | 5.00 | 9.7% | ⏳ pendiente | — |
| CORGI8 | Cincinnati Open: Amanda Anisimova vs Jes | Amanda Anisimova (BUY) | 46% | 5.00 | 35.7% | ⏳ pendiente | — |
| IMAREALPERSON | Dota 2: Nigma Galaxy vs Team Falcons (BO | Nigma Galaxy (BUY) | 43% | 5.00 | 56.5% | 💰 vendida anticipada | +0.18 |
| ChonkyChocolateCake | LoL: Karmine Corp Blue vs Ici Japon Corp | Karmine Corp Blue (BUY) | 67% | 5.00 | 3.2% | ⏳ pendiente | — |
| predictionlegend | K. Sint-Truidense VV vs. AS Omónoia Leuk | Over (BUY) | 44% | 5.00 | 67.1% | ⏳ pendiente | — |
| IMAREALPERSON | Dota 2: Nigma Galaxy vs Team Falcons (BO | Nigma Galaxy (BUY) | 47% | 5.00 | 60.8% | 💰 vendida anticipada | +0.37 |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | Dota 2: Nigma Galaxy vs Team Falcons (BO | Team Falcons (BUY) | 59% | 5.00 | 67.2% | ❌ perdida | -5.10 |
| ChonkyChocolateCake | Dota 2: Nigma Galaxy vs Team Falcons (BO | Team Falcons (BUY) | 59% | 5.00 | 32.6% | ❌ perdida | -5.10 |
| ChonkyChocolateCake | LoL: G2 NORD vs Eintracht Spandau - Game | G2 NORD (BUY) | 61% | 5.00 | 31.0% | ⏳ pendiente | — |
| Sassy-Bucket | San Francisco Giants vs. Cleveland Guard | Over (BUY) | 57% | 5.00 | 86.0% | ⏳ pendiente | — |
| CORGI8 | Counter-Strike: G2 vs FURIA (BO3) - Espo | G2 (BUY) | 45% | 5.00 | 163.0% | ⏳ pendiente | — |
| Sassy-Bucket | San Francisco Giants vs. Cleveland Guard | Over (BUY) | 44% | 5.00 | 216.9% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Roehampton: Michael Geerts vs Lucas Poul | Michael Geerts (BUY) | 48% | 5.00 | 18.7% | ❌ perdida | -5.13 |
| danielwolfmorales3pddb6dl6 | Cincinnati Open: Amanda Anisimova vs Jes | Amanda Anisimova (BUY) | 47% | 5.00 | 73.9% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Cincinnati Open: Iga Swiatek vs Elena Ry | Iga Swiatek (BUY) | 59% | 5.00 | 78.0% | ⏳ pendiente | — |
| SDTrading | Athletics vs. Kansas City Royals: O/U 8. | Over (BUY) | 48% | 5.00 | 0.6% | ⏳ pendiente | — |
| SDTrading | Athletics vs. Kansas City Royals | Athletics (BUY) | 45% | 5.00 | 0.7% | ⏳ pendiente | — |
| IMAREALPERSON | Dota 2: Nigma Galaxy vs Team Falcons - G | Nigma Galaxy (BUY) | 74% | 5.00 | 30.2% | 💰 vendida anticipada | +0.08 |
| ChonkyChocolateCake | LoL: G2 NORD vs Eintracht Spandau - Game | G2 NORD (BUY) | 57% | 5.00 | 8.5% | ⏳ pendiente | — |
|  | Will FC København win on 2026-08-20? | Yes (BUY) | 63% | 5.00 | 7.4% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Cincinnati Open: Tommy Paul vs Flavio Co | Tommy Paul (BUY) | 61% | 5.00 | 130.7% | ⏳ pendiente | — |
|  | PAOK vs. SK Brann: O/U 2.5 | Under (BUY) | 51% | 5.00 | 0.9% | ⏳ pendiente | — |
