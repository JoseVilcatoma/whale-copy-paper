# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 14:51:47 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $449.72
**Retorno acumulado:** -10.06%
**Peor caída desde un máximo (drawdown):** 17.99%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $371.62 en 75 posiciones abiertas (disponible para nuevas apuestas: $78.10)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 3 | 0 | 1 | +10.20 USD |
| Lakersfan111 | 1 | 0 | 1 | +5.29 USD |
| sentrio | 3 | 2 | 2 | +3.16 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 2 | 1 | 4 | +2.27 USD |
| BOOMBOYS.Kiritych | 2 | 1 | 0 | +1.22 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
|  | 1 | 0 | 3 | +0.53 USD |
| Satisfied | 0 | 0 | 3 | +0.00 USD |
| predictionlegend | 0 | 0 | 4 | +0.00 USD |
| ChonkyChocolateCake | 0 | 0 | 2 | +0.00 USD |
| ic4cream | 0 | 0 | 1 | +0.00 USD |
| SDTrading | 1 | 1 | 5 | -0.83 USD |
| theowalcott | 1 | 1 | 0 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 1 | -4.12 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 0 | -5.75 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| RN1 | 40 | 20 | 30 | -10.28 USD |
| Sassy-Bucket | 0 | 3 | 0 | -15.38 USD |
| HomeRunHazard | 15 | 9 | 8 | -19.49 USD |
| ferrariChampions2026 | 106 | 65 | 9 | -46.70 USD |

## Análisis general

- **Apuestas resueltas:** 320
- **Aciertos:** 208 (65.0%)
- **Cuota promedio de entrada:** 65.3%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $1,600.00
- **ROI sobre lo apostado:** -3.21%
- **Comisiones pagadas (taker fee):** $27.81 (1.74% del capital apostado)
- **ROI que habría dado SIN comisiones:** -1.47% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 133 | 45.1% | 49.9% | -4.8 pp |
| 60-79% | 119 | 72.3% | 68.1% | +4.2 pp |
| 80-94% | 49 | 87.8% | 87.4% | +0.3 pp |
| 95-99% (casi seguro) | 19 | 100.0% | 97.6% | +2.4 pp |

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
| lal-mad-mala-2026-08-19-mad | RN1, ic4cream, swisstony |
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
| lol-al-tes-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, ferrariChampions2026, jtwyslljy |
| atp-maxted-brady-2026-08-19 | RN1, ferrariChampions2026 |
| lol-we-edg-2026-08-19-game-handicap-away-1pt5 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, Lakersfan111 |
| atp-giustin-bernet-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-mia-phi-2026-08-19-total-8pt5 | 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185, HomeRunHazard |
| atp-molleke-jianu-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-atl-min-2026-08-19 | , RN1, SDTrading, Satisfied, ferrariChampions2026 |
| chi-shp-ygb-2026-07-12-ygb | RN1, ferrariChampions2026 |
| atp-geerts-albot-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-mia-phi-2026-08-19 | SDTrading, ferrariChampions2026 |
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
| mlb-ari-bos-2026-08-19-total-8pt5 | HomeRunHazard, SDTrading |
| wta-swiatek-parry-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| lal-mad-mala-2026-08-19-total-2pt5 | RN1, predictionlegend |
| atp-kopp-hassan-2026-08-19 | RN1, ferrariChampions2026 |
| lol-big1-use1-2026-08-19 | , ferrariChampions2026 |
| mlb-det-pit-2026-08-19-total-7pt5 | HomeRunHazard, RN1 |
| wta-cirstea-pegula-2026-08-19 | HomeRunHazard, RN1 |
| mlb-sd-nym-2026-08-19 | HomeRunHazard, RN1 |
| wta-kostyuk-andreev-2026-08-19 | HomeRunHazard, RN1 |
| atp-tirante-mensik-2026-08-19 | HomeRunHazard, RN1 |
| lal-mad-mala-2026-08-19-spread-home-1pt5 | RN1, predictionlegend |
| ucl-sba-cel1-2026-08-19-sba | RN1, predictionlegend |
| wta-noskova-anisimo-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, RN1 |
| atp-fils-minaur-2026-08-19 | , RN1 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | Will Club Atlético de Madrid win on 2026 | No (BUY) | 42% | 5.00 | 0.2% | ⏳ pendiente | — |
|  | Cincinnati Open: Arthur Fils vs Alex de  | Arthur Fils (BUY) | 61% | 5.00 | 1.4% | ⏳ pendiente | — |
| RN1 | San Diego Padres vs. New York Mets | New York Mets (BUY) | 92% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | Club Atlético de Madrid vs. Málaga CF: O | Over (BUY) | 91% | 5.00 | 0.4% | ⏳ pendiente | — |
| RN1 | Will ŠK Slovan Bratislava win on 2026-08 | Yes (BUY) | 79% | 5.00 | 1.2% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Arthur Fils vs Alex de  | Arthur Fils (BUY) | 59% | 5.00 | 4.9% | ⏳ pendiente | — |
|  | LoL: BIG vs Unicorns Of Love Sexy Editio | BIG (BUY) | 62% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | Spread: ŠK Slovan Bratislava (-1.5) | ŠK Slovan Bratislava (BUY) | 48% | 5.00 | 0.2% | ⏳ pendiente | — |
| RN1 | Club Atlético de Madrid vs. Málaga CF: O | Under (BUY) | 52% | 5.00 | 0.8% | ⏳ pendiente | — |
|  | Atlanta Braves vs. Minnesota Twins | Atlanta Braves (BUY) | 41% | 5.00 | 0.9% | ⏳ pendiente | — |
| RN1 | Will Club Atlético de Madrid vs. Málaga  | No (BUY) | 78% | 5.00 | 0.8% | ⏳ pendiente | — |
| RN1 | Will Málaga CF win on 2026-08-19? | No (BUY) | 90% | 5.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Spread: Club Atlético de Madrid (-1.5) | Club Atlético de Madrid (BUY) | 41% | 5.00 | 0.2% | ⏳ pendiente | — |
| RN1 | Club Atlético de Madrid vs. Málaga CF: O | Over (BUY) | 79% | 5.00 | 1.2% | ⏳ pendiente | — |
| RN1 | Will Club Atlético de Madrid win on 2026 | Yes (BUY) | 66% | 5.00 | 5.7% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Linda Noskova vs Amanda | Amanda Anisimova (BUY) | 57% | 5.00 | 6.5% | ⏳ pendiente | — |
| RN1 | NEC vs. FK Bodø/Glimt: O/U 3.5 | Under (BUY) | 59% | 5.00 | 0.9% | ⏳ pendiente | — |
| RN1 | Celtic FC vs. LASK Linz: Both Teams to S | Yes (BUY) | 62% | 5.00 | 0.4% | ⏳ pendiente | — |
| RN1 | Club Atlético de Madrid vs. Málaga CF: O | Over (BUY) | 58% | 5.00 | 0.4% | ⏳ pendiente | — |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | Cincinnati Open: Linda Noskova vs Amanda | Linda Noskova (BUY) | 53% | 5.00 | 3.1% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Thiago Agustin Tirante  | Thiago Agustin Tirante (BUY) | 58% | 5.00 | 4.5% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Linda Noskova vs Amanda | Linda Noskova (BUY) | 51% | 5.00 | 3.8% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Sorana Cirstea vs Jessi | Sorana Cirstea (BUY) | 48% | 5.00 | 0.3% | ❌ perdida | -5.13 |
| RN1 | Chicago White Sox vs. Chicago Cubs | Chicago Cubs (BUY) | 57% | 5.00 | 2.1% | ⏳ pendiente | — |
| RN1 | Chicago White Sox vs. Chicago Cubs | Chicago White Sox (BUY) | 48% | 5.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Alexander Zverev vs Tom | Alexander Zverev (BUY) | 80% | 5.00 | 3.6% | ⏳ pendiente | — |
| RN1 | Spread: Chicago Cubs (-1.5) | Chicago White Sox (BUY) | 59% | 5.00 | 1.5% | ⏳ pendiente | — |
| predictionlegend | ŠK Slovan Bratislava vs. NK Celje: O/U 2 | Under (BUY) | 50% | 5.00 | 45.9% | ⏳ pendiente | — |
|  | Kingston: Igor Ribeiro Marcondes vs Laut | Lautaro Midon (BUY) | 90% | 5.00 | 0.6% | ✅ ganada | +0.53 |
| RN1 | Detroit Tigers vs. Pittsburgh Pirates: O | Under (BUY) | 64% | 5.00 | 0.4% | ✅ ganada | +2.72 |
