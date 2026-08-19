# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 12:13:23 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $476.06
**Retorno acumulado:** -4.79%
**Peor caída desde un máximo (drawdown):** 13.99%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $428.25 en 86 posiciones abiertas (disponible para nuevas apuestas: $47.81)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 3 | 0 | 1 | +10.20 USD |
| RN1 | 25 | 11 | 17 | +1.49 USD |
| HomeRunHazard | 10 | 2 | 14 | +1.23 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| sentrio | 2 | 2 | 3 | +0.78 USD |
| Lakersfan111 | 0 | 0 | 2 | +0.00 USD |
| SDTrading | 0 | 0 | 7 | +0.00 USD |
| Satisfied | 0 | 0 | 3 | +0.00 USD |
| predictionlegend | 0 | 0 | 1 | +0.00 USD |
| ChonkyChocolateCake | 0 | 0 | 2 | +0.00 USD |
| ic4cream | 0 | 0 | 1 | +0.00 USD |
| BOOMBOYS.Kiritych | 1 | 1 | 1 | -1.16 USD |
| theowalcott | 1 | 1 | 0 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 1 | -4.12 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 0 | 1 | 5 | -5.10 USD |
| jtwyslljy | 0 | 1 | 0 | -5.10 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 0 | -5.75 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| Sassy-Bucket | 0 | 3 | 0 | -15.38 USD |
| ferrariChampions2026 | 96 | 57 | 27 | -35.71 USD |

## Análisis general

- **Apuestas resueltas:** 258
- **Aciertos:** 171 (66.3%)
- **Cuota promedio de entrada:** 65.8%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $1,290.00
- **ROI sobre lo apostado:** -1.93%
- **Comisiones pagadas (taker fee):** $22.08 (1.71% del capital apostado)
- **ROI que habría dado SIN comisiones:** -0.22% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 108 | 45.4% | 50.0% | -4.6 pp |
| 60-79% | 89 | 74.2% | 68.3% | +5.9 pp |
| 80-94% | 44 | 88.6% | 87.2% | +1.4 pp |
| 95-99% (casi seguro) | 17 | 100.0% | 97.5% | +2.5 pp |

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
| mlb-atl-min-2026-08-19 | SDTrading, Satisfied, ferrariChampions2026 |
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
| atp-gombos-cuenin-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-det-pit-2026-08-19-total-8pt5 | HomeRunHazard, RN1, SDTrading |
| mlb-det-pit-2026-08-19 | HomeRunHazard, RN1, SDTrading, ferrariChampions2026 |
| mlb-nyy-bal-2026-08-19 | Satisfied, ferrariChampions2026 |
| atp-jodar-cobolli-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| mlb-ari-bos-2026-08-19-total-8pt5 | HomeRunHazard, SDTrading |
| wta-swiatek-parry-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| atp-kopp-hassan-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-det-pit-2026-08-19-total-7pt5 | HomeRunHazard, RN1 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| RN1 | ITF W15 Wanfercée-Baulet Women: Delia Ga | Margaux Maquet (BUY) | 99% | 5.00 | 1.2% | ⏳ pendiente | — |
| HomeRunHazard | Cincinnati Open: Rafael Jodar vs Flavio  | Flavio Cobolli (BUY) | 46% | 5.00 | 3.4% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Rafael Jodar vs Flavio  | Flavio Cobolli (BUY) | 42% | 5.00 | 7.2% | ⏳ pendiente | — |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | Counter-Strike: GamerLegion vs MOUZ (BO3 | MOUZ (BUY) | 80% | 5.00 | 11.3% | ⏳ pendiente | — |
| HomeRunHazard | Cirstea vs. Pegula: Match O/U 21.5 | Under (BUY) | 52% | 5.00 | 1.2% | ⏳ pendiente | — |
| HomeRunHazard | Quebec City: Duncan Chan vs Taro Daniel | Taro Daniel (BUY) | 73% | 5.00 | 0.6% | ⏳ pendiente | — |
| RN1 | Cincinnati Open: Sorana Cirstea vs Jessi | Jessica Pegula (BUY) | 72% | 5.00 | 0.8% | ⏳ pendiente | — |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | Counter-Strike: FURIA vs Aurora Gaming ( | FURIA (BUY) | 63% | 5.00 | 13.1% | ⏳ pendiente | — |
| RN1 | Detroit Tigers vs. Pittsburgh Pirates | Pittsburgh Pirates (BUY) | 61% | 5.00 | 0.8% | ⏳ pendiente | — |
| RN1 | Detroit Tigers vs. Pittsburgh Pirates: O | Over (BUY) | 50% | 5.00 | 1.8% | ⏳ pendiente | — |
| RN1 | Detroit Tigers vs. Pittsburgh Pirates: O | Over (BUY) | 53% | 5.00 | 1.8% | ⏳ pendiente | — |
| HomeRunHazard | Arizona Diamondbacks vs. Boston Red Sox: | Over (BUY) | 46% | 5.00 | 2.5% | ⏳ pendiente | — |
| RN1 | ITF M15 Båstad Men: Leo Borg vs Lucas Re | Leo Borg (BUY) | 93% | 5.00 | 0.3% | ⏳ pendiente | — |
| HomeRunHazard | Detroit Tigers vs. Pittsburgh Pirates: O | Over (BUY) | 57% | 5.00 | 8.3% | ⏳ pendiente | — |
| RN1 | Sion: Sandro Kopp vs Benjamin Hassan | Benjamin Hassan (BUY) | 90% | 5.00 | 1.3% | ✅ ganada | +0.53 |
| ic4cream | Will Club Atlético de Madrid win on 2026 | Yes (BUY) | 73% | 5.00 | 3.8% | ⏳ pendiente | — |
| RN1 | Sion: Sandro Kopp vs Benjamin Hassan | Sandro Kopp (BUY) | 69% | 5.00 | 2.2% | ❌ perdida | -5.08 |
| RN1 | ITF W35 Krakow Women: Marcelina Podlinsk | Dalila Jakupovic (BUY) | 91% | 5.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: BIG vs Unicorns Of Love Sexy Editio | Unicorns Of Love Sexy Edition (BUY) | 50% | 5.00 | 0.1% | ⏳ pendiente | — |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | Will Inter Miami CF win on 2026-08-19? | No (BUY) | 65% | 5.00 | 6.2% | ⏳ pendiente | — |
| HomeRunHazard | Roehampton: Mark Ceban vs Iliyan Radulov | Mark Ceban (BUY) | 96% | 5.00 | 4.3% | ✅ ganada | +0.20 |
| ferrariChampions2026 | Counter-Strike: Black Phoenix vs Bushido | Black Phoenix (BUY) | 85% | 5.00 | 0.5% | ⏳ pendiente | — |
| HomeRunHazard | Spread: Boston Red Sox (-1.5) | Arizona Diamondbacks (BUY) | 59% | 5.00 | 4.1% | ⏳ pendiente | — |
| ChonkyChocolateCake | LoL: Vitality.Bee vs Ici Japon Corp. Esp | Ici Japon Corp. Esport (BUY) | 51% | 5.00 | 5.6% | ⏳ pendiente | — |
| ChonkyChocolateCake | LoL: UCAM Esports Club vs Team Heretics  | UCAM Esports Club (BUY) | 51% | 5.00 | 11.5% | ⏳ pendiente | — |
| RN1 | Prague 2: Norbert Gombos vs Sean Cuenin | Norbert Gombos (BUY) | 78% | 5.00 | 1.8% | ⏳ pendiente | — |
| RN1 | ITF M25 Santander Men: Bernardo Munk Mes | Sergi Perez Contri (BUY) | 75% | 5.00 | 0.5% | ⏳ pendiente | — |
| RN1 | ITF M25 Ueberlingen Men: Moritz Hoffmann | Christian Djonov (BUY) | 51% | 5.00 | 1.0% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: UCAM Esports Club vs Team Heretics  | Team Heretics Academy (BUY) | 66% | 5.00 | 0.2% | ⏳ pendiente | — |
| HomeRunHazard | Prague 2: Norbert Gombos vs Sean Cuenin | Sean Cuenin (BUY) | 62% | 5.00 | 1.6% | ⏳ pendiente | — |
