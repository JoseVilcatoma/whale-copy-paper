# Paper trading — resultado de la simulación

Actualizado: 2026-08-22 08:43:24 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $451.77
**Retorno acumulado:** -9.65%
**Peor caída desde un máximo (drawdown):** 29.20%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $270.00 en 54 posiciones abiertas (disponible para nuevas apuestas: $181.77)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| IMAREALPERSON | 28 | 9 | 1 | +31.38 USD |
| casualbet2020 | 8 | 2 | 1 | +19.47 USD |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 14 | 7 | 0 | +17.54 USD |
| 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 | 4 | 0 | 6 | +15.05 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| BOOMBOYS.Kiritych | 7 | 3 | 1 | +11.84 USD |
| sentrio | 5 | 2 | 0 | +10.49 USD |
| Satisfied | 2 | 1 | 0 | +5.26 USD |
| Lakersfan111 | 11 | 8 | 0 | +4.18 USD |
| ferrariChampions2026 | 204 | 115 | 0 | +3.88 USD |
| TeGeeLP | 2 | 3 | 0 | +2.69 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 5 | 3 | 0 | +2.04 USD |
| sulumos | 1 | 0 | 0 | +1.96 USD |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | 3 | 2 | 0 | +1.93 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| HVAB | 2 | 0 | 0 | +1.13 USD |
| dauntlesswitness | 1 | 0 | 0 | +1.13 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 3 | 0 | +0.56 USD |
| Sunshine.Smile | 0 | 0 | 1 | +0.00 USD |
| monkeymashingkeyboard | 0 | 0 | 1 | +0.00 USD |
| theowalcott | 5 | 4 | 0 | -0.44 USD |
| Djdjdjekekek | 9 | 6 | 0 | -1.70 USD |
| SDTrading | 12 | 11 | 2 | -2.25 USD |
| predictionlegend | 3 | 3 | 0 | -2.50 USD |
| CORGI8 | 1 | 2 | 0 | -3.22 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| Wiretransferxyz | 0 | 1 | 2 | -5.12 USD |
| crisp1973 | 1 | 2 | 1 | -5.31 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| ExplosiveNinja | 0 | 2 | 0 | -10.21 USD |
| SineNooneEI | 0 | 2 | 0 | -10.26 USD |
| kluckkluck | 0 | 2 | 0 | -10.27 USD |
| ChonkyChocolateCake | 10 | 8 | 3 | -10.51 USD |
| HomeRunHazard | 47 | 26 | 6 | -14.80 USD |
| danielwolfmorales3pddb6dl6 | 9 | 12 | 9 | -19.45 USD |
| Sassy-Bucket | 9 | 14 | 0 | -30.65 USD |
|  | 26 | 20 | 0 | -48.67 USD |
| RN1 | 136 | 66 | 20 | -49.72 USD |

## Análisis general

- **Apuestas resueltas:** 911
- **Aciertos:** 575 (63.1%)
- **Cuota promedio de entrada:** 62.9%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $4,550.45
- **ROI sobre lo apostado:** -2.31%
- **Comisiones pagadas (taker fee):** $84.50 (1.86% del capital apostado)
- **ROI que habría dado SIN comisiones:** -0.45% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 461 | 47.3% | 50.1% | -2.9 pp |
| 60-79% | 286 | 73.1% | 67.6% | +5.5 pp |
| 80-94% | 107 | 86.9% | 86.7% | +0.2 pp |
| 95-99% (casi seguro) | 57 | 96.5% | 97.2% | -0.8 pp |

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
| dota2-ts8-liquid-2026-08-21-game2 | BOOMBOYS.Kiritych, IMAREALPERSON |
| cs2-furia-fut-2026-08-22 | BOOMBOYS.Kiritych, danielwolfmorales3pddb6dl6 |
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

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| SDTrading | Atlanta Braves vs. Milwaukee Brewers | Milwaukee Brewers (BUY) | 63% | 5.00 | 76.2% | ⏳ pendiente | — |
| monkeymashingkeyboard | Cincinnati Open: Jessica Pegula vs Iga S | Iga Swiatek (BUY) | 69% | 5.00 | 10.3% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Set Handicap: Gauff (-1.5) vs Bejlek (+1 | Bejlek (BUY) | 48% | 5.00 | 1.5% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Cincinnati Open: Brandon Nakashima vs Fr | Brandon Nakashima (BUY) | 53% | 5.00 | 15.2% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Prague 2: Chun-Hsin Tseng vs Jan Kumstat | Chun-Hsin Tseng (BUY) | 61% | 5.00 | 21.1% | ⏳ pendiente | — |
| 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 | Will Rochdale AFC win on 2026-08-22? | No (BUY) | 47% | 5.00 | 1.4% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Counter-Strike: FURIA vs FUT Esports (BO | FUT Esports (BUY) | 41% | 5.00 | 16.1% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | LoL: JD Gaming vs Top Esports - Game 1 W | JD Gaming (BUY) | 57% | 5.00 | 42.4% | ⏳ pendiente | — |
| SDTrading | St. Louis Cardinals vs. Philadelphia Phi | Philadelphia Phillies (BUY) | 56% | 5.00 | 81.5% | ⏳ pendiente | — |
| Sunshine.Smile | LoL: DN SOOPers vs Kiwoom DRX - Game 2 W | DN SOOPers (BUY) | 58% | 5.00 | 14.2% | ⏳ pendiente | — |
| HomeRunHazard | Sion: Benjamin Hassan vs Dominic Stephan | Dominic Stephan Stricker (BUY) | 95% | 5.00 | 1.2% | ✅ ganada | +0.25 |
| Wiretransferxyz | Valorant: BESTIA vs G2 Esports (BO3) - V | G2 Esports (BUY) | 76% | 5.00 | 6.0% | ⏳ pendiente | — |
| RN1 | Millwall FC vs. Norwich City FC: 1st Hal | Over (BUY) | 54% | 5.00 | 0.6% | ⏳ pendiente | — |
| RN1 | Will Hull City AFC win on 2026-08-22? | No (BUY) | 75% | 5.00 | 0.8% | ⏳ pendiente | — |
| RN1 | Will Barnsley FC win on 2026-08-22? | No (BUY) | 75% | 5.00 | 0.6% | ⏳ pendiente | — |
| RN1 | Will Manchester United FC win on 2026-08 | No (BUY) | 53% | 5.00 | 3.0% | ⏳ pendiente | — |
| RN1 | Will Millwall FC win on 2026-08-22? | Yes (BUY) | 58% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | Hull City AFC vs. Manchester United FC:  | Over (BUY) | 75% | 5.00 | 1.6% | ⏳ pendiente | — |
| RN1 | Will Norwich City FC win on 2026-08-22? | No (BUY) | 83% | 5.00 | 0.4% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Los Angeles Sparks (-3.5) | Los Angeles Sparks (BUY) | 54% | 5.00 | 1.2% | ⏳ pendiente | — |
| RN1 | Will Portsmouth FC win on 2026-08-22? | Yes (BUY) | 80% | 5.00 | 1.0% | ⏳ pendiente | — |
| RN1 | Birmingham City FC vs. Bristol City FC:  | Over (BUY) | 66% | 5.00 | 0.6% | ⏳ pendiente | — |
| RN1 | Will Millwall FC win on 2026-08-22? | No (BUY) | 66% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | Hull City AFC vs. Manchester United FC:  | Under (BUY) | 47% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | Will Hull City AFC vs. Manchester United | No (BUY) | 83% | 5.00 | 1.2% | ⏳ pendiente | — |
| MisterVision | Dota 2: TEAM VISION vs Team Yandex (BO3) | TEAM VISION (BUY) | 69% | 5.00 | 33.3% | ✅ ganada | +2.17 |
| RN1 | Hull City AFC vs. Manchester United FC:  | Over (BUY) | 72% | 5.00 | 0.6% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Spread: Manchester United FC (-1.5) | Manchester United FC (BUY) | 50% | 5.00 | 40.7% | ⏳ pendiente | — |
| RN1 | Spread: Manchester United FC (-1.5) | Hull City AFC (BUY) | 52% | 5.00 | 1.5% | ⏳ pendiente | — |
| RN1 | ITF M25 Idanha-a-Nova 2 Men: Goncalo Mar | Goncalo Marques (BUY) | 69% | 5.00 | 0.6% | ✅ ganada | +2.17 |
