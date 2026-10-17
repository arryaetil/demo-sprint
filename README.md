# demo-sprint

Herbruikbare skill om een bedrijfswebsite vanaf nul te bouwen of een bestaande website te herontwerpen: onderzoek, echte content, ontwerp, bouw, browsercontrole, beheerbare productie en een vaste SEO-eindronde. De repository werkt op verschillende computers met Codex of Claude Code; er zijn geen gebruikers- of projectpaden vastgelegd.

De workflow staat in [SKILL.md](SKILL.md). Gebruik [ontwerp en libraries](references/design-and-build.md), [productie en bewerkbare content](references/production-and-content.md) en [de verplichte SEO-eindronde](references/seo-final-pass.md) als uitvoerbare handleidingen. De optionele live-controle staat in [scripts/live_check.py](scripts/live_check.py).

## Van begin tot eind

1. Bepaal of het een demo of productieproject is, onderzoek de bedrijfssite en verzamel verifieerbare feiten. Gebruik beschikbare foto's van het bedrijf eerst; stock alleen als die ontbreken of op verzoek.
2. Onderzoek met Refero echte stijl- en schermreferenties, inspecteer beelden en leg één passende hoofdrichting vast in een reference lock. Lees de passende designskills en maak een eigen ontwerpsysteem.
3. Bouw tot die referentierichting zichtbaar terugkomt en voeg **minstens één betekenisvolle, geteste interactie** toe. Gebruik component- en animatielibraries waar ze functioneel passen. Voor een productieproject maak je klantcontent daadwerkelijk bewerkbaar via een passende beheerroute.
4. Test de interface, formulieren en mobiele weergave. Doe **daarna altijd de SEO-eindronde**; bij een demo blijft `noindex` intact.
5. Lever preview, bron- en beeldlijst, QA/SEO-rapport en zo nodig een beheerinstructie op. Bij outreach: onderzoek elk bedrijf apart, schrijf met `humanizer` een persoonlijke mail en toon de volledige tekst eerst aan de opdrachtgever. Publicatie en verzending volgen de opdracht.

## Ontwerpworkflow

**Dit is de kern van demo-sprint:** eerst een TasteSkill design read met `VARIANCE`, `MOTION` en `DENSITY`, daarna gerichte referenties en pas dan bouwen. De skill gebruikt `design-md-library` en **Awesome Design** ([VoltAgent's DESIGN.md-bibliotheek](https://github.com/VoltAgent/awesome-design-md) en [Bergside's designskills](https://github.com/bergside/awesome-design-skills)) voor een passende stijlrichting. **Refero MCP** levert voorbeelden voor hero, prijzen, reviews, werkwijze en contact; **details.so** en **designspells.com** helpen bij afwerking. Per gekozen patroon legt de agent vast welke referentie eraan ten grondslag ligt.

Tijdens de bouw stuurt **TasteSkill / design-taste-frontend** het ontwerp. **Magic UI, Kokonut UI, React Bits en Bklit** zijn bewuste componentkeuzes; **GSAP, Lenis, Motion en anime.js** zijn opties voor gerichte beweging. De skill legt per library uit wanneer je die inzet en hoe je overbodige effecten voorkomt. Daarna volgen de TasteSkill preflight, **Vercel Web Interface Guidelines** en **Playwright** browsercontrole. Zie [de volledige ontwerpstappen](references/design-and-build.md).

## Alle skills en hun repositories

Dit is de installatielijst voor jou en je partner. Een link opent de **bronrepository** of de betreffende skillmap. `demo-sprint` installeert deze andere skills niet automatisch.

| Skill of bron | Repository | Gebruik |
| --- | --- | --- |
| TasteSkill / `design-taste-frontend` | [tasteskill/tasteskill](https://github.com/tasteskill/tasteskill) | Design read, de drie dials, anti-patronen en preflight. De lokaal gebruikte variant kan afwijken van de huidige repo. |
| `design-md-library` | [Publieke design-md-skill](https://github.com/arumwu/design-md-skill) + [onderliggende Awesome DESIGN.md-bibliotheek](https://github.com/VoltAgent/awesome-design-md) | De oorspronkelijke notities geven geen verifieerbare repo voor de *exacte* skillnaam; dit is een functioneel publiek alternatief. |
| Awesome Design MD | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | Merkgebonden `DESIGN.md`-referenties. |
| Awesome Design Skills | [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) | `SKILL.md` + `DESIGN.md` per stijlrichting. |
| `image-to-code` | [tasteskill/tasteskill – image-to-code](https://github.com/tasteskill/tasteskill/tree/main/image-to-code) | Een visuele referentie analyseren en in code vertalen. |
| **`logo-design`** | **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill/tree/main/skills/logo-design)** | Bij ontbrekend of zwak logo: drie concepten, SVG-controle, keuze eigenaar, dan varianten en gebruiksgids. Dit is de repository van de scripts uit de oorspronkelijke workflow. |
| `humanizer` | [blader/humanizer](https://github.com/blader/humanizer) | Webtekst natuurlijker maken zonder feiten te wijzigen. |
| `emil-design-eng` | [emilkowalski/skills – emil-design-eng](https://github.com/emilkowalski/skills/tree/main/skills/emil-design-eng) | Interactie- en animatiekwaliteit. |
| `find-animation-opportunities` | [emilkowalski/skills – find-animation-opportunities](https://github.com/emilkowalski/skills/tree/main/skills/find-animation-opportunities) | Bepalen waar beweging nuttig is. |
| `review-animations` | [emilkowalski/skills – review-animations](https://github.com/emilkowalski/skills/tree/main/skills/review-animations) | Bestaande animaties beoordelen. |
| `emilkowal-animations` | [Emil Kowalski's publieke skillverzameling](https://github.com/emilkowalski/skills) | De lokaal aanwezige skill is een aparte variant; de exacte publieke bron daarvan is niet vastgesteld. Gebruik de gelinkte `emil-design-eng` als verifieerbaar alternatief. |
| `web-design-guidelines` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) + [richtlijnen](https://github.com/vercel-labs/web-interface-guidelines) | UI-, toegankelijkheids- en interactiecontrole. |
| `playwright-cli` | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli/tree/main/skills/playwright-cli) | Browsercontrole en screenshots. |
| `geo-optimizer-skill` | [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | Aanvullende audit voor AI-vindbaarheid in de laatste ronde, als beschikbaar. |

## Referenties en MCP

| Middel | Bron |
| --- | --- |
| Refero MCP | [Refero MCP](https://refero.design/mcp) voor zoekbare stijlen en schermen. |
| details.so | [details.so](https://details.so/) voor hero, navigatie, footer en overgangen. |
| Design Spells | [designspells.com](https://designspells.com/) voor een passend interactiedetail. |
| Google Search Console MCP | [AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc) voor echte zoek- en indexgegevens van een geverifieerde site. |
| Open SEO | [every-app/open-seo](https://github.com/every-app/open-seo) voor aanvullende SEO-audits en onderzoek; zelf hosten kan een betaalde data-API vereisen. |

Dit zijn diensten, MCP's of inspiratiebronnen, geen meegeleverde GitHub-skills. De stappen voor Refero staan in [references/design-and-build.md](references/design-and-build.md). De SEO-toepassing en voorwaarden staan in [references/seo-final-pass.md](references/seo-final-pass.md).

## Libraries en componenten: bronrepositories

| Middel | Repository | Rol |
| --- | --- | --- |
| Magic UI | [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | Animatie- en interfacecomponenten. |
| Kokonut UI | [kokonut-labs/kokonutui](https://github.com/kokonut-labs/kokonutui) | Interfacecomponenten. |
| React Bits | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | Interactieve React-componenten. |
| Bklit UI | [bklit/bklit-ui](https://github.com/bklit/bklit-ui) | Grafieken en datavisualisatie. |
| GSAP | [greensock/GSAP](https://github.com/greensock/GSAP) | Tijdlijnen en gerichte scrollanimatie. |
| Lenis | [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis) | Vloeiend scrollen bij echte scrollvertelling. |
| Motion | [motiondivision/motion](https://github.com/motiondivision/motion) | React-animaties en toestandswisselingen. |
| anime.js | [juliangarnier/anime](https://github.com/juliangarnier/anime) | Lichte DOM- en SVG-animaties. |
| Python Playwright | [microsoft/playwright-python](https://github.com/microsoft/playwright-python) | Motor achter het meegeleverde [live-controlescript](scripts/live_check.py). |

De volledige [ontwerpstappen en beslisregels](references/design-and-build.md) vertellen wanneer je deze middelen inzet. GitHub, Lovable en Railway zijn platforms voor overdracht en publicatie, geen skills of componentlibraries. Controleer per computer welke externe skills geïnstalleerd zijn; zeg niet dat een ontbrekende skill is uitgevoerd.

De skill kan automatisch worden gekozen wanneer je om een nieuwe bedrijfswebsite, pitchdemo of groot herontwerp vraagt, of expliciet worden aangeroepen als `demo-sprint`. Publicatie naar GitHub of Railway gebeurt alleen binnen de toestemming van de lopende opdracht.

De skillstructuur is aangescherpt met de [Anthropic skill-creator-richtlijnen](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md): de korte hoofdinstructie verwijst naar gerichte referenties en noemt toetsbare uitkomsten. De lokale skillvalidatie controleert de opbouw; een echte website moet daarna nog in de browser worden beoordeeld.

## Lokaal gebruiken

Installeer de repository als map `demo-sprint` in de skillmap van je agent. De locatie van die map verschilt per tool en besturingssysteem. Alle verwijzingen **binnen** deze repository, zoals `scripts/live_check.py`, zijn relatief aan de repositorymap. Voer het controlescript vanuit die map uit:

```bash
python3 scripts/live_check.py https://voorbeeld.nl --out qa-output
```

Wie de skill in zowel Codex als Claude Code wil gebruiken, kan dezelfde checkout voor beide agents beschikbaar maken of de repository in beide skillmappen clonen. Haal latere wijzigingen met `git pull` op in de checkout die de agent gebruikt.

Voor de browsercontrole is Python Playwright met Chromium nodig. Het script is optioneel; de skill blijft bruikbaar zonder die dependency.
