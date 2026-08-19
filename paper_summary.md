# Paper trading — resultado de la simulación

Actualizado: 2026-08-19 09:45:41 (hora de Perú)

**Bankroll inicial:** $500.00
**Bankroll actual:** $506.08
**Retorno acumulado:** +1.22%
**Peor caída desde un máximo (drawdown):** 8.51%
**Posiciones recortadas por el tope de seguridad (25% máx. por posición):** 0

**Modo de apuesta:** monto fijo de $5.00 por apuesta

**Filtro de cuota mínima:** solo se replican apuestas de 40% o más
**Comisión de Polymarket:** taker fee con coeficiente 0.05 (deportes) — se paga al entrar gane o pierda, y otra vez al vender anticipadamente. Mínimo de orden: 5 acciones.
**Slippage aplicado:** 2.0% — entramos siempre a peor precio que la ballena (su orden mueve el mercado y reaccionamos después). Sin esto la simulación sería optimista.
**Capital comprometido ahora mismo:** $440.00 en 88 posiciones abiertas (disponible para nuevas apuestas: $66.08)

_Todavía sin tope por mercado ni límite de pérdida — fase de solo medición._

## Por vigilado

| Apostador | Ganadas | Perdidas | Pendientes | Resultado simulado |
|---|---|---|---|---|
| swisstony | 29 | 1 | 1 | +41.97 USD |
| 0xcF609D3256f0f37f0595E5Dc64012Fa3a8fEa6f5-1771809916847 | 3 | 0 | 0 | +10.20 USD |
| RN1 | 10 | 3 | 21 | +4.55 USD |
| HomeRunHazard | 4 | 1 | 9 | +2.93 USD |
| HVAB | 1 | 0 | 0 | +1.03 USD |
| sentrio | 2 | 2 | 3 | +0.78 USD |
| 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436 | 0 | 0 | 4 | +0.00 USD |
| jtwyslljy | 0 | 0 | 1 | +0.00 USD |
| BOOMBOYS.Kiritych | 0 | 0 | 3 | +0.00 USD |
| Lakersfan111 | 0 | 0 | 2 | +0.00 USD |
| SDTrading | 0 | 0 | 3 | +0.00 USD |
| theowalcott | 1 | 1 | 0 | -1.43 USD |
| 0x3DFb153c197D4C19D3B31c1ecD2c7B6860eeabAf-1722957908185 | 2 | 3 | 1 | -4.12 USD |
| danielwolfmorales3pddb6dl6 | 1 | 2 | 0 | -5.75 USD |
| alaskabaked | 1 | 2 | 0 | -6.84 USD |
| Sassy-Bucket | 0 | 3 | 0 | -15.38 USD |
| ferrariChampions2026 | 80 | 48 | 40 | -21.80 USD |

## Análisis general

- **Apuestas resueltas:** 199
- **Aciertos:** 133 (66.8%)
- **Cuota promedio de entrada:** 64.8%
- **Stake promedio:** $5.00
- **Total apostado (suma de stakes):** $995.00
- **ROI sobre lo apostado:** +0.51%
- **Comisiones pagadas (taker fee):** $17.51 (1.76% del capital apostado)
- **ROI que habría dado SIN comisiones:** +2.27% _(referencia: cuánto pesan las comisiones)_

### ¿Aciertan más o menos de lo que promete la cuota?

_Si la cuota dice 70%, deberían ganar ~70% de esas apuestas. Ganar MENOS de lo que dice la cuota significa que la señal pierde plata a la larga._

| Rango de cuota | Apuestas | Acierto real | Cuota promedio | Diferencia |
|---|---|---|---|---|
| 40-59% | 90 | 46.7% | 49.8% | -3.1 pp |
| 60-79% | 65 | 76.9% | 68.5% | +8.4 pp |
| 80-94% | 31 | 90.3% | 87.0% | +3.3 pp |
| 95-99% (casi seguro) | 13 | 100.0% | 97.7% | +2.3 pp |

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
| chi-shp-ygb-2026-07-12-ygb | RN1, ferrariChampions2026 |
| atp-geerts-albot-2026-08-19 | RN1, ferrariChampions2026 |
| mlb-mia-phi-2026-08-19 | SDTrading, ferrariChampions2026 |
| cs2-fut-mgc-2026-08-19 | 0x547f2917D51F2e63ab382DCF641d4E0240162937-1782667852436, ferrariChampions2026 |
| atp-papoe-cosano-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| itf-ricci-panshin-2026-08-19 | RN1, ferrariChampions2026 |
| atp-durasov-poullai-2026-08-19 | HomeRunHazard, RN1, ferrariChampions2026 |
| itf-gniewko-pere-2026-08-19 | HVAB, RN1 |
| atp-almeida-tarvet-2026-08-19 | HomeRunHazard, ferrariChampions2026 |

## Últimas 30 apuestas de papel (detalle)

| Apostador | Mercado | Apostó a | Precio | Stake ($) | % real ballena | Estado | Resultado |
|---|---|---|---|---|---|---|---|
| ferrariChampions2026 | New York Yankees vs. Baltimore Orioles | New York Yankees (BUY) | 54% | 5.00 | 1.7% | ⏳ pendiente | — |
| SDTrading | Detroit Tigers vs. Pittsburgh Pirates | Detroit Tigers (BUY) | 41% | 5.00 | 20.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: G2 vs Astralis (BO3) - E | Astralis (BUY) | 46% | 5.00 | 0.2% | ⏳ pendiente | — |
| RN1 | ITF M25 Lesa Men: Stefano Reitano vs Fed | Federico Arnaboldi (BUY) | 58% | 5.00 | 0.7% | ⏳ pendiente | — |
| RN1 | Roehampton: Viktor Durasovic vs Lucas Po | Lucas Poullain (BUY) | 99% | 5.00 | 0.5% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Team WE vs EDward Gaming - Game 2 W | Team WE (BUY) | 89% | 5.00 | 1.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: G2 vs Astralis - Map 1 W | Astralis (BUY) | 63% | 5.00 | 1.6% | ⏳ pendiente | — |
| ferrariChampions2026 | St. Louis Cardinals vs. Cincinnati Reds | St. Louis Cardinals (BUY) | 43% | 5.00 | 4.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: FUT Esports vs magic (BO | magic (BUY) | 44% | 5.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: FUT Esports vs magic - M | magic (BUY) | 56% | 5.00 | 8.0% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: FUT Esports vs magic (BO | FUT Esports (BUY) | 59% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: FUT Esports vs magic - M | FUT Esports (BUY) | 46% | 5.00 | 1.3% | ⏳ pendiente | — |
| ferrariChampions2026 | LoL: Team WE vs EDward Gaming (BO3) - LP | EDward Gaming (BUY) | 52% | 5.00 | 1.1% | ⏳ pendiente | — |
| ferrariChampions2026 | Prague 2: Norbert Gombos vs Sean Cuenin | Norbert Gombos (BUY) | 52% | 5.00 | 1.4% | ⏳ pendiente | — |
| HomeRunHazard | Prague 2: Radu Mihai Papoe vs Javier Bar | Radu Mihai Papoe (BUY) | 97% | 5.00 | 4.9% | ⏳ pendiente | — |
| HomeRunHazard | Detroit Tigers vs. Pittsburgh Pirates: O | Under (BUY) | 54% | 5.00 | 5.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Prague 2: Norbert Gombos vs Sean Cuenin | Sean Cuenin (BUY) | 62% | 5.00 | 0.2% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: G2 vs Astralis - Map 1 W | G2 (BUY) | 45% | 5.00 | 3.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Counter-Strike: G2 vs Astralis (BO3) - E | G2 (BUY) | 65% | 5.00 | 4.0% | ⏳ pendiente | — |
| RN1 | Roehampton: Michael Geerts vs Radu Albot | Michael Geerts (BUY) | 69% | 5.00 | 9.6% | ⏳ pendiente | — |
| HomeRunHazard | Roehampton: Viktor Durasovic vs Lucas Po | Lucas Poullain (BUY) | 93% | 5.00 | 1.4% | ⏳ pendiente | — |
| ferrariChampions2026 | Roehampton: Michael Geerts vs Radu Albot | Michael Geerts (BUY) | 74% | 5.00 | 3.3% | ⏳ pendiente | — |
| ferrariChampions2026 | Map Handicap: G2 (-1.5) vs Astralis (+1. | Astralis (BUY) | 61% | 5.00 | 1.7% | ⏳ pendiente | — |
| HomeRunHazard | Sion: Lorenzo Giustino vs Henry Bernet | Lorenzo Giustino (BUY) | 78% | 5.00 | 2.2% | ⏳ pendiente | — |
| RN1 | Will FC Barcelona win on 2026-08-19? | Yes (BUY) | 88% | 5.00 | 0.4% | ⏳ pendiente | — |
| HomeRunHazard | Sion: Lorenzo Giustino vs Henry Bernet | Henry Bernet (BUY) | 49% | 5.00 | 1.5% | ⏳ pendiente | — |
| ferrariChampions2026 | Sion: Mika Brunold vs Calvin Hemery | Calvin Hemery (BUY) | 46% | 5.00 | 2.8% | ⏳ pendiente | — |
| SDTrading | Chicago White Sox vs. Chicago Cubs | Chicago White Sox (BUY) | 43% | 5.00 | 4.9% | ⏳ pendiente | — |
| ferrariChampions2026 | ITF W75 Kursumlijska Banja 3 Women: Beat | Beatrice Ricci (BUY) | 57% | 5.00 | 0.6% | ⏳ pendiente | — |
| RN1 | ITF M25 Idanha-a-Nova 2 Men: Vasco Leote | Vasco Leote Prata (BUY) | 62% | 5.00 | 0.9% | ⏳ pendiente | — |
