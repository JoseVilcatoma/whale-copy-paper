# Paper trading — resultado de la simulación

Actualizado: 2026-08-23 07:33:56 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $531.99
**Retorno acumulado:** +6.40%
**Peor caída desde un máximo (drawdown):** 29.20%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $360.00 en 72 posiciones abiertas (disponible para nuevas apuestas: $171.99)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 | 16 | 3 | 8 | +43.99 USD |
| swisstony | 30 | 1 | 0 | +43.66 USD |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 34 | 14 | 2 | +33.12 USD |
| casualbet2020 | 13 | 4 | 0 | +28.91 USD |
| IMAREALPERSON | 29 | 10 | 0 | +27.06 USD |
| BOOMBOYS.Kiritych | 14 | 7 | 5 | +23.83 USD |
| kekasaur | 3 | 0 | 0 | +15.34 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| ChonkyChocolateCake | 22 | 14 | 2 | +11.72 USD |
| sentrio | 5 | 2 | 0 | +10.49 USD |
| Sunshine.Smile | 6 | 3 | 0 | +9.80 USD |
| Satisfied | 2 | 1 | 0 | +5.26 USD |
| Lakersfan111 | 11 | 8 | 0 | +4.18 USD |
| ferrariChampions2026 | 204 | 115 | 0 | +3.88 USD |
| pleaseplease123 | 2 | 1 | 0 | +3.52 USD |
| SDTrading | 16 | 13 | 0 | +3.35 USD |
| TeGeeLP | 2 | 3 | 0 | +2.69 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 5 | 3 | 0 | +2.04 USD |
| sulumos | 1 | 0 | 0 | +1.96 USD |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | 3 | 2 | 0 | +1.93 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| beachboy4 | 1 | 0 | 0 | +1.78 USD |
| HVAB | 2 | 0 | 0 | +1.13 USD |
| dauntlesswitness | 1 | 0 | 0 | +1.13 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 3 | 0 | +0.56 USD |
| plonker2026 | 0 | 0 | 4 | +0.00 USD |
| theowalcott | 5 | 4 | 0 | -0.44 USD |
| predictionlegend | 3 | 3 | 0 | -2.50 USD |
| CORGI8 | 1 | 2 | 0 | -3.22 USD |
| monkeymashingkeyboard | 0 | 1 | 0 | -5.08 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| WTSA | 0 | 1 | 0 | -5.12 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| ExplosiveNinja | 0 | 2 | 0 | -10.21 USD |
| SineNooneEI | 0 | 2 | 0 | -10.26 USD |
| kluckkluck | 0 | 2 | 0 | -10.27 USD |
| crisp1973 | 1 | 3 | 0 | -10.43 USD |
| Wiretransferxyz | 3 | 4 | 4 | -11.20 USD |
| Djdjdjekekek | 10 | 11 | 2 | -15.81 USD |
| HomeRunHazard | 76 | 46 | 16 | -16.19 USD |
| danielwolfmorales3pddb6dl6 | 14 | 17 | 0 | -20.20 USD |
| Sassy-Bucket | 11 | 15 | 0 | -28.06 USD |
|  | 28 | 21 | 0 | -50.55 USD |
| RN1 | 162 | 78 | 29 | -52.37 USD |

## Análisis general

- **Apuestas resueltas:** 1105
- **Aciertos:** 700 (63.3%)
- **Cuota promedio de entrada:** 62.5%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $5,520.45
- **ROI sobre lo apostado:** -0.70%
- **Comisiones pagadas (taker fee):** $103.62 (1.88% del capital apostado)
- **ROI que habría dado SIN comisiones:** +1.18% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 575 | 50.1% | 50.3% | -0.2 pp |
| 60-79% | 342 | 70.5% | 67.7% | +2.7 pp |
| 80-94% | 126 | 88.1% | 86.7% | +1.4 pp |
| 95-99% (casi seguro) | 62 | 96.8% | 97.3% | -0.5 pp |

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
| cs2-lgc-fal2-2026-08-21-map-handicap-home-1pt5 | Lakersfan111, casualbet2020, ferrariChampions2026 |
| atp-magadan-wong-2026-08-20 | , RN1, ferrariChampions2026 |
| dota2-liquid-flc-2026-08-21 | , 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, Djdjdjekekek, IMAREALPERSON, Lakersfan111, ferrariChampions2026 |
| dota2-ty-ngx-2026-08-21 | 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3, 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, BOOMBOYS.Kiritych, Djdjdjekekek, IMAREALPERSON, Lakersfan111, ferrariChampions2026 |
| sud-mac-san-2026-08-20-mac | RN1, ferrariChampions2026 |
| cs2-fut-mouz-2026-08-21 | ExplosiveNinja, Lakersfan111 |
| mlb-laa-hou-2026-08-20 | , ferrariChampions2026 |
| cs2-lgc-fal2-2026-08-21 | , Lakersfan111, ferrariChampions2026 |
| wnba-conn-las-2026-08-20 | , ferrariChampions2026 |
| cs2-vit-ts7-2026-08-21 | BOOMBOYS.Kiritych, Djdjdjekekek, ExplosiveNinja, Lakersfan111 |
| dota2-liquid-flc-2026-08-21-game1 | Djdjdjekekek, IMAREALPERSON, ferrariChampions2026 |
| dota2-liquid-flc-2026-08-21-game2 | , 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, Djdjdjekekek, IMAREALPERSON |
| lol-edg-tt-2026-08-21-game2 | MisterVision, TeGeeLP |
| lol-bro2-fox1-2026-08-21-game1 | IMAREALPERSON, MisterVision |
| lol-al-we-2026-08-21-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, TeGeeLP |
| dota2-ts8-vsn2-2026-08-21-game1 | Djdjdjekekek, IMAREALPERSON |
| dota2-ts8-vsn2-2026-08-21-game2 | Djdjdjekekek, IMAREALPERSON |
| dota2-ts8-vsn2-2026-08-21 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, Djdjdjekekek, IMAREALPERSON |
| mlb-pit-lad-2026-08-21-total-8pt5 | HomeRunHazard, SDTrading |
| cs2-lgc-fal2-2026-08-21-game1 | Djdjdjekekek, ferrariChampions2026 |
| atp-stricke-compagn-2026-08-21 | RN1, ferrariChampions2026 |
| itf-cvetko-guth-2026-08-21 | RN1, ferrariChampions2026 |
| dota2-ty-ngx-2026-08-21-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON |
| spl-haz-dir-2026-08-21-dir | RN1, crisp1973 |
| dota2-ty-ngx-2026-08-21-game2 | BOOMBOYS.Kiritych, MisterVision |
| lol-vit-navi-2026-08-21-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, MisterVision |
| val-bbl1-fut1-2026-08-21 | Djdjdjekekek, Wiretransferxyz |
| mlb-atl-mil-2026-08-21 | , RN1 |
| atp-bergs-sakella-2026-08-21 | RN1, ferrariChampions2026 |
| mlb-sf-bos-2026-08-21-total-7pt5 | Sassy-Bucket, ferrariChampions2026 |
| chi1-aci-cul-2026-08-21-aci | 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3, kluckkluck |
| val-sen-kru1-2026-08-22 | Wiretransferxyz, casualbet2020 |
| dota2-ts8-liquid-2026-08-21-game2 | BOOMBOYS.Kiritych, IMAREALPERSON |
| cs2-furia-fut-2026-08-22 | BOOMBOYS.Kiritych, Djdjdjekekek, danielwolfmorales3pddb6dl6 |
| dota2-ngx-boombo-2026-08-22-game2 | BOOMBOYS.Kiritych, IMAREALPERSON |
| lol-we-lgd-2026-08-22-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON, danielwolfmorales3pddb6dl6 |
| lol-we-lgd-2026-08-22-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, MisterVision, danielwolfmorales3pddb6dl6 |
| lol-dk-gen-2026-08-22-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON, MisterVision, danielwolfmorales3pddb6dl6 |
| dota2-vsn2-ty-2026-08-22-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON |
| dota2-vsn2-ty-2026-08-22 | Djdjdjekekek, MisterVision |
| lol-nip-ig1-2026-08-22-game1 | MisterVision, danielwolfmorales3pddb6dl6 |
| el1-don-bar-2026-08-22-don | RN1, crisp1973 |
| atp-tarvet-poullai-2026-08-22 | HomeRunHazard, RN1 |
| epl-hul-mun-2026-08-22-spread-away-1pt5 | RN1, danielwolfmorales3pddb6dl6 |
| val-bst1-g21-2026-08-22 | Wiretransferxyz, casualbet2020 |
| wta-pegula-swiatek-2026-08-22 | HomeRunHazard, monkeymashingkeyboard |
| mlb-atl-mil-2026-08-22 | HomeRunHazard, SDTrading |
| lol-fnc-shft-2026-08-22-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, MisterVision, Sunshine.Smile |
| mlb-tor-nyy-2026-08-22-total-6pt5 | HomeRunHazard, SDTrading, pleaseplease123 |
| lol-sen-fly-2026-08-22-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, MisterVision |
| mlb-laa-tex-2026-08-22-total-8pt5 | 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3, SDTrading |
| lol-dsg-dig-2026-08-22-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, MisterVision |
| cs2-furia-lgc-2026-08-23 | BOOMBOYS.Kiritych, Wiretransferxyz |
| mls-orl-rsl-2026-08-22-orl | 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3, kekasaur |
| epl-new-liv-2026-08-23-liv | 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3, RN1, plonker2026 |
| dota2-ty-ts8-2026-08-22-game1 | , 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, Djdjdjekekek |
| itf-kisimov-juhas-2026-08-23 | , RN1 |
| dota2-ty-ts8-2026-08-22-game2 | BOOMBOYS.Kiritych, Djdjdjekekek, MisterVision |
| dota2-vsn2-ts8-2026-08-23 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, BOOMBOYS.Kiritych, Djdjdjekekek |
| dota2-vsn2-ts8-2026-08-23-game1 | BOOMBOYS.Kiritych, MisterVision |
| lol-tt-lgd-2026-08-23-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, MisterVision |
| dota2-vsn2-ts8-2026-08-23-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, BOOMBOYS.Kiritych, MisterVision |
| lol-tt-lgd-2026-08-23-game2 | BOOMBOYS.Kiritych, MisterVision, Sunshine.Smile |
| lol-hle1-t1-2026-08-23-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, BOOMBOYS.Kiritych, MisterVision, Sunshine.Smile |
| cs2-fut-ts7-2026-08-23-map-handicap-home-1pt5 | BOOMBOYS.Kiritych, Wiretransferxyz |
| lol-hle1-t1-2026-08-23-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, BOOMBOYS.Kiritych |
| dota2-vsn2-ts8-2026-08-23-game3 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, BOOMBOYS.Kiritych, MisterVision, Sunshine.Smile |
| dfb-fur-boc-2026-08-23-boc | RN1, plonker2026 |
| dota2-vsn2-ts8-2026-08-23-game4 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, BOOMBOYS.Kiritych, Sunshine.Smile |
| lol-fox1-ns-2026-08-23 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, SPCEXBUYER |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | Will SSV Jeddeloh II win on 2026-08-23? | Yes (BUY) | 97% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | Will Liverpool FC win on 2026-08-23? | No (BUY) | 50% | 5.00 | 3.1% | ⏳ pendiente | — |
| SPCEXBUYER | LoL: Bilibili Gaming vs Anyone's Legend  | Anyone's Legend (BUY) | 43% | 5.00 | 2.7% | ⏳ pendiente | — |
| RN1 | West Bromwich Albion FC vs. Burnley FC:  | Over (BUY) | 58% | 5.00 | 0.5% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | Dota 2: TEAM VISION vs Team Spirit (BO5) | TEAM VISION (BUY) | 53% | 5.00 | 883.4% | ⏳ pendiente | — |
| RN1 | Will Randers FC win on 2026-08-23? | No (BUY) | 91% | 5.00 | 0.5% | ⏳ pendiente | — |
| HomeRunHazard | Athletics vs. Houston Astros | Houston Astros (BUY) | 63% | 5.00 | 4.0% | ⏳ pendiente | — |
| RN1 | Spread: SpVgg Greuther Fürth (-1.5) | VfL Bochum (BUY) | 99% | 5.00 | 1.1% | ⏳ pendiente | — |
| RN1 | Augsburg: Georgii Kravchenko vs Dominik  | Georgii Kravchenko (BUY) | 61% | 5.00 | 2.0% | ⏳ pendiente | — |
| RN1 | ITF W15 Logrono Women: Juliana Giaccio v | Juliana Giaccio (BUY) | 87% | 5.00 | 2.4% | ⏳ pendiente | — |
| 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 | Will Liverpool FC win on 2026-08-23? | No (BUY) | 50% | 5.00 | 34.9% | ⏳ pendiente | — |
| RN1 | Will Young Boys Bern win on 2026-08-23? | Yes (BUY) | 88% | 5.00 | 1.0% | ⏳ pendiente | — |
| RN1 | Will Burnley FC win on 2026-08-23? | No (BUY) | 94% | 5.00 | 1.1% | ⏳ pendiente | — |
| 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 | Manchester City FC vs. AFC Bournemouth:  | Over (BUY) | 50% | 5.00 | 6.3% | ⏳ pendiente | — |
| 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 | Will Beşiktaş JK win on 2026-08-23? | No (BUY) | 45% | 5.00 | 4.7% | ⏳ pendiente | — |
| RN1 | Will Go Ahead Eagles win on 2026-08-23? | Yes (BUY) | 88% | 5.00 | 0.5% | ⏳ pendiente | — |
| SPCEXBUYER | LoL: BNK FEARX vs Nongshim Red Force (BO | BNK FEARX (BUY) | 56% | 5.00 | 37.6% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: BNK FEARX vs Nongshim Red Force (BO | BNK FEARX (BUY) | 53% | 5.00 | 14.4% | 💰 vendida anticipada | -1.46 |
| RN1 | West Bromwich Albion FC vs. Burnley FC:  | Under (BUY) | 98% | 5.00 | 1.3% | ⏳ pendiente | — |
| RN1 | Will Aarhus GF win on 2026-08-21? | Yes (BUY) | 50% | 5.00 | 2.4% | ⏳ pendiente | — |
| RN1 | SpVgg Greuther Fürth vs. VfL Bochum: O/U | Over (BUY) | 52% | 5.00 | 1.2% | ⏳ pendiente | — |
| RN1 | Will 1. FC Heidenheim 1846 win on 2026-0 | No (BUY) | 68% | 5.00 | 1.8% | ⏳ pendiente | — |
| MisterVision | LoL: EDward Gaming vs JD Gaming (BO3) -  | JD Gaming (BUY) | 74% | 5.00 | 21.4% | ⏳ pendiente | — |
| RN1 | Will Go Ahead Eagles vs. ADO Den Haag en | No (BUY) | 85% | 5.00 | 2.0% | ⏳ pendiente | — |
| RN1 | ITF M25 Lesa Men: Pierluigi Basile vs Al | Pierluigi Basile (BUY) | 89% | 5.00 | 0.7% | ✅ ganada | +0.59 |
| RN1 | West Bromwich Albion FC vs. Burnley FC:  | Over (BUY) | 57% | 5.00 | 1.0% | ⏳ pendiente | — |
| RN1 | Will VfL Bochum win on 2026-08-23? | Yes (BUY) | 64% | 5.00 | 2.1% | ⏳ pendiente | — |
| RN1 | ITF W35 Erwitte Women: Josy Daems vs Val | Valentina Steiner (BUY) | 60% | 5.00 | 0.6% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: CTBC Flying Oyster vs Team Secret W | CTBC Flying Oyster (BUY) | 62% | 5.00 | 2.2% | 💰 vendida anticipada | -2.21 |
| RN1 | Will VfL Bochum win on 2026-08-23? | No (BUY) | 65% | 5.00 | 3.3% | ⏳ pendiente | — |
