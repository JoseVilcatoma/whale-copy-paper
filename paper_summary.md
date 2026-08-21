# Paper trading — resultado de la simulación

Actualizado: 2026-08-20 21:05:21 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $488.68
**Retorno acumulado:** -2.26%
**Peor caída desde un máximo (drawdown):** 25.62%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $205.00 en 41 posiciones abiertas (disponible para nuevas apuestas: $283.68)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| Lakersfan111 | 4 | 0 | 13 | +19.61 USD |
| IMAREALPERSON | 13 | 1 | 0 | +19.00 USD |
| casualbet2020 | 4 | 0 | 0 | +13.30 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| sentrio | 5 | 2 | 0 | +10.49 USD |
| Satisfied | 2 | 1 | 0 | +5.26 USD |
| ferrariChampions2026 | 173 | 96 | 15 | +4.93 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 5 | 3 | 0 | +2.04 USD |
| sulumos | 1 | 0 | 0 | +1.96 USD |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | 3 | 2 | 0 | +1.93 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| BOOMBOYS.Kiritych | 2 | 1 | 0 | +1.22 USD |
| dauntlesswitness | 1 | 0 | 0 | +1.13 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 3 | 0 | +0.56 USD |
| Djdjdjekekek | 1 | 0 | 1 | +0.47 USD |
| theowalcott | 5 | 4 | 0 | -0.44 USD |
| ChonkyChocolateCake | 4 | 3 | 0 | -1.19 USD |
| predictionlegend | 3 | 3 | 0 | -2.50 USD |
| CORGI8 | 1 | 2 | 0 | -3.22 USD |
| SDTrading | 8 | 8 | 1 | -4.90 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616 | 1 | 2 | 0 | -5.33 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| Sassy-Bucket | 6 | 7 | 3 | -8.52 USD |
| SineNooneEI | 0 | 2 | 0 | -10.26 USD |
|  | 16 | 10 | 5 | -11.73 USD |
| HomeRunHazard | 36 | 20 | 0 | -12.70 USD |
| danielwolfmorales3pddb6dl6 | 7 | 10 | 1 | -21.92 USD |
| RN1 | 107 | 55 | 2 | -57.94 USD |

## Análisis general

- **Apuestas resueltas:** 673
- **Aciertos:** 434 (64.5%)
- **Cuota promedio de entrada:** 63.6%
- **Stake promedio:** $4.99
- **Total apostado (suma de stakes):** $3,360.45
- **ROI sobre lo apostado:** -1.00%
- **Comisiones pagadas (taker fee):** $61.15 (1.82% del capital apostado)
- **ROI que habría dado SIN comisiones:** +0.82% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 327 | 47.4% | 50.1% | -2.7 pp |
| 60-79% | 217 | 75.1% | 68.0% | +7.2 pp |
| 80-94% | 83 | 85.5% | 86.8% | -1.3 pp |
| 95-99% (casi seguro) | 46 | 97.8% | 97.2% | +0.6 pp |

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
| wta-swiatek-rybakin-2026-08-20 | RN1, danielwolfmorales3pddb6dl6, ferrariChampions2026 |
| dota2-ngx-flc-2026-08-20 | 0xF201A19b43471261A3c1Ba9247335d55270e527e-1763824114616, ChonkyChocolateCake, IMAREALPERSON |
| lol-koia-hrts-2026-08-20 | ChonkyChocolateCake, danielwolfmorales3pddb6dl6 |
| dota2-ironwi-boombo-2026-08-20 | Djdjdjekekek, Lakersfan111 |
| val-sen-2game-2026-08-20-game2 | Lakersfan111, casualbet2020, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-20-total-7pt5 | , RN1, Sassy-Bucket, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-20 | Djdjdjekekek, RN1, Sassy-Bucket, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-20-total-8pt5 | Sassy-Bucket, ferrariChampions2026 |
| atp-magadan-wong-2026-08-20 | , RN1, ferrariChampions2026 |
| sud-mac-san-2026-08-20-mac | RN1, ferrariChampions2026 |
| mlb-laa-hou-2026-08-20 | , ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
|  | Indiana Fever vs. Dallas Wings | Dallas Wings (BUY) | 99% | 5.00 | 3.0% | ⏳ pendiente | — |
| Djdjdjekekek | Dota 2: Iron Wing vs BoomBoys (BO3) - Th | BoomBoys (BUY) | 60% | 5.00 | 31.8% | ⏳ pendiente | — |
| Sassy-Bucket | Atlanta Dream vs. Los Angeles Sparks: O/ | Under (BUY) | 52% | 5.00 | 22.2% | ⏳ pendiente | — |
| Lakersfan111 | Dota 2: Iron Wing vs BoomBoys - Game 1 W | BoomBoys (BUY) | 54% | 5.00 | 2.4% | ⏳ pendiente | — |
|  | New York Yankees vs. Baltimore Orioles:  | Under (BUY) | 79% | 5.00 | 0.7% | ✅ ganada | +1.28 |
|  | Quebec City: Jacob Fearnley vs Alexis Ga | Jacob Fearnley (BUY) | 96% | 5.00 | 0.7% | ⏳ pendiente | — |
|  | Los Angeles Angels vs. Houston Astros | Los Angeles Angels (BUY) | 82% | 5.00 | 1.2% | ⏳ pendiente | — |
| Lakersfan111 | Counter-Strike: Legacy vs Team Falcons ( | Team Falcons (BUY) | 75% | 5.00 | 0.8% | ⏳ pendiente | — |
|  | Cancun: Alan Magadan vs Coleman Wong | Alan Magadan (BUY) | 42% | 5.00 | 5.2% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | Set Handicap: Fils (-1.5) vs Tirante (+1 | Tirante (BUY) | 49% | 5.00 | 33.4% | ⏳ pendiente | — |
| Djdjdjekekek | New York Yankees vs. Baltimore Orioles | New York Yankees (BUY) | 91% | 5.00 | 4.1% | 💰 vendida anticipada | +0.47 |
| Lakersfan111 | Games Total: O/U 2.5 | Under (BUY) | 51% | 5.00 | 1.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Los Angeles Angels vs. Houston Astros | Houston Astros (BUY) | 64% | 5.00 | 6.6% | ⏳ pendiente | — |
| ferrariChampions2026 | New York Yankees vs. Baltimore Orioles:  | Under (BUY) | 61% | 5.00 | 3.2% | ⏳ pendiente | — |
| ferrariChampions2026 | New York Yankees vs. Baltimore Orioles:  | Under (BUY) | 51% | 5.00 | 2.2% | ✅ ganada | +4.68 |
| ferrariChampions2026 | Connecticut Sun vs. Las Vegas Aces: O/U  | Over (BUY) | 48% | 5.00 | 0.7% | ⏳ pendiente | — |
| ferrariChampions2026 | New York Yankees vs. Baltimore Orioles:  | Over (BUY) | 51% | 5.00 | 7.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Indiana Fever vs. Dallas Wings: O/U 185. | Over (BUY) | 51% | 5.00 | 1.3% | ⏳ pendiente | — |
| Lakersfan111 | Counter-Strike: FUT Esports vs MOUZ (BO3 | MOUZ (BUY) | 60% | 5.00 | 2.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Connecticut Sun vs. Las Vegas Aces: O/U  | Under (BUY) | 50% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: KRÜ Esports vs Fluxo W7M - Map | KRÜ Esports (BUY) | 86% | 5.00 | 0.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Alan Magadan vs Coleman Wong | Coleman Wong (BUY) | 93% | 5.00 | 5.1% | ⏳ pendiente | — |
| ferrariChampions2026 | New York Yankees vs. Baltimore Orioles | Baltimore Orioles (BUY) | 54% | 5.00 | 3.9% | ❌ perdida | -5.12 |
| ferrariChampions2026 | Valorant: KRÜ Esports vs Fluxo W7M (BO3) | KRÜ Esports (BUY) | 71% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Iga Swiatek vs Elena Ry | Iga Swiatek (BUY) | 80% | 5.00 | 0.3% | ✅ ganada | +1.20 |
| RN1 | Will CSyD Macará win on 2026-08-20? | No (BUY) | 62% | 5.00 | 2.1% | ✅ ganada | +2.97 |
| ferrariChampions2026 | Will CSyD Macará win on 2026-08-20? | No (BUY) | 60% | 5.00 | 0.2% | ✅ ganada | +3.23 |
| RN1 | Will CSyD Macará win on 2026-08-20? | Yes (BUY) | 44% | 5.00 | 0.8% | ❌ perdida | -5.14 |
| Lakersfan111 | Counter-Strike: FUT Esports vs MOUZ - Ma | MOUZ (BUY) | 59% | 5.00 | 0.7% | ⏳ pendiente | — |
| Lakersfan111 | Dota 2: Team Yandex vs Nigma Galaxy (BO3 | Team Yandex (BUY) | 66% | 5.00 | 1.7% | ⏳ pendiente | — |
