# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 21:07:58 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $467.92
**Retorno acumulado:** -6.42%
**Peor caída desde un máximo (drawdown):** 25.62%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $218.25 en 44 posiciones abiertas (disponible para nuevas apuestas: $249.67)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 4 | 0 | 0 | +13.04 USD |
| sentrio | 4 | 2 | 1 | +9.13 USD |
| Lakersfan111 | 1 | 0 | 2 | +5.29 USD |
| SDTrading | 5 | 4 | 2 | +2.45 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| BOOMBOYS.Kiritych | 2 | 1 | 0 | +1.22 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 3 | 3 | 0 | +0.56 USD |
| dauntlesswitness | 0 | 0 | 1 | +0.00 USD |
| Satisfied | 1 | 1 | 1 | -0.25 USD |
| ChonkyChocolateCake | 1 | 1 | 0 | -0.44 USD |
| predictionlegend | 2 | 2 | 0 | -0.46 USD |
|  | 3 | 2 | 0 | -3.59 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 2 | -5.75 USD |
| HomeRunHazard | 33 | 16 | 7 | -5.88 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 3 | 3 | 1 | -6.79 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| theowalcott | 3 | 4 | 2 | -7.60 USD |
| Sassy-Bucket | 1 | 3 | 3 | -9.87 USD |
| RN1 | 71 | 36 | 10 | -19.78 USD |
| ferrariChampions2026 | 141 | 84 | 12 | -37.86 USD |

## Análisis general

- **Apuestas resueltas:** 479
- **Aciertos:** 311 (64.9%)
- **Cuota promedio de entrada:** 64.4%
- **Stake promedio:** $4.99
- **Total apostado (suma de stakes):** $2,392.20
- **ROI sobre lo apostado:** -1.38%
- **Comisiones pagadas (taker fee):** $42.64 (1.78% del capital apostado)
- **ROI que habría dado SIN comisiones:** +0.40% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 224 | 47.3% | 50.1% | -2.8 pp |
| 60-79% | 157 | 73.9% | 68.3% | +5.6 pp |
| 80-94% | 66 | 86.4% | 87.3% | -1.0 pp |
| 95-99% (casi seguro) | 32 | 100.0% | 97.2% | +2.8 pp |

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
| mlb-nyy-bal-2026-08-19 | HomeRunHazard, RN1, Satisfied, ferrariChampions2026 |
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
| mlb-lad-col-2026-08-19 | RN1, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | CR Flamengo vs. Cruzeiro EC: O/U 2.5 | Over (BUY) | 68% | 5.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Taylor Fritz vs Christo | Taylor Fritz (BUY) | 99% | 5.00 | 0.7% | ⏳ pendiente | — |
| RN1 | Will Los Angeles Galaxy win on 2026-08-1 | No (BUY) | 47% | 5.00 | 0.9% | ⏳ pendiente | — |
| RN1 | New York Yankees vs. Baltimore Orioles | New York Yankees (BUY) | 98% | 5.00 | 0.3% | ✅ ganada | +0.10 |
| RN1 | Will Portland Timbers win on 2026-08-19? | No (BUY) | 48% | 5.00 | 0.5% | ⏳ pendiente | — |
| HomeRunHazard | Athletics vs. Kansas City Royals | Athletics (BUY) | 82% | 5.00 | 1.5% | ⏳ pendiente | — |
| HomeRunHazard | Minnesota Lynx vs. Golden State Valkyrie | Under (BUY) | 49% | 5.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Will CR Flamengo win on 2026-08-19? | Yes (BUY) | 83% | 5.00 | 0.2% | ⏳ pendiente | — |
| RN1 | Los Angeles Dodgers vs. Colorado Rockies | Los Angeles Dodgers (BUY) | 82% | 5.00 | 1.0% | ⏳ pendiente | — |
| RN1 | Independiente Santa Fe vs. CA River Plat | Over (BUY) | 54% | 5.00 | 0.2% | ⏳ pendiente | — |
| RN1 | CR Flamengo vs. Cruzeiro EC: O/U 2.5 | Under (BUY) | 57% | 5.00 | 0.2% | ⏳ pendiente | — |
| HomeRunHazard | Los Angeles Angels vs. Houston Astros: O | Over (BUY) | 73% | 5.00 | 0.2% | ⏳ pendiente | — |
| HomeRunHazard | Minnesota Lynx vs. Golden State Valkyrie | Over (BUY) | 50% | 5.00 | 0.2% | ⏳ pendiente | — |
| Lakersfan111 | Game Handicap: BLG (-1.5) vs LGD Gaming  | LGD Gaming (BUY) | 45% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: G2 Esports vs M80 (BO3) - VCT  | G2 Esports (BUY) | 65% | 5.00 | 1.1% | ⏳ pendiente | — |
| Sassy-Bucket | Los Angeles Dodgers vs. Colorado Rockies | Under (BUY) | 53% | 5.00 | 19.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Madison Keys vs Xiyu Wa | Madison Keys (BUY) | 74% | 4.47 | 0.2% | ✅ ganada | +1.51 |
| ferrariChampions2026 | Will Inter Miami CF win on 2026-08-19? | No (BUY) | 65% | 5.00 | 0.4% | ⏳ pendiente | — |
| dauntlesswitness | Counter-Strike: Team Falcons vs TheMongo | Team Falcons (BUY) | 81% | 5.00 | 9.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Columbus Crew vs. CF Montréal: O/U 4.5 | Under (BUY) | 73% | 5.00 | 0.1% | ✅ ganada | +1.78 |
| ferrariChampions2026 | Valorant: G2 Esports vs M80 - Map 1 Winn | M80 (BUY) | 52% | 5.00 | 1.6% | ⏳ pendiente | — |
| danielwolfmorales3pddb6dl6 | LoL: Nongshim Red Force vs Kiwoom DRX (B | Kiwoom DRX (BUY) | 42% | 5.00 | 13.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Quebec City: Alexis Galarneau vs Dino Pr | Alexis Galarneau (BUY) | 56% | 5.00 | 0.2% | ✅ ganada | +3.82 |
| danielwolfmorales3pddb6dl6 | LoL: Dplus KIA Challengers vs DN SOOPers | DN SOOPers Challengers (BUY) | 43% | 5.00 | 25.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Toronto FC vs. Charlotte FC: O/U 1.5 | Over (BUY) | 96% | 5.00 | 0.2% | ✅ ganada | +0.20 |
| theowalcott | Montevideo City Torque vs. CA Tigre: O/U | Over (BUY) | 63% | 5.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Nuno Borges vs Brandon  | Brandon Nakashima (BUY) | 79% | 5.00 | 1.9% | ✅ ganada | +1.28 |
| ferrariChampions2026 | Set 1 Winner: Keys vs Wang | Wang (BUY) | 55% | 4.36 | 0.1% | ❌ perdida | -4.46 |
| ferrariChampions2026 | Valorant: G2 Esports vs M80 - Map 1 Winn | G2 Esports (BUY) | 69% | 5.00 | 3.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Will FC Cincinnati win on 2026-08-19? | No (BUY) | 49% | 5.00 | 0.5% | ❌ perdida | -5.13 |
