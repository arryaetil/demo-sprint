# demo-sprint

Herbruikbare skill voor het onderzoeken, ontwerpen, controleren en opleveren van website-demo's voor kleine bedrijven. De repository werkt op verschillende computers met Codex of Claude Code; er zijn geen gebruikers- of projectpaden vastgelegd.

De skill staat in [SKILL.md](SKILL.md). Uitgebreidere ontwerpkeuzes staan in [references/design-and-build.md](references/design-and-build.md). De optionele live-controle staat in [scripts/live_check.py](scripts/live_check.py).

## Ontwerpworkflow

**Dit is de kern van demo-sprint:** eerst een TasteSkill design read met `VARIANCE`, `MOTION` en `DENSITY`, daarna gerichte referenties en pas dan bouwen. De skill gebruikt `design-md-library` en **Awesome Design** ([VoltAgent's DESIGN.md-bibliotheek](https://github.com/VoltAgent/awesome-design-md) en [Bergside's designskills](https://github.com/bergside/awesome-design-skills)) voor een passende stijlrichting. **Refero MCP** levert voorbeelden voor hero, prijzen, reviews, werkwijze en contact; **details.so** en **designspells.com** helpen bij afwerking. Per gekozen patroon legt de agent vast welke referentie eraan ten grondslag ligt.

Tijdens de bouw stuurt **TasteSkill / design-taste-frontend** het ontwerp. **Magic UI, Kokonut UI, React Bits en Bklit** zijn bewuste componentkeuzes; **GSAP, Lenis, Motion en anime.js** zijn opties voor gerichte beweging. De skill legt per library uit wanneer je die inzet en hoe je overbodige effecten voorkomt. Daarna volgen de TasteSkill preflight, **Vercel Web Interface Guidelines** en **Playwright** browsercontrole. Zie [de volledige ontwerpstappen](references/design-and-build.md).

## Compleet overzicht van genoemde middelen

Dit overzicht is ook de checklist voor een partner die de skill op een andere computer gebruikt. `demo-sprint` is de workflow; de genoemde externe skills, diensten en libraries worden niet automatisch meegeleverd of geïnstalleerd.

| Soort | Namen | Rol |
| --- | --- | --- |
| Ontwerpsturing | **TasteSkill / `design-taste-frontend`** | Design read, `VARIANCE`/`MOTION`/`DENSITY`, anti-patronen en preflight. |
| Designsystemen | **`design-md-library`**, **[Awesome Design MD](https://github.com/VoltAgent/awesome-design-md)**, **[Awesome Design Skills](https://github.com/bergside/awesome-design-skills)** | Eén of twee passende `DESIGN.md`/`SKILL.md`-referenties lezen en vertalen naar een eigen merkstijl. |
| Visuele referenties | **[Refero](https://refero.design/) MCP**, **[details.so](https://details.so/)**, **[Design Spells](https://designspells.com/)**, **`image-to-code`** | Sectiepatronen, afwerking en eventueel analyse van een door de opdrachtgever aangeleverde afbeelding. |
| Logo | **`logo-design`** | Als het bedrijf geen bruikbaar logo heeft: drie zwart-witconcepten, vectorcontrole, keuze door eigenaar, daarna varianten en gebruiksgids. Deze skill is een aparte dependency. |
| Tekst | **`humanizer`** | Natuurlijke webtekst zonder nieuwe claims of gewijzigde feiten. |
| Animatieskills | **`emilkowal-animations` / `emil-design-eng`**, **`find-animation-opportunities`**, **`review-animations`** | Beslissen waar beweging helpt en duur, easing en feedback beoordelen. |
| Componenten | **[Magic UI](https://magicui.design/)**, **[Kokonut UI](https://kokonutui.com/)**, **[React Bits](https://reactbits.dev/)**, **Bklit** | Selectief een passend component of dataweergave inzetten. |
| Animatielibraries | **[GSAP](https://gsap.com/)**, **[Lenis](https://lenis.darkroom.engineering/)**, **[Motion](https://motion.dev/)**, **[anime.js](https://animejs.com/)** | Alleen bij een concreet doel; één animatie-engine per componentboom. |
| Controle | **[Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines) / `web-design-guidelines`**, **[Playwright CLI](https://github.com/microsoft/playwright-cli)**, **Python Playwright**, **`scripts/live_check.py`** | Ontwerp-, toegankelijkheids- en browsercontrole. |
| Oplevering | **GitHub**, **Lovable** (als de demo daar vandaan komt), **Railway** (bij publicatie) | Code overdragen en de demo bereikbaar maken. |

De stappen en beslisregels per middel staan in [references/design-and-build.md](references/design-and-build.md). Sommige namen komen uit de oorspronkelijke projectworkflow en zijn mogelijk niet op de computer van de partner geïnstalleerd. Controleer de aanwezigheid voordat je ze gebruikt; claim niet dat een ontbrekende skill is uitgevoerd.

De skill kan automatisch worden gekozen wanneer je om een pitchdemo of groot herontwerp vraagt, of expliciet worden aangeroepen als `demo-sprint`. Publicatie naar GitHub of Railway gebeurt alleen binnen de toestemming van de lopende opdracht.

## Lokaal gebruiken

Installeer de repository als map `demo-sprint` in de skillmap van je agent. De locatie van die map verschilt per tool en besturingssysteem. Alle verwijzingen **binnen** deze repository, zoals `scripts/live_check.py`, zijn relatief aan de repositorymap. Voer het controlescript vanuit die map uit:

```bash
python3 scripts/live_check.py https://voorbeeld.nl --out qa-output
```

Wie de skill in zowel Codex als Claude Code wil gebruiken, kan dezelfde checkout voor beide agents beschikbaar maken of de repository in beide skillmappen clonen. Haal latere wijzigingen met `git pull` op in de checkout die de agent gebruikt.

Voor de browsercontrole is Python Playwright met Chromium nodig. Het script is optioneel; de skill blijft bruikbaar zonder die dependency.
