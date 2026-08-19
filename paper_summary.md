# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 14:00:18 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $482.62
**Retorno acumulado:** -3.48%
**Peor caída desde un máximo (drawdown):** 15.31%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $451.62 en 91 posiciones abiertas (disponible para nuevas apuestas: $31.00)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 3 | 0 | 1 | +10.20 USD |
| Lakersfan111 | 1 | 0 | 1 | +5.29 USD |
| RN1 | 32 | 13 | 29 | +5.19 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| sentrio | 2 | 2 | 3 | +0.78 USD |
| SDTrading | 0 | 0 | 7 | +0.00 USD |
| Satisfied | 0 | 0 | 3 | +0.00 USD |
| predictionlegend | 0 | 0 | 4 | +0.00 USD |
| ChonkyChocolateCake | 0 | 0 | 2 | +0.00 USD |
| ic4cream | 0 | 0 | 1 | +0.00 USD |
|  | 0 | 0 | 1 | +0.00 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 1 | 1 | 5 | -0.22 USD |
| BOOMBOYS.Kiritych | 1 | 1 | 1 | -1.16 USD |
| HomeRunHazard | 12 | 4 | 16 | -1.43 USD |
| theowalcott | 1 | 1 | 0 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 1 | -4.12 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 0 | -5.75 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| Sassy-Bucket | 0 | 3 | 0 | -15.38 USD |
| ferrariChampions2026 | 103 | 62 | 15 | -40.36 USD |

## Análisis general

- **Apuestas resueltas:** 285
- **Aciertos:** 189 (66.3%)
- **Cuota promedio de entrada:** 65.9%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $1,425.00
- **ROI sobre lo apostado:** -1.29%
- **Comisiones pagadas (taker fee):** $24.33 (1.71% del capital apostado)
- **ROI que habría dado SIN comisiones:** +0.42% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 115 | 48.7% | 50.0% | -1.3 pp |
| 60-79% | 105 | 70.5% | 68.3% | +2.2 pp |
| 80-94% | 47 | 87.2% | 87.3% | -0.0 pp |
| 95-99% (casi seguro) | 18 | 100.0% | 97.6% | +2.4 pp |

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
| lal-mad-mala-2026-08-19-mad | ic4cream, swisstony |
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
| mlb-atl-min-2026-08-19 | RN1, SDTrading, Satisfied, ferrariChampions2026 |
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
| atp-kopp-hassan-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-det-pit-2026-08-19-total-7pt5 | HomeRunHazard, RN1 |
| wta-cirstea-pegula-2026-08-19 | HomeRunHazard, RN1 |
| mlb-sd-nym-2026-08-19 | HomeRunHazard, RN1 |
| wta-kostyuk-andreev-2026-08-19 | HomeRunHazard, RN1 |
| atp-tirante-mensik-2026-08-19 | HomeRunHazard, RN1 |
| wta-noskova-anisimo-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, RN1 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | Cincinnati Open: Linda Noskova vs Amanda | Linda Noskova (BUY) | 53% | 5.00 | 3.1% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Thiago Agustin Tirante  | Thiago Agustin Tirante (BUY) | 58% | 5.00 | 1.1% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Linda Noskova vs Amanda | Linda Noskova (BUY) | 51% | 5.00 | 0.4% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Sorana Cirstea vs Jessi | Sorana Cirstea (BUY) | 48% | 5.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Chicago White Sox vs. Chicago Cubs | Chicago Cubs (BUY) | 57% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | Chicago White Sox vs. Chicago Cubs | Chicago White Sox (BUY) | 48% | 5.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Alexander Zverev vs Tom | Alexander Zverev (BUY) | 80% | 5.00 | 0.7% | ⏳ pendiente | — |
| RN1 | Spread: Chicago Cubs (-1.5) | Chicago White Sox (BUY) | 59% | 5.00 | 1.5% | ⏳ pendiente | — |
| predictionlegend | ŠK Slovan Bratislava vs. NK Celje: O/U 2 | Under (BUY) | 50% | 5.00 | 45.9% | ⏳ pendiente | — |
|  | Kingston: Igor Ribeiro Marcondes vs Laut | Lautaro Midon (BUY) | 90% | 5.00 | 0.6% | ⏳ pendiente | — |
| RN1 | Detroit Tigers vs. Pittsburgh Pirates: O | Under (BUY) | 64% | 5.00 | 0.4% | ⏳ pendiente | — |
| RN1 | Atlanta Braves vs. Minnesota Twins: O/U  | Under (BUY) | 52% | 5.00 | 0.4% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Marta Kostyuk vs Mirra  | Marta Kostyuk (BUY) | 63% | 5.00 | 10.5% | ⏳ pendiente | — |
| predictionlegend | Will ŠK Slovan Bratislava win on 2026-08 | No (BUY) | 50% | 5.00 | 142.0% | ⏳ pendiente | — |
| predictionlegend | Spread: Club Atlético de Madrid (-1.5) | Málaga CF (BUY) | 55% | 5.00 | 130.7% | ⏳ pendiente | — |
| RN1 | FC Barcelona vs. AL Ahly SC (EGY): 1st H | Under (BUY) | 63% | 5.00 | 1.1% | ⏳ pendiente | — |
| HomeRunHazard | Detroit Tigers vs. Pittsburgh Pirates: O | Over (BUY) | 47% | 5.00 | 1.6% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Marta Kostyuk vs Mirra  | Mirra Andreeva (BUY) | 74% | 5.00 | 3.3% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Chicago Cubs (-2.5) | Chicago White Sox (BUY) | 72% | 5.00 | 1.2% | ⏳ pendiente | — |
| RN1 | Atlanta Braves vs. Minnesota Twins | Atlanta Braves (BUY) | 52% | 3.37 | 2.9% | ⏳ pendiente | — |
| RN1 | Atlanta Braves vs. Minnesota Twins | Minnesota Twins (BUY) | 49% | 5.00 | 1.6% | ⏳ pendiente | — |
| RN1 | ITF M15 Båstad Men: Alessandro Battiston | Alessandro Battiston (BUY) | 74% | 5.00 | 0.5% | ✅ ganada | +1.69 |
| HomeRunHazard | Cincinnati Open: Thiago Agustin Tirante  | Jakub Mensik (BUY) | 67% | 5.00 | 1.3% | ⏳ pendiente | — |
| RN1 | San Diego Padres vs. New York Mets | San Diego Padres (BUY) | 53% | 5.00 | 1.3% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Sorana Cirstea vs Jessi | Jessica Pegula (BUY) | 97% | 5.00 | 1.7% | ⏳ pendiente | — |
| RN1 | ITF M15 Båstad Men: Jonathan Mridha vs O | Jonathan Mridha (BUY) | 71% | 5.00 | 0.4% | ✅ ganada | +1.97 |
| HomeRunHazard | Cincinnati Open: Marta Kostyuk vs Mirra  | Mirra Andreeva (BUY) | 74% | 5.00 | 6.1% | ⏳ pendiente | — |
| HomeRunHazard | San Diego Padres vs. New York Mets | San Diego Padres (BUY) | 58% | 5.00 | 0.3% | ⏳ pendiente | — |
| RN1 | Spread: Pittsburgh Pirates (-2.5) | Detroit Tigers (BUY) | 76% | 5.00 | 1.0% | ⏳ pendiente | — |
| RN1 | Spread: San Diego Padres (-1.5) | New York Mets (BUY) | 63% | 5.00 | 0.6% | ⏳ pendiente | — |
