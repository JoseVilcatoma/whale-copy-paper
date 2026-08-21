# Paper trading — resultado de la simulación

Actualizado: 2026-08-21 17:53:51 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $421.60
**Retorno acumulado:** -15.68%
**Peor caída desde un máximo (drawdown):** 29.20%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $115.00 en 23 posiciones abiertas (disponible para nuevas apuestas: $306.60)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| IMAREALPERSON | 23 | 6 | 0 | +26.74 USD |
| casualbet2020 | 7 | 0 | 1 | +26.20 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| sentrio | 5 | 2 | 0 | +10.49 USD |
| BOOMBOYS.Kiritych | 5 | 2 | 0 | +10.33 USD |
| Satisfied | 2 | 1 | 0 | +5.26 USD |
| Lakersfan111 | 11 | 8 | 0 | +4.18 USD |
| TeGeeLP | 2 | 3 | 0 | +2.69 USD |
| 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 | 1 | 0 | 0 | +2.49 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 5 | 3 | 0 | +2.04 USD |
| sulumos | 1 | 0 | 0 | +1.96 USD |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | 3 | 2 | 0 | +1.93 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| dauntlesswitness | 1 | 0 | 0 | +1.13 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 3 | 0 | +0.56 USD |
| ChonkyChocolateCake | 8 | 5 | 0 | +0.13 USD |
| Djdjdjekekek | 7 | 5 | 1 | -0.26 USD |
| theowalcott | 5 | 4 | 0 | -0.44 USD |
| predictionlegend | 3 | 3 | 0 | -2.50 USD |
| CORGI8 | 1 | 2 | 0 | -3.22 USD |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 8 | 7 | 0 | -3.69 USD |
| ferrariChampions2026 | 195 | 111 | 7 | -4.11 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| Wiretransferxyz | 0 | 1 | 1 | -5.12 USD |
| crisp1973 | 1 | 2 | 0 | -5.31 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| ExplosiveNinja | 0 | 2 | 0 | -10.21 USD |
| SDTrading | 9 | 10 | 4 | -10.26 USD |
| SineNooneEI | 0 | 2 | 0 | -10.26 USD |
| HomeRunHazard | 36 | 20 | 0 | -12.70 USD |
| Sassy-Bucket | 6 | 10 | 5 | -23.92 USD |
| danielwolfmorales3pddb6dl6 | 7 | 11 | 0 | -27.05 USD |
|  | 26 | 20 | 0 | -48.67 USD |
| RN1 | 127 | 63 | 4 | -54.18 USD |

## Análisis general

- **Apuestas resueltas:** 830
- **Aciertos:** 523 (63.0%)
- **Cuota promedio de entrada:** 63.1%
- **Stake promedio:** $4.99
- **Total apostado (suma de stakes):** $4,145.45
- **ROI sobre lo apostado:** -2.89%
- **Comisiones pagadas (taker fee):** $76.45 (1.84% del capital apostado)
- **ROI que habría dado SIN comisiones:** -1.04% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 415 | 46.7% | 50.1% | -3.4 pp |
| 60-79% | 261 | 72.8% | 67.7% | +5.1 pp |
| 80-94% | 100 | 87.0% | 86.8% | +0.2 pp |
| 95-99% (casi seguro) | 54 | 96.3% | 97.3% | -1.0 pp |

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

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| Sassy-Bucket | Minnesota Lynx vs. Washington Mystics | Minnesota Lynx (BUY) | 56% | 5.00 | 4.0% | ⏳ pendiente | — |
| ferrariChampions2026 | St. Louis Cardinals vs. Philadelphia Phi | Over (BUY) | 48% | 5.00 | 3.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Zizou Bergs vs Stefanos Sak | Stefanos Sakellaridis (BUY) | 41% | 5.00 | 1.2% | ⏳ pendiente | — |
| Sassy-Bucket | San Francisco Giants vs. Boston Red Sox: | Over (BUY) | 48% | 5.00 | 2.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: MIBR vs Team Envy (BO3) - VCT  | MIBR (BUY) | 68% | 5.00 | 0.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Roman Safiullin vs Hubert Hurkac | Hubert Hurkacz (BUY) | 83% | 5.00 | 3.3% | ⏳ pendiente | — |
| Sassy-Bucket | Washington Nationals vs. Miami Marlins:  | Over (BUY) | 44% | 5.00 | 5.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: MIBR vs Team Envy - Map 2 Winn | MIBR (BUY) | 73% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | St. Louis Cardinals vs. Philadelphia Phi | Over (BUY) | 55% | 5.00 | 0.3% | ⏳ pendiente | — |
| Sassy-Bucket | Washington Nationals vs. Miami Marlins:  | Over (BUY) | 52% | 5.00 | 5.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Zizou Bergs vs Stefanos Sak | Zizou Bergs (BUY) | 81% | 5.00 | 1.8% | ⏳ pendiente | — |
| Sassy-Bucket | Cleveland Guardians vs. Colorado Rockies | Under (BUY) | 51% | 5.00 | 6.0% | ⏳ pendiente | — |
| casualbet2020 | Valorant: Bilibili Gaming vs TYLOO (BO5) | TYLOO (BUY) | 58% | 5.00 | 34.5% | ⏳ pendiente | — |
| RN1 | Atlanta Braves vs. Milwaukee Brewers | Milwaukee Brewers (BUY) | 93% | 5.00 | 0.6% | ✅ ganada | +0.36 |
| RN1 | Quebec City: Zizou Bergs vs Stefanos Sak | Stefanos Sakellaridis (BUY) | 62% | 5.00 | 1.1% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Taylor Fritz vs Brandon | Brandon Nakashima (BUY) | 45% | 5.00 | 0.8% | ✅ ganada | +5.97 |
| RN1 | Cincinnati Open: Taylor Fritz vs Brandon | Taylor Fritz (BUY) | 69% | 5.00 | 0.5% | ❌ perdida | -5.08 |
| Djdjdjekekek | Dota 2: Team Spirit vs Team Liquid (BO3) | Team Spirit (BUY) | 60% | 5.00 | 652.7% | ⏳ pendiente | — |
|  | Atlanta Braves vs. Milwaukee Brewers | Atlanta Braves (BUY) | 44% | 5.00 | 0.8% | ❌ perdida | -5.14 |
| Wiretransferxyz | Will Team Spirit Win the CS2 EWC 2026? | Yes (BUY) | 46% | 5.00 | 9.4% | ⏳ pendiente | — |
| Wiretransferxyz | Valorant: BBL Esports vs FUT Esports (BO | BBL Esports (BUY) | 50% | 5.00 | 6.9% | ❌ perdida | -5.12 |
| Djdjdjekekek | Valorant: BBL Esports vs FUT Esports (BO | FUT Esports (BUY) | 50% | 5.00 | 705.8% | ✅ ganada | +4.88 |
| Djdjdjekekek | Counter-Strike: Vitality vs Spirit (BO3) | Vitality (BUY) | 51% | 5.00 | 3574.0% | ❌ perdida | -5.12 |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | LoL: Team Vitality vs Natus Vincere (BO3 | Team Vitality (BUY) | 55% | 5.00 | 93.5% | 💰 vendida anticipada | +3.41 |
| IMAREALPERSON | Dota 2: Team Yandex vs Nigma Galaxy (BO3 | Team Yandex (BUY) | 99% | 5.00 | 345.6% | ✅ ganada | +0.05 |
| IMAREALPERSON | Dota 2: Team Yandex vs Nigma Galaxy (BO3 | Team Yandex (BUY) | 59% | 5.00 | 81.8% | 💰 vendida anticipada | +2.31 |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | Dota 2: Team Yandex vs Nigma Galaxy (BO3 | Nigma Galaxy (BUY) | 49% | 5.00 | 54.5% | 💰 vendida anticipada | +0.46 |
| BOOMBOYS.Kiritych | Dota 2: Team Yandex vs Nigma Galaxy (BO3 | Team Yandex (BUY) | 61% | 5.00 | 6.0% | ✅ ganada | +3.10 |
| RN1 | Cincinnati Open: Sara Bejlek vs Madison  | Madison Keys (BUY) | 63% | 5.00 | 6.0% | ❌ perdida | -5.09 |
| RN1 | Seinajoen JK vs. FC Lahti: O/U 1.5 | Over (BUY) | 49% | 5.00 | 0.4% | ✅ ganada | +5.08 |
