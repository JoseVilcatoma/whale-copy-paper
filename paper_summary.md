# Paper trading — resultado de la simulación

Actualizado: 2026-08-20 03:14:43 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $482.64
**Retorno acumulado:** -3.47%
**Peor caída desde un máximo (drawdown):** 25.62%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $125.00 en 25 posiciones abiertas (disponible para nuevas apuestas: $357.64)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| SDTrading | 7 | 4 | 0 | +11.47 USD |
| Lakersfan111 | 2 | 0 | 1 | +10.80 USD |
| sentrio | 5 | 2 | 0 | +10.49 USD |
| Satisfied | 2 | 1 | 0 | +5.26 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| BOOMBOYS.Kiritych | 2 | 1 | 0 | +1.22 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 3 | 0 | +0.56 USD |
| dauntlesswitness | 0 | 0 | 1 | +0.00 USD |
| SineNooneEI | 0 | 0 | 1 | +0.00 USD |
| theowalcott | 5 | 4 | 0 | -0.44 USD |
| ChonkyChocolateCake | 1 | 1 | 0 | -0.44 USD |
| predictionlegend | 2 | 2 | 0 | -0.46 USD |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | 1 | 1 | 3 | -3.51 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 4 | 3 | 0 | -4.18 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 2 | -5.75 USD |
| Sassy-Bucket | 3 | 4 | 0 | -6.36 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
|  | 5 | 4 | 4 | -10.09 USD |
| HomeRunHazard | 36 | 20 | 0 | -12.70 USD |
| RN1 | 91 | 43 | 2 | -24.64 USD |
| ferrariChampions2026 | 150 | 88 | 11 | -36.07 USD |

## Análisis general

- **Apuestas resueltas:** 543
- **Aciertos:** 356 (65.6%)
- **Cuota promedio de entrada:** 64.6%
- **Stake promedio:** $4.99
- **Total apostado (suma de stakes):** $2,710.45
- **ROI sobre lo apostado:** -0.68%
- **Comisiones pagadas (taker fee):** $47.99 (1.77% del capital apostado)
- **ROI que habría dado SIN comisiones:** +1.10% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 249 | 47.8% | 50.2% | -2.4 pp |
| 60-79% | 182 | 74.7% | 68.4% | +6.3 pp |
| 80-94% | 75 | 85.3% | 87.1% | -1.7 pp |
| 95-99% (casi seguro) | 37 | 100.0% | 97.2% | +2.8 pp |

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
| wta-sabalen-bejlek-2026-08-19 | , 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653, RN1 |
| dota2-ironwi-ts8-2026-08-19-game2 | , ferrariChampions2026 |
| dota2-vsn2-boombo-2026-08-20-game1 | , ferrariChampions2026 |
| dota2-vsn2-boombo-2026-08-20 | , ferrariChampions2026 |
| lol-dk-hle1-2026-08-20-game1 | SineNooneEI, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | LoL: Dplus KIA vs Hanwha Life Esports -  | Hanwha Life Esports (BUY) | 50% | 5.00 | 1.3% | ⏳ pendiente | — |
| SineNooneEI | LoL: Dplus KIA vs Hanwha Life Esports -  | Dplus KIA (BUY) | 52% | 5.00 | 108.8% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Dplus KIA vs Hanwha Life Esports -  | Dplus KIA (BUY) | 51% | 5.00 | 5.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Dota 2: TEAM VISION vs BoomBoys - Game 2 | TEAM VISION (BUY) | 66% | 5.00 | 2.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Atlanta Dream (-8.5) | Los Angeles Sparks (BUY) | 47% | 5.00 | 0.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Las Vegas Aces (-14.5) | Las Vegas Aces (BUY) | 48% | 5.00 | 0.8% | ⏳ pendiente | — |
|  | Spread: KAA Gent (-1.5) | Hibernian FC (BUY) | 68% | 5.00 | 0.8% | ⏳ pendiente | — |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | Sion: Tommaso Compagnucci vs Juan Manuel | Tommaso Compagnucci (BUY) | 56% | 5.00 | 16.9% | ⏳ pendiente | — |
|  | Dota 2: TEAM VISION vs BoomBoys (BO3) -  | TEAM VISION (BUY) | 90% | 5.00 | 0.8% | ⏳ pendiente | — |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | Prague 2: Norbert Gombos vs Radu Mihai P | Norbert Gombos (BUY) | 42% | 5.00 | 24.5% | ⏳ pendiente | — |
|  | ITF M25 Taipei Men: Yu Hsiou Hsu vs Kuan | Yu Hsiou Hsu (BUY) | 97% | 5.00 | 6.9% | ⏳ pendiente | — |
| RN1 | ITF W15 Tianjin 3 Women: Tiana Tian Deng | Peangtarn Plipuech (BUY) | 73% | 5.00 | 4.3% | ✅ ganada | +1.78 |
| ferrariChampions2026 | Dota 2: TEAM VISION vs BoomBoys (BO3) -  | TEAM VISION (BUY) | 58% | 5.00 | 3.1% | ⏳ pendiente | — |
|  | Dota 2: TEAM VISION vs BoomBoys - Game 1 | TEAM VISION (BUY) | 62% | 5.00 | 2.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Games Total: O/U 2.5 | Under (BUY) | 58% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Dota 2: TEAM VISION vs BoomBoys - Game 1 | BoomBoys (BUY) | 42% | 5.00 | 7.7% | ⏳ pendiente | — |
| ferrariChampions2026 | ITF M25 Ueberlingen Men: Tim Handel vs A | Tim Handel (BUY) | 51% | 5.00 | 0.7% | ⏳ pendiente | — |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | Cincinnati Open: Amanda Anisimova vs Jes | Amanda Anisimova (BUY) | 45% | 5.00 | 3.7% | ⏳ pendiente | — |
| RN1 | ITF M15 Maanshan 7 Men: Weiyi Kong vs M  | M Rifqi Fitriadi (BUY) | 79% | 5.00 | 1.5% | ✅ ganada | +1.28 |
| ferrariChampions2026 | Dota 2: TEAM VISION vs BoomBoys - Game 1 | TEAM VISION (BUY) | 66% | 5.00 | 8.3% | ⏳ pendiente | — |
| RN1 | ITF W15 Tianjin 3 Women: Dabin Kim vs Me | Meng Yi Chen (BUY) | 90% | 5.00 | 2.1% | ✅ ganada | +0.53 |
| ferrariChampions2026 | Dota 2: Iron Wing vs Team Spirit - Game  | Team Spirit (BUY) | 65% | 5.00 | 0.6% | ✅ ganada | +2.61 |
| ferrariChampions2026 | Dota 2: Iron Wing vs Team Spirit - Game  | Iron Wing (BUY) | 63% | 5.00 | 2.9% | ❌ perdida | -5.09 |
|  | Dota 2: Iron Wing vs Team Spirit (BO3) - | Team Spirit (BUY) | 69% | 5.00 | 0.5% | ✅ ganada | +2.17 |
|  | Dota 2: Iron Wing vs Team Spirit - Game  | Iron Wing (BUY) | 57% | 5.00 | 1.2% | ❌ perdida | -5.11 |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | Cincinnati Open: Aryna Sabalenka vs Sara | Sara Bejlek (BUY) | 75% | 5.00 | 9.3% | ✅ ganada | +1.60 |
| RN1 | ITF W15 Tianjin 3 Women: Rinko Matsuda v | Rinko Matsuda (BUY) | 79% | 5.00 | 0.3% | ✅ ganada | +1.28 |
| RN1 | Los Angeles Dodgers vs. Colorado Rockies | Under (BUY) | 84% | 5.00 | 0.6% | ✅ ganada | +0.91 |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | Cincinnati Open: Aryna Sabalenka vs Sara | Aryna Sabalenka (BUY) | 56% | 5.00 | 1.4% | ❌ perdida | -5.11 |
| RN1 | Los Angeles Dodgers vs. Colorado Rockies | Colorado Rockies (BUY) | 45% | 5.00 | 0.9% | ❌ perdida | -5.14 |
