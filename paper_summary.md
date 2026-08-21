# Paper trading — resultado de la simulación

Actualizado: 2026-08-21 08:18:59 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $441.34
**Retorno acumulado:** -11.73%
**Peor caída desde un máximo (drawdown):** 25.62%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $140.00 en 28 posiciones abiertas (disponible para nuevas apuestas: $301.34)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| IMAREALPERSON | 18 | 5 | 1 | +20.95 USD |
| casualbet2020 | 5 | 0 | 2 | +20.35 USD |
| Lakersfan111 | 7 | 3 | 9 | +16.04 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| sentrio | 5 | 2 | 0 | +10.49 USD |
| TeGeeLP | 2 | 2 | 1 | +7.82 USD |
| Djdjdjekekek | 5 | 2 | 1 | +5.59 USD |
| Satisfied | 2 | 1 | 0 | +5.26 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 5 | 3 | 0 | +2.04 USD |
| sulumos | 1 | 0 | 0 | +1.96 USD |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | 3 | 2 | 0 | +1.93 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| BOOMBOYS.Kiritych | 2 | 1 | 0 | +1.22 USD |
| dauntlesswitness | 1 | 0 | 0 | +1.13 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 3 | 0 | +0.56 USD |
| ExplosiveNinja | 0 | 0 | 2 | +0.00 USD |
| crisp1973 | 0 | 0 | 2 | +0.00 USD |
| SDTrading | 9 | 8 | 4 | -0.02 USD |
| theowalcott | 5 | 4 | 0 | -0.44 USD |
| predictionlegend | 3 | 3 | 0 | -2.50 USD |
| CORGI8 | 1 | 2 | 0 | -3.22 USD |
| ChonkyChocolateCake | 5 | 4 | 0 | -4.44 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 3 | 4 | 2 | -7.78 USD |
| ferrariChampions2026 | 190 | 108 | 0 | -7.93 USD |
| SineNooneEI | 0 | 2 | 0 | -10.26 USD |
| HomeRunHazard | 36 | 20 | 0 | -12.70 USD |
| Sassy-Bucket | 6 | 10 | 0 | -23.92 USD |
| danielwolfmorales3pddb6dl6 | 7 | 11 | 0 | -27.05 USD |
|  | 24 | 18 | 3 | -44.03 USD |
| RN1 | 108 | 55 | 1 | -57.10 USD |

## Análisis general

- **Apuestas resueltas:** 749
- **Aciertos:** 475 (63.4%)
- **Cuota promedio de entrada:** 63.2%
- **Stake promedio:** $4.99
- **Total apostado (suma de stakes):** $3,740.45
- **ROI sobre lo apostado:** -2.46%
- **Comisiones pagadas (taker fee):** $68.77 (1.84% del capital apostado)
- **ROI que habría dado SIN comisiones:** -0.62% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 376 | 46.3% | 50.1% | -3.8 pp |
| 60-79% | 231 | 74.9% | 67.8% | +7.0 pp |
| 80-94% | 92 | 87.0% | 86.9% | +0.1 pp |
| 95-99% (casi seguro) | 50 | 96.0% | 97.3% | -1.3 pp |

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
| atp-kouame-burruch-2026-08-20 | , ferrariChampions2026 |
| mlb-oak-kc-2026-08-20-total-8pt5 | SDTrading, Sassy-Bucket |
| wta-swiatek-rybakin-2026-08-20 | RN1, danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| dota2-ngx-flc-2026-08-20 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, ChonkyChocolateCake, IMAREALPERSON |
| lol-koia-hrts-2026-08-20 | ChonkyChocolateCake, danielwolfmorales3pddb6dl6 |
| dota2-ironwi-boombo-2026-08-20 | Djdjdjekekek, IMAREALPERSON, Lakersfan111, ferrariChampions2026 |
| dota2-ironwi-boombo-2026-08-20-game1 | , Lakersfan111, ferrariChampions2026 |
| val-sen-2game-2026-08-20-game2 | Lakersfan111, casualbet2020, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-20-total-7pt5 | , RN1, Sassy-Bucket, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-20 | Djdjdjekekek, RN1, Sassy-Bucket, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-20-total-8pt5 | Sassy-Bucket, ferrariChampions2026 |
| cs2-lgc-fal2-2026-08-21-map-handicap-home-1pt5 | Lakersfan111, casualbet2020 |
| atp-magadan-wong-2026-08-20 | , RN1, ferrariChampions2026 |
| dota2-liquid-flc-2026-08-21 | , 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, Djdjdjekekek, IMAREALPERSON, Lakersfan111, ferrariChampions2026 |
| sud-mac-san-2026-08-20-mac | RN1, ferrariChampions2026 |
| cs2-fut-mouz-2026-08-21 | ExplosiveNinja, Lakersfan111 |
| mlb-laa-hou-2026-08-20 | , ferrariChampions2026 |
| cs2-lgc-fal2-2026-08-21 | , Lakersfan111 |
| wnba-conn-las-2026-08-20 | , ferrariChampions2026 |
| cs2-vit-ts7-2026-08-21 | ExplosiveNinja, Lakersfan111 |
| dota2-liquid-flc-2026-08-21-game1 | Djdjdjekekek, IMAREALPERSON, ferrariChampions2026 |
| dota2-liquid-flc-2026-08-21-game2 | , 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, Djdjdjekekek, IMAREALPERSON |
| lol-edg-tt-2026-08-21-game2 | MisterVision, TeGeeLP |
| lol-bro2-fox1-2026-08-21-game1 | IMAREALPERSON, MisterVision |
| lol-al-we-2026-08-21-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, TeGeeLP |
| dota2-ts8-vsn2-2026-08-21-game1 | Djdjdjekekek, IMAREALPERSON |
| dota2-ts8-vsn2-2026-08-21-game2 | Djdjdjekekek, IMAREALPERSON |
| dota2-ts8-vsn2-2026-08-21 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, Djdjdjekekek |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| crisp1973 | Al Faisaly Saudi Club vs. NEOM SC: O/U 2 | Over (BUY) | 55% | 5.00 | 8.1% | ⏳ pendiente | — |
| IMAREALPERSON | Valorant: Enterprise Esports vs Karmine  | Karmine Corp (BUY) | 56% | 5.00 | 4.8% | ⏳ pendiente | — |
| SDTrading | Pittsburgh Pirates vs. Los Angeles Dodge | Over (BUY) | 57% | 5.00 | 8.4% | ⏳ pendiente | — |
| SDTrading | Pittsburgh Pirates vs. Los Angeles Dodge | Over (BUY) | 47% | 5.00 | 2.5% | ⏳ pendiente | — |
| Djdjdjekekek | Dota 2: Team Spirit vs TEAM VISION (BO3) | Team Spirit (BUY) | 45% | 5.00 | 1.5% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | Dota 2: Team Spirit vs TEAM VISION (BO3) | Team Spirit (BUY) | 43% | 5.00 | 90.3% | ⏳ pendiente | — |
| crisp1973 | Will Al Qadisiyah Saudi Club win on 2026 | Yes (BUY) | 66% | 5.00 | 34.7% | ⏳ pendiente | — |
| TeGeeLP | LoL: Top Esports vs Bilibili Gaming - Ga | Bilibili Gaming (BUY) | 61% | 5.00 | 9.1% | 💰 vendida anticipada | -1.43 |
| IMAREALPERSON | Dota 2: Team Spirit vs TEAM VISION - Gam | TEAM VISION (BUY) | 51% | 5.00 | 14.5% | ❌ perdida | -5.12 |
| IMAREALPERSON | Dota 2: Team Spirit vs TEAM VISION - Gam | Team Spirit (BUY) | 47% | 5.00 | 992.8% | ✅ ganada | +5.51 |
| Djdjdjekekek | Dota 2: Team Spirit vs TEAM VISION - Gam | Team Spirit (BUY) | 47% | 5.00 | 1.8% | ✅ ganada | +5.51 |
| SDTrading | Tampa Bay Rays vs. Baltimore Orioles | Baltimore Orioles (BUY) | 55% | 5.00 | 2.0% | ⏳ pendiente | — |
| SDTrading | Washington Nationals vs. Miami Marlins | Washington Nationals (BUY) | 43% | 5.00 | 35.8% | ⏳ pendiente | — |
|  | FC Tōkyō vs. JEF United Ichihara Chiba:  | Under (BUY) | 52% | 5.00 | 12.0% | ❌ perdida | -5.12 |
|  | ITF W50 Prague Women: Alena Kovackova vs | Jana Kovackova (BUY) | 94% | 5.00 | 1.3% | ✅ ganada | +0.30 |
| IMAREALPERSON | Dota 2: Team Spirit vs TEAM VISION - Gam | Team Spirit (BUY) | 41% | 5.00 | 19.6% | 💰 vendida anticipada | -0.54 |
|  | Counter-Strike: Legacy vs Team Falcons ( | Team Falcons (BUY) | 75% | 5.00 | 1.0% | ⏳ pendiente | — |
|  | ITF W50 Prague Women: Alena Kovackova vs | Alena Kovackova (BUY) | 57% | 5.00 | 1.4% | ❌ perdida | -5.11 |
| casualbet2020 | LoL: KT Rolster vs T1 (BO3) - LCK Round  | T1 (BUY) | 72% | 5.00 | 237.9% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: Anyone's Legend vs Team WE - Game 2 | Anyone's Legend (BUY) | 58% | 5.00 | 18.0% | ⏳ pendiente | — |
| Djdjdjekekek | Dota 2: Team Spirit vs TEAM VISION - Gam | Team Spirit (BUY) | 49% | 5.00 | 15.4% | ❌ perdida | -5.13 |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: HANJIN BRION vs BNK FEARX (BO3) - L | HANJIN BRION (BUY) | 54% | 5.00 | 17.6% | ❌ perdida | -5.12 |
| TeGeeLP | LoL: Anyone's Legend vs Team WE - Game 2 | Team WE (BUY) | 41% | 5.00 | 1.9% | 💰 vendida anticipada | +7.05 |
|  | Arsenal FC vs. Coventry City FC: O/U 3.5 | Under (BUY) | 63% | 5.00 | 1.7% | ⏳ pendiente | — |
| TeGeeLP | LoL: Anyone's Legend vs Team WE - Game 1 | Team WE (BUY) | 47% | 5.00 | 3.8% | ⏳ pendiente | — |
| TeGeeLP | LoL: Anyone's Legend vs Team WE - Game 2 | Team WE (BUY) | 42% | 5.00 | 5.4% | 💰 vendida anticipada | -0.64 |
| IMAREALPERSON | Dota 2: Team Liquid vs Team Falcons (BO3 | Team Liquid (BUY) | 59% | 5.00 | 92.6% | ✅ ganada | +3.37 |
|  | Dota 2: Team Liquid vs Team Falcons (BO3 | Team Falcons (BUY) | 43% | 5.00 | 0.9% | ❌ perdida | -5.14 |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | Dota 2: Team Liquid vs Team Falcons (BO3 | Team Liquid (BUY) | 55% | 5.00 | 143.2% | ✅ ganada | +3.98 |
|  | ITF W35 Bistrita Women: Jessica Pieri vs | Jessica Pieri (BUY) | 85% | 5.00 | 1.5% | ✅ ganada | +0.84 |
