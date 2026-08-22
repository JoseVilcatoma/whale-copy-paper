# Paper trading — resultado de la simulación

Actualizado: 2026-08-22 04:49:27 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $441.18
**Retorno acumulado:** -11.76%
**Peor caída desde un máximo (drawdown):** 29.20%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $150.00 en 30 posiciones abiertas (disponible para nuevas apuestas: $291.18)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| IMAREALPERSON | 26 | 8 | 4 | +27.44 USD |
| casualbet2020 | 7 | 2 | 2 | +15.95 USD |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 13 | 7 | 1 | +14.31 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| BOOMBOYS.Kiritych | 7 | 3 | 1 | +11.84 USD |
| 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 | 3 | 0 | 6 | +11.23 USD |
| sentrio | 5 | 2 | 0 | +10.49 USD |
| Satisfied | 2 | 1 | 0 | +5.26 USD |
| Lakersfan111 | 11 | 8 | 0 | +4.18 USD |
| ferrariChampions2026 | 204 | 115 | 0 | +3.88 USD |
| Djdjdjekekek | 8 | 5 | 0 | +2.97 USD |
| TeGeeLP | 2 | 3 | 0 | +2.69 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 5 | 3 | 0 | +2.04 USD |
| sulumos | 1 | 0 | 0 | +1.96 USD |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | 3 | 2 | 0 | +1.93 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| HVAB | 2 | 0 | 0 | +1.13 USD |
| dauntlesswitness | 1 | 0 | 0 | +1.13 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 3 | 0 | +0.56 USD |
| ChonkyChocolateCake | 8 | 5 | 3 | +0.13 USD |
| theowalcott | 5 | 4 | 0 | -0.44 USD |
| SDTrading | 12 | 11 | 0 | -2.25 USD |
| predictionlegend | 3 | 3 | 0 | -2.50 USD |
| CORGI8 | 1 | 2 | 0 | -3.22 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| Wiretransferxyz | 0 | 1 | 1 | -5.12 USD |
| crisp1973 | 1 | 2 | 0 | -5.31 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| ExplosiveNinja | 0 | 2 | 0 | -10.21 USD |
| SineNooneEI | 0 | 2 | 0 | -10.26 USD |
| kluckkluck | 0 | 2 | 0 | -10.27 USD |
| HomeRunHazard | 45 | 26 | 3 | -17.12 USD |
| danielwolfmorales3pddb6dl6 | 7 | 11 | 4 | -27.05 USD |
| Sassy-Bucket | 9 | 14 | 0 | -30.65 USD |
|  | 26 | 20 | 0 | -48.67 USD |
| RN1 | 128 | 63 | 5 | -51.21 USD |

## Análisis general

- **Apuestas resueltas:** 882
- **Aciertos:** 555 (62.9%)
- **Cuota promedio de entrada:** 62.9%
- **Stake promedio:** $4.99
- **Total apostado (suma de stakes):** $4,405.45
- **ROI sobre lo apostado:** -2.62%
- **Comisiones pagadas (taker fee):** $81.84 (1.86% del capital apostado)
- **ROI que habría dado SIN comisiones:** -0.77% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 448 | 47.1% | 50.1% | -3.0 pp |
| 60-79% | 274 | 73.0% | 67.6% | +5.4 pp |
| 80-94% | 104 | 86.5% | 86.8% | -0.2 pp |
| 95-99% (casi seguro) | 56 | 96.4% | 97.3% | -0.9 pp |

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
| dota2-ngx-boombo-2026-08-22-game2 | BOOMBOYS.Kiritych, IMAREALPERSON |
| lol-we-lgd-2026-08-22-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON, danielwolfmorales3pddb6dl6 |
| lol-we-lgd-2026-08-22-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, MisterVision, danielwolfmorales3pddb6dl6 |
| lol-dk-gen-2026-08-22-game2 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON, MisterVision, danielwolfmorales3pddb6dl6 |
| dota2-vsn2-ty-2026-08-22-game1 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, IMAREALPERSON |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| HomeRunHazard | Spread: Los Angeles Sparks (-3.5) | Connecticut Sun (BUY) | 46% | 5.00 | 3.1% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: Ninjas in Pyjamas vs Invictus Gamin | Invictus Gaming (BUY) | 54% | 5.00 | 12.2% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: Dplus KIA vs Gen.G - Game 2 Winner | Dplus KIA (BUY) | 49% | 5.00 | 59.9% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: Dplus KIA vs Gen.G - Game 2 Winner | Dplus KIA (BUY) | 60% | 5.00 | 16.1% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | Dota 2: TEAM VISION vs Team Yandex - Gam | TEAM VISION (BUY) | 47% | 5.00 | 2.1% | 💰 vendida anticipada | +4.28 |
| IMAREALPERSON | Dota 2: TEAM VISION vs Team Yandex - Gam | Team Yandex (BUY) | 51% | 5.00 | 167.0% | ⏳ pendiente | — |
| MisterVision | LoL: Dplus KIA vs Gen.G - Game 2 Winner | Gen.G (BUY) | 59% | 5.00 | 28.7% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | LoL: DN SOOPers vs Kiwoom DRX (BO3) - LC | DN SOOPers (BUY) | 56% | 5.00 | 23.6% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | LoL: Dplus KIA vs Gen.G - Game 2 Winner | Dplus KIA (BUY) | 42% | 5.00 | 21.2% | ⏳ pendiente | — |
| HomeRunHazard | KBO: Kia Tigers vs. Kiwoom Heroes | Kia Tigers (BUY) | 65% | 5.00 | 3.7% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: Team WE vs LGD Gaming (BO3) - LPL G | LGD Gaming (BUY) | 48% | 5.00 | 40.8% | 💰 vendida anticipada | +2.91 |
| RN1 | ITF M25 Ueberlingen Men: Nicola Senn vs  | Tymur Bieldiugin (BUY) | 69% | 5.00 | 2.8% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: Team WE vs LGD Gaming - Game 2 Winn | LGD Gaming (BUY) | 50% | 5.00 | 1.2% | 💰 vendida anticipada | +4.35 |
| MisterVision | LoL: Dplus KIA vs Gen.G - Game 1 Winner | Gen.G (BUY) | 66% | 5.00 | 86.7% | ⏳ pendiente | — |
| MisterVision | LoL: Team WE vs LGD Gaming - Game 2 Winn | Team WE (BUY) | 59% | 5.00 | 37.6% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | LoL: Team WE vs LGD Gaming - Game 2 Winn | LGD Gaming (BUY) | 45% | 5.00 | 58.8% | ⏳ pendiente | — |
| RN1 | Hull City AFC vs. Manchester United FC:  | Under (BUY) | 43% | 5.00 | 5.8% | ⏳ pendiente | — |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | Dota 2: Nigma Galaxy vs BoomBoys (BO3) - | BoomBoys (BUY) | 60% | 5.00 | 615.8% | ✅ ganada | +3.23 |
| IMAREALPERSON | Game Handicap: VSN (-1.5) vs Team Yandex | Team Yandex (BUY) | 55% | 5.00 | 89.3% | ⏳ pendiente | — |
| IMAREALPERSON | LoL: Team WE vs LGD Gaming - Game 1 Winn | LGD Gaming (BUY) | 46% | 5.00 | 64.5% | 💰 vendida anticipada | +0.38 |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: Team WE vs LGD Gaming - Game 1 Winn | LGD Gaming (BUY) | 43% | 5.00 | 13.3% | 💰 vendida anticipada | +3.23 |
| danielwolfmorales3pddb6dl6 | LoL: Team WE vs LGD Gaming - Game 1 Winn | LGD Gaming (BUY) | 48% | 5.00 | 42.7% | ⏳ pendiente | — |
| IMAREALPERSON | Dota 2: Nigma Galaxy vs BoomBoys - Game  | BoomBoys (BUY) | 55% | 5.00 | 133.9% | 💰 vendida anticipada | -0.13 |
| BOOMBOYS.Kiritych | Dota 2: Nigma Galaxy vs BoomBoys - Game  | BoomBoys (BUY) | 53% | 5.00 | 112.8% | ❌ perdida | -5.12 |
| 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 | Will Club Tijuana win on 2026-08-22? | No (BUY) | 85% | 5.00 | 8.3% | ⏳ pendiente | — |
| HomeRunHazard | Indiana Fever vs. New York Liberty: O/U  | Under (BUY) | 55% | 5.00 | 0.7% | ⏳ pendiente | — |
| 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 | Everton FC vs. Crystal Palace FC: O/U 9. | Over (BUY) | 51% | 5.00 | 2.6% | ⏳ pendiente | — |
| BOOMBOYS.Kiritych | Counter-Strike: FURIA vs FUT Esports (BO | FUT Esports (BUY) | 41% | 5.00 | 0.4% | ⏳ pendiente | — |
| BOOMBOYS.Kiritych | Dota 2: Nigma Galaxy vs BoomBoys - Game  | BoomBoys (BUY) | 66% | 5.00 | 167.3% | ✅ ganada | +2.49 |
| HomeRunHazard | Pittsburgh Pirates vs. Los Angeles Dodge | Pittsburgh Pirates (BUY) | 48% | 5.00 | 0.6% | ❌ perdida | -5.13 |
