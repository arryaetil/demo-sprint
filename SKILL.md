---
name: demo-sprint
description: Onderzoek een bestaand klein bedrijf en maak of verbeter een overtuigende website-demo met echte inhoud, zorgvuldig ontwerp, browsercontrole en optionele Railway-publicatie. Gebruik bij een klant-URL met verzoeken als "maak een demo", "verbeter deze website" of bij werk aan een bestaande pitchdemo. Niet voor gewone onderhoudstaken zonder demo- of herontwerpdoel.
---

# Demo Sprint

Maak een demo die een eigenaar kan beoordelen: herkenbaar bedrijf, echt werk, duidelijke contactroute, één heldere ontwerpgedachte en een werkende preview. Gebruik dit als workflow, niet als toestemming om accounts, domeinen of live websites te wijzigen. Volg de actuele opdracht, bestaande afspraken en projectinstructies.

## 1. Onderzoek de bron

- Bekijk de bestaande website en alle relevante paginatypen: diensten, prijzen/PDF's, werkgebied, reviews, contact, openingstijden, team, projecten en juridische pagina's. Noteer bronlinks en onzekerheden. Controleer veranderlijke feiten opnieuw vlak voor publicatie.
- Maak een beeldinventaris met herkomst, kwaliteit, gebruiksrecht en functie. Onderscheid echte projectfoto's, stockbeeld en AI-bewerkingen. Hergebruik bedrijfsfoto's alleen met toestemming; respecteer licenties en verplichte naamsvermelding. Verwijder geen watermerken van materiaal zonder gebruiksrecht.
- Neem geen fictieve reviews, scores, aantallen, certificaten, garanties of prijzen op. Een gemiddelde beoordeling zegt niets over de sterren van een individuele review. Vraag bij tegenstrijdige brongegevens om bevestiging of label een waarde als indicatief.
- Bewaar de echte contactgegevens en links naar privacy- en cookiepagina's. Controleer of telefoon-, e-mail- en sociale profielen bij dit bedrijf horen.

## 2. Kies de richting

Toon eerst een korte **design read** met vier antwoorden: (1) wat moet de demo overbrengen, (2) wie is het bedrijf en wie zijn de klanten, (3) drie sfeerwoorden, (4) de ontwerpkeuze met TasteSkill-dials `VARIANCE`, `MOTION` en `DENSITY`. Geef concrete keuzes voor fotografie, typografie, kleur en compositie.

**Referentieonderzoek is een verplichte ontwerpstap.** Lees [references/design-and-build.md](references/design-and-build.md) volledig voordat je een nieuwe richting of groot herontwerp uitwerkt. Gebruik de volgende bronnen en noteer per gekozen patroon welke referentie welk ontwerpbesluit beïnvloedt:

- **TasteSkill / `design-taste-frontend`** voor design read, dials, ontwerpkritiek en de preflightcheck.
- **`design-md-library` en Awesome Design** (`awesome-design-md` en `awesome-design-skills`) om één of twee passende `DESIGN.md`/`SKILL.md` referenties te lezen en om te zetten naar een eigen, merkgebonden ontwerpsysteem.
- **Refero MCP** voor stijlrichtingen en sectiepatronen: zoek met `refero_search_styles` vanuit 3–5 invalshoeken en bekijk de beste 3 met `refero_get_style`; zoek schermen per relevante sectie met `refero_search_screens` en bekijk 3–6 volledige voorbeelden met `refero_get_screen_image`.
- **details.so** voor hero, navigatie, footer en overgangen; **designspells.com** voor één zorgvuldig gekozen interactiedetail.

Kopieer geen site of merkstijl letterlijk. Als een logo ontbreekt of zwak is, bied eerst concepten aan en wacht op de keuze voordat je het als merk gebruikt. Label een onbevestigd logo als concept.

## 3. Bouw de demo

- Werk in de bestaande stack als er een project is. Maak echte, taakgerichte pagina-inhoud; laat een tekst-herschrijfskill alleen de formulering verbeteren, niet de feiten veranderen.
- Gebruik de beste rechtmatig bruikbare afbeeldingen op passende resolutie. Geef beelden beschrijvende alt-tekst, afmetingen en lazy loading onder de eerste schermhoogte. Documenteer herkomst en beperkingen.
- Houd contact bereikbaar. Maak demoformulieren duidelijk herkenbaar als demo en verstuur zonder backend geen gegevens. Zet conceptstatus zichtbaar bovenaan en onderaan; zet demo's op `noindex` tenzij de gebruiker anders vraagt.
- Bouw met **TasteSkill / `design-taste-frontend`**. Gebruik **`emilkowal-animations`** (of beschikbaar equivalent) voor timing en feedback, en **`find-animation-opportunities` → `review-animations`** indien aanwezig. Kies bewust uit **GSAP, Lenis, Motion, anime.js, Magic UI, Kokonut UI, React Bits en Bklit** volgens de beslisregels in [references/design-and-build.md](references/design-and-build.md). Gebruik één animatie-engine per componentboom, maximaal 2–3 opvallende effecten per pagina en respecteer `prefers-reduced-motion`.
- Houd feitelijke claims, echte klantreacties en verplichte bronvermelding intact. Zet geen onbevestigd sociaal profiel online.

## 4. Controleer

- Doe de **TasteSkill preflight** en controleer tegen **Vercel Web Interface Guidelines**. Gebruik **Playwright CLI** of de beschikbare browserautomatisering voor desktop en mobiel, echte content, contrast, toetsenbordfocus, menu, formulieren, links, afbeeldingen, console en ontbrekende assets. Controleer lichte en donkere weergave als de demo beide heeft. Los gevonden fouten op voordat je publiceert.
- Het meegeleverde script `scripts/live_check.py` controleert een live URL op 1440 en 375 pixels, elk in licht en donker, en bewaart screenshots plus `report.json`. Voer vanaf de skillmap uit: `python3 scripts/live_check.py https://voorbeeld.nl --out qa-output`. Installeer Python Playwright en Chromium als ze ontbreken; het script zelf verandert de website niet.
- Controleer daarnaast handmatig wat het script niet kan bewijzen: of claims kloppen, of de beste foto gekozen is, of het formulier werkelijk niets verstuurt en of de demo de juiste indruk geeft.

## 5. Lever op

- Geef een lokale preview zodat de gebruiker kan meekijken. Zet code alleen naar een bestaande gekoppelde GitHub-branch als dat bij het project hoort; herschrijf nooit gepushte geschiedenis.
- Publiceer op Railway wanneer de huidige opdracht of eerdere toestemming dat omvat. Gebruik de Railway-tooling die in de omgeving beschikbaar is, controleer project en service, en verifieer de uiteindelijke URL. Publiceer geen geheimen of tokens in repo of logs.
- Rapporteer kort wat af is, waar de preview staat, welke bronnen/beelden toestemming of credit vereisen en welke punten nog door de eigenaar bevestigd moeten worden. Vermeld bij een concept uitdrukkelijk dat het geen officiële website is.

Deze workflow komt uit projectnotities. [references/design-and-build.md](references/design-and-build.md) bewaart de specifieke ontwerp- en toolkeuzes; de opdracht van de gebruiker gaat voor.
