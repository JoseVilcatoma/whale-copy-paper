# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 23:49:53 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $480.03
**Retorno acumulado:** -3.99%
**Peor caída desde un máximo (drawdown):** 25.62%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $95.00 en 19 posiciones abiertas (disponible para nuevas apuestas: $385.03)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| SDTrading | 7 | 4 | 0 | +11.47 USD |
| sentrio | 5 | 2 | 0 | +10.49 USD |
| Lakersfan111 | 1 | 0 | 2 | +5.29 USD |
| Satisfied | 2 | 1 | 0 | +5.26 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| BOOMBOYS.Kiritych | 2 | 1 | 0 | +1.22 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 3 | 0 | +0.56 USD |
| dauntlesswitness | 0 | 0 | 1 | +0.00 USD |
| theowalcott | 5 | 4 | 0 | -0.44 USD |
| ChonkyChocolateCake | 1 | 1 | 0 | -0.44 USD |
| predictionlegend | 2 | 2 | 0 | -0.46 USD |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | 1 | 1 | 0 | -3.51 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 4 | 3 | 0 | -4.18 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 2 | -5.75 USD |
| Sassy-Bucket | 3 | 4 | 0 | -6.36 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
|  | 4 | 3 | 2 | -7.15 USD |
| HomeRunHazard | 35 | 19 | 2 | -12.66 USD |
| RN1 | 84 | 41 | 8 | -27.23 USD |
| ferrariChampions2026 | 149 | 87 | 2 | -33.59 USD |

## Análisis general

- **Apuestas resueltas:** 527
- **Aciertos:** 345 (65.5%)
- **Cuota promedio de entrada:** 64.6%
- **Stake promedio:** $4.99
- **Total apostado (suma de stakes):** $2,630.45
- **ROI sobre lo apostado:** -0.80%
- **Comisiones pagadas (taker fee):** $46.56 (1.77% del capital apostado)
- **ROI que habría dado SIN comisiones:** +0.97% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 242 | 47.9% | 50.2% | -2.3 pp |
| 60-79% | 176 | 74.4% | 68.3% | +6.1 pp |
| 80-94% | 72 | 84.7% | 87.1% | -2.4 pp |
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

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | Dota 2: Iron Wing vs Team Spirit - Game  | Iron Wing (BUY) | 63% | 5.00 | 2.9% | ⏳ pendiente | — |
|  | Dota 2: Iron Wing vs Team Spirit (BO3) - | Team Spirit (BUY) | 69% | 5.00 | 0.5% | ⏳ pendiente | — |
|  | Dota 2: Iron Wing vs Team Spirit - Game  | Iron Wing (BUY) | 57% | 5.00 | 1.2% | ⏳ pendiente | — |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | Cincinnati Open: Aryna Sabalenka vs Sara | Sara Bejlek (BUY) | 75% | 5.00 | 9.3% | ✅ ganada | +1.60 |
| RN1 | ITF W15 Tianjin 3 Women: Rinko Matsuda v | Rinko Matsuda (BUY) | 79% | 5.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Los Angeles Dodgers vs. Colorado Rockies | Under (BUY) | 84% | 5.00 | 0.6% | ✅ ganada | +0.91 |
| 0x32b484581fc5606dE9C1e43AF4636b6Be9BC8B21-1774274303653 | Cincinnati Open: Aryna Sabalenka vs Sara | Aryna Sabalenka (BUY) | 56% | 5.00 | 1.4% | ❌ perdida | -5.11 |
| RN1 | Los Angeles Dodgers vs. Colorado Rockies | Colorado Rockies (BUY) | 45% | 5.00 | 0.9% | ❌ perdida | -5.14 |
|  | Cincinnati Open: Aryna Sabalenka vs Sara | Aryna Sabalenka (BUY) | 69% | 5.00 | 1.4% | ❌ perdida | -5.08 |
| RN1 | Cancun: Alan Magadan vs Alex Hernandez | Alan Magadan (BUY) | 71% | 5.00 | 1.3% | ✅ ganada | +1.97 |
| RN1 | Cincinnati Open: Aryna Sabalenka vs Sara | Aryna Sabalenka (BUY) | 82% | 5.00 | 1.7% | ❌ perdida | -5.04 |
| RN1 | Quebec City: Jacob Fearnley vs Mackenzie | Jacob Fearnley (BUY) | 97% | 5.00 | 0.4% | ✅ ganada | +0.15 |
| RN1 | Spread: Los Angeles Dodgers (-2.5) | Colorado Rockies (BUY) | 53% | 5.00 | 0.4% | ✅ ganada | +4.32 |
| RN1 | ITF W15 Tianjin 3 Women: Yidi Yang vs Ch | Chenting Zhu (BUY) | 44% | 5.00 | 0.6% | ⏳ pendiente | — |
| RN1 | Seattle Mariners vs. Milwaukee Brewers | Seattle Mariners (BUY) | 95% | 5.00 | 0.2% | ✅ ganada | +0.25 |
| RN1 | Los Angeles Galaxy vs. San Jose Earthqua | Over (BUY) | 46% | 5.00 | 0.6% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Jaime Faria vs Lorenzo  | Lorenzo Musetti (BUY) | 99% | 5.00 | 2.3% | ✅ ganada | +0.05 |
|  | Los Angeles Angels vs. Houston Astros | Houston Astros (BUY) | 76% | 5.00 | 0.6% | ✅ ganada | +1.52 |
| RN1 | Cincinnati Open: Frances Tiafoe vs Felix | Frances Tiafoe (BUY) | 66% | 5.00 | 6.0% | ✅ ganada | +2.49 |
| RN1 | Montevideo City Torque vs. CA Tigre: O/U | Under (BUY) | 72% | 5.00 | 0.4% | ✅ ganada | +1.87 |
| RN1 | Washington Nationals vs. Texas Rangers | Washington Nationals (BUY) | 99% | 5.00 | 2.1% | ✅ ganada | +0.05 |
| RN1 | Will Montevideo City Torque win on 2026- | Yes (BUY) | 86% | 5.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Cancun: Alan Magadan vs Alex Hernandez | Alex Hernandez (BUY) | 67% | 5.00 | 0.4% | ❌ perdida | -5.08 |
| RN1 | CR Flamengo vs. Cruzeiro EC: O/U 2.5 | Over (BUY) | 68% | 5.00 | 0.3% | ✅ ganada | +2.27 |
| RN1 | Cincinnati Open: Taylor Fritz vs Christo | Taylor Fritz (BUY) | 99% | 5.00 | 0.7% | ✅ ganada | +0.05 |
| RN1 | Will Los Angeles Galaxy win on 2026-08-1 | No (BUY) | 47% | 5.00 | 0.9% | ⏳ pendiente | — |
| RN1 | New York Yankees vs. Baltimore Orioles | New York Yankees (BUY) | 98% | 5.00 | 0.3% | ✅ ganada | +0.10 |
| RN1 | Will Portland Timbers win on 2026-08-19? | No (BUY) | 48% | 5.00 | 0.5% | ⏳ pendiente | — |
| HomeRunHazard | Athletics vs. Kansas City Royals | Athletics (BUY) | 82% | 5.00 | 1.5% | ❌ perdida | -5.04 |
| HomeRunHazard | Minnesota Lynx vs. Golden State Valkyrie | Under (BUY) | 49% | 5.00 | 0.3% | ⏳ pendiente | — |
