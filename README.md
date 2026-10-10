# demo-sprint

Herbruikbare skill voor het onderzoeken, ontwerpen, controleren en opleveren van website-demo's voor kleine bedrijven. De repository werkt op verschillende computers met Codex of Claude Code; er zijn geen gebruikers- of projectpaden vastgelegd.

De skill staat in [SKILL.md](SKILL.md). Uitgebreidere ontwerpkeuzes staan in [references/design-and-build.md](references/design-and-build.md). De optionele live-controle staat in [scripts/live_check.py](scripts/live_check.py).

## Ontwerpworkflow

**Dit is de kern van demo-sprint:** eerst een TasteSkill design read met `VARIANCE`, `MOTION` en `DENSITY`, daarna gerichte referenties en pas dan bouwen. De skill gebruikt `design-md-library` en **Awesome Design** ([VoltAgent's DESIGN.md-bibliotheek](https://github.com/VoltAgent/awesome-design-md) en [Bergside's designskills](https://github.com/bergside/awesome-design-skills)) voor een passende stijlrichting. **Refero MCP** levert voorbeelden voor hero, prijzen, reviews, werkwijze en contact; **details.so** en **designspells.com** helpen bij afwerking. Per gekozen patroon legt de agent vast welke referentie eraan ten grondslag ligt.

Tijdens de bouw stuurt **TasteSkill / design-taste-frontend** het ontwerp. **Magic UI, Kokonut UI, React Bits en Bklit** zijn bewuste componentkeuzes; **GSAP, Lenis, Motion en anime.js** zijn opties voor gerichte beweging. De skill legt per library uit wanneer je die inzet en hoe je overbodige effecten voorkomt. Daarna volgen de TasteSkill preflight, **Vercel Web Interface Guidelines** en **Playwright** browsercontrole. Zie [de volledige ontwerpstappen](references/design-and-build.md).

De skill kan automatisch worden gekozen wanneer je om een pitchdemo of groot herontwerp vraagt, of expliciet worden aangeroepen als `demo-sprint`. Publicatie naar GitHub of Railway gebeurt alleen binnen de toestemming van de lopende opdracht.

## Lokaal gebruiken

Installeer de repository als map `demo-sprint` in de skillmap van je agent. De locatie van die map verschilt per tool en besturingssysteem. Alle verwijzingen **binnen** deze repository, zoals `scripts/live_check.py`, zijn relatief aan de repositorymap. Voer het controlescript vanuit die map uit:

```bash
python3 scripts/live_check.py https://voorbeeld.nl --out qa-output
```

Wie de skill in zowel Codex als Claude Code wil gebruiken, kan dezelfde checkout voor beide agents beschikbaar maken of de repository in beide skillmappen clonen. Haal latere wijzigingen met `git pull` op in de checkout die de agent gebruikt.

Voor de browsercontrole is Python Playwright met Chromium nodig. Het script is optioneel; de skill blijft bruikbaar zonder die dependency.
