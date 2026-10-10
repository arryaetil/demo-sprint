# demo-sprint

Herbruikbare skill voor het onderzoeken, ontwerpen, controleren en opleveren van website-demo's voor kleine bedrijven. De workflow komt uit Arrya's notities en is aangepast voor gebruik op deze Mac met Codex of Claude Code.

De skill staat in [SKILL.md](SKILL.md). Uitgebreidere ontwerpkeuzes staan in [references/design-and-build.md](references/design-and-build.md). De optionele live-controle staat in [scripts/live_check.py](scripts/live_check.py).

De skill kan automatisch worden gekozen wanneer je om een pitchdemo of groot herontwerp vraagt, of expliciet worden aangeroepen als `demo-sprint`. Publicatie naar GitHub of Railway gebeurt alleen binnen de toestemming van de lopende opdracht.

## Lokaal gebruiken

Installeer de repository als map `demo-sprint` onder `~/.codex/skills/` voor Codex of `~/.claude/skills/` voor Claude Code. Op deze Mac zijn beide locaties gekoppeld aan dezelfde checkout, zodat latere updates uit GitHub op één plek kunnen worden opgehaald.

Voor de browsercontrole is Python Playwright met Chromium nodig. Het script is optioneel; de skill blijft bruikbaar zonder die dependency.
