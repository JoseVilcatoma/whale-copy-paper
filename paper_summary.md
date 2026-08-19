# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 17:34:13 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $447.21
**Retorno acumulado:** -10.56%
**Peor caída desde un máximo (drawdown):** 25.62%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $348.25 en 70 posiciones abiertas (disponible para nuevas apuestas: $98.96)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 30 | 1 | 0 | +43.66 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 3 | 0 | 1 | +10.20 USD |
| SDTrading | 3 | 2 | 4 | +6.04 USD |
| Lakersfan111 | 1 | 0 | 1 | +5.29 USD |
| Satisfied | 1 | 0 | 2 | +4.88 USD |
| sentrio | 3 | 2 | 2 | +3.16 USD |
| ic4cream | 1 | 0 | 0 | +1.78 USD |
| BOOMBOYS.Kiritych | 2 | 1 | 0 | +1.22 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| ChonkyChocolateCake | 1 | 1 | 0 | -0.44 USD |
| predictionlegend | 2 | 2 | 0 | -0.46 USD |
| theowalcott | 1 | 1 | 2 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 1 | -4.12 USD |
|  | 1 | 1 | 3 | -4.62 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 0 | -5.75 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 2 | 3 | 2 | -7.99 USD |
| RN1 | 65 | 33 | 10 | -13.10 USD |
| Sassy-Bucket | 0 | 3 | 2 | -15.38 USD |
| HomeRunHazard | 17 | 11 | 13 | -22.08 USD |
| ferrariChampions2026 | 114 | 69 | 27 | -42.71 USD |

## Análisis general

- **Apuestas resueltas:** 389
- **Aciertos:** 251 (64.5%)
- **Cuota promedio de entrada:** 64.8%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $1,943.37
- **ROI sobre lo apostado:** -2.77%
- **Comisiones pagadas (taker fee):** $34.19 (1.76% del capital apostado)
- **ROI que habría dado SIN comisiones:** -1.01% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 175 | 46.3% | 50.1% | -3.8 pp |
| 60-79% | 133 | 71.4% | 68.3% | +3.2 pp |
| 80-94% | 54 | 88.9% | 87.7% | +1.2 pp |
| 95-99% (casi seguro) | 27 | 100.0% | 97.4% | +2.6 pp |

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
| mlb-det-pit-2026-08-19 | HomeRunHazard, RN1, SDTrading, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-19 | Satisfied, ferrariChampions2026 |
| atp-jodar-cobolli-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-ari-bos-2026-08-19-total-8pt5 | HomeRunHazard, SDTrading, ferrariChampions2026 |
| wta-swiatek-parry-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| lal-mad-mala-2026-08-19-total-2pt5 | RN1, predictionlegend |
| atp-kopp-hassan-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-ari-bos-2026-08-19-spread-home-1pt5 | HomeRunHazard, ferrariChampions2026 |
| mls-phi-mia-2026-08-19-mia | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, RN1 |
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
| mlb-ari-bos-2026-08-19-total-9pt5 | RN1, ferrariChampions2026 |
| wta-shnaide-rybakin-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-tor-tb-2026-08-19-total-7pt5 | HomeRunHazard, Sassy-Bucket, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| SDTrading | Spread: Cleveland Guardians (-1.5) | Cleveland Guardians (BUY) | 50% | 5.00 | 1.3% | ⏳ pendiente | — |
| SDTrading | San Francisco Giants vs. Cleveland Guard | Over (BUY) | 47% | 5.00 | 34.0% | ⏳ pendiente | — |
| Sassy-Bucket | Minnesota Lynx vs. Golden State Valkyrie | Over (BUY) | 47% | 5.00 | 0.7% | ⏳ pendiente | — |
| HomeRunHazard | Seattle Mariners vs. Milwaukee Brewers:  | Over (BUY) | 62% | 5.00 | 3.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Will SE Palmeiras win on 2026-08-19? | Yes (BUY) | 45% | 5.00 | 0.2% | ⏳ pendiente | — |
| HomeRunHazard | Miami Marlins vs. Philadelphia Phillies | Philadelphia Phillies (BUY) | 64% | 5.00 | 4.5% | ⏳ pendiente | — |
| HomeRunHazard | New York Yankees vs. Baltimore Orioles:  | Under (BUY) | 54% | 5.00 | 4.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Will Club Cerro Porteño win on 2026-08-1 | No (BUY) | 85% | 5.00 | 0.5% | ⏳ pendiente | — |
| HomeRunHazard | New York Yankees vs. Baltimore Orioles:  | Over (BUY) | 58% | 5.00 | 4.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Toronto Blue Jays vs. Tampa Bay Rays: O/ | Under (BUY) | 55% | 5.00 | 1.8% | ⏳ pendiente | — |
| HomeRunHazard | Athletics vs. Kansas City Royals: O/U 7. | Over (BUY) | 59% | 5.00 | 4.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Miami Marlins vs. Philadelphia Phillies: | Under (BUY) | 50% | 5.00 | 1.4% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Alexander Zverev vs Tom | Tommy Paul (BUY) | 88% | 5.00 | 7.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Spread: Miami Marlins (-1.5) | Philadelphia Phillies (BUY) | 71% | 5.00 | 0.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Alexander Zverev vs Tom | Tommy Paul (BUY) | 55% | 5.00 | 3.9% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: Cloud9 vs BESTIA (BO3) - VCT A | Cloud9 (BUY) | 42% | 5.00 | 0.6% | ⏳ pendiente | — |
| HomeRunHazard | Cancun: Alexandre Muller vs Coleman Wong | Coleman Wong (BUY) | 95% | 5.00 | 4.0% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Miami Marlins (-2.5) | Philadelphia Phillies (BUY) | 78% | 5.00 | 0.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: Cloud9 vs BESTIA - Map 2 Winne | Cloud9 (BUY) | 67% | 5.00 | 2.6% | ⏳ pendiente | — |
| ferrariChampions2026 | Miami Marlins vs. Philadelphia Phillies: | Over (BUY) | 52% | 5.00 | 0.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Club Cerro Porteño vs. SE Palmeiras: O/U | Under (BUY) | 65% | 5.00 | 0.8% | ⏳ pendiente | — |
| HomeRunHazard | Toronto Blue Jays vs. Tampa Bay Rays: O/ | Under (BUY) | 55% | 5.00 | 24.6% | ⏳ pendiente | — |
| Sassy-Bucket | Toronto Blue Jays vs. Tampa Bay Rays: O/ | Over (BUY) | 47% | 5.00 | 383.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Cancun: Otto Virtanen vs Moez Echargui | Moez Echargui (BUY) | 45% | 5.00 | 5.7% | ⏳ pendiente | — |
| ferrariChampions2026 | Valorant: Cloud9 vs BESTIA (BO3) - VCT A | BESTIA (BUY) | 52% | 5.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Diana Shnaider vs Elena | Elena Rybakina (BUY) | 94% | 5.00 | 2.7% | ⏳ pendiente | — |
| theowalcott | Will CA Mineiro win on 2026-08-19? | No (BUY) | 62% | 5.00 | 35.7% | ⏳ pendiente | — |
| theowalcott | CA Mineiro vs. Red Bull Bragantino: O/U  | Over (BUY) | 44% | 5.00 | 2.8% | ⏳ pendiente | — |
| ferrariChampions2026 | Cincinnati Open: Alexander Zverev vs Tom | Alexander Zverev (BUY) | 86% | 5.00 | 10.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Miami Marlins vs. Philadelphia Phillies: | Over (BUY) | 43% | 5.00 | 0.9% | ⏳ pendiente | — |
