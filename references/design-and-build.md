# Designworkflow en gereedschap voor demo-sprint

Dit is de uitvoerbare ontwerpstap van de skill. Doorloop hem bij iedere nieuwe bedrijfswebsite, demo en groot herontwerp. Een tool die niet beschikbaar is, vervang je door handmatig onderzoek met dezelfde uitkomst; sla de ontwerpbeslissing niet over en claim het toolgebruik niet. Controleer actuele documentatie en licenties voordat je externe code of beelden gebruikt.

## 1. Design read en designskills

Toon de opdrachtgever een tabel met vier antwoorden: **wat moet de demo overbrengen**, **wie is het bedrijf en wie zijn de klanten**, **drie sfeerwoorden**, en **welke ontwerprichting**. Formuleer die laatste met TasteSkill (`design-taste-frontend`) en de dials `VARIANCE`, `MOTION`, `DENSITY`. Maak daarna keuzes voor beeldgebruik, typografie, kleur, witruimte en compositie. Gebruik TasteSkill opnieuw voor de preflight voordat de demo wordt opgeleverd.

Gebruik **`design-md-library`** als aanwezig: lees één of twee passende merkgebonden `DESIGN.md`-voorbeelden vóór je stijlen schrijft. Richtingvoorbeelden uit de oorspronkelijke workflow: Stripe/Wise voor financiële helderheid, Airbnb voor woningdiensten, Apple/Notion voor rustige eenvoud en Nike/SpaceX voor uitgesproken energie. Vertaal principes naar het eigen bedrijf; neem geen logo, merkuitstraling of volledige layout over.

Gebruik **Awesome Design** expliciet als extra catalogus. De naam verwijst naar twee nuttige verzamelingen:

| Bron | Rol in de sprint |
| --- | --- |
| [VoltAgent / awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | Zoek passende `DESIGN.md`-voorbeelden; haal er kleurrollen, typografie, layout en componentregels uit. |
| [bergside / awesome-design-skills](https://github.com/bergside/awesome-design-skills) | Kies één passende ontwerp-skill of stijlfamilie; lees `SKILL.md` én de bijbehorende `DESIGN.md`. |

Maak hieruit een korte eigen stijlnotitie voor de demo: kleuren met functie, lettertypen en schaal, raster en ruimte, beeldstijl, hoeken, interacties en wat je bewust vermijdt. Laat de echte bedrijfsidentiteit voorgaan op de voorbeeldstijl.

## 2. Refero en visuele referenties

Gebruik [Refero](https://refero.design/) als de MCP-koppeling beschikbaar is. Zoek bij lokale bedrijven op **patroon**, niet alleen op branche.

1. Doe `refero_search_styles` vanuit 3–5 invalshoeken: sfeer, doelgroep, gewenste uitstraling en vergelijkbare merken. Bekijk de beste drie met `refero_get_style` als er resultaten zijn. Geeft stijlzoeken geen resultaten, ga door met schermzoeken en vermeld dat.
2. Doe `refero_search_screens` voor de secties die deze demo nodig heeft: hero, diensten, prijzen, reviews, werkwijze, galerij, contactformulier en footer. Bekijk de beste 3–6 volledige schermen met `refero_get_screen_image`.
3. Noteer per ontwerpbesluit de concrete referentie en wat je ervan gebruikt, bijvoorbeeld een reviewswand in plaats van een carrousel. Gebruik de referentie als inzicht, niet als kopie.

**Maak vóór de bouw een reference lock**, bijvoorbeeld: `primaire Refero-URL/UUID · waarom passend bij dit bedrijf · 3-5 te behouden trekken · typografie/kleur/ruimte/fotografierollen · 1-2 details uit andere bronnen · merkgebonden aanpassingen · wat je niet overneemt`. Zet in een beslislog per hoofdkeuze de bron en de reden. Zoek daadwerkelijk en inspecteer het schermbeeld; een vermelding van Refero in een rapport zonder toolresultaten is geen onderzoek. Na de bouw maak je screenshots van de eigen site naast de gekozen Refero-beelden, controleer je ritme, hiërarchie, beeldverhouding en mobiele weergave, en herstel je afwijkingen. Benader de kwaliteit en dominante compositietrekken nauwkeurig zonder een referentiesite te klonen.

Bekijk daarnaast [details.so](https://details.so/) voor hero, navigatie, footer en overgangen, en [Design Spells](https://designspells.com/) voor hoogstens één sterk interactiedetail. Als de gebruiker een eigen screenshot of ontwerp aanlevert, kan **`image-to-code`** helpen om die visueel te analyseren en nauwkeurig te implementeren. Genereer geen referentiebeelden wanneer de gebruiker die niet wil.

## 3. Logo, inhoud en bouw

Als een bestaand logo bruikbaar is, behoud het. Als er geen goed logo is en een nieuw logo binnen de opdracht valt, gebruik de aparte **[`logo-design`-skill](https://github.com/kaankiziltug/logo-design-skill/tree/main/skills/logo-design)**. De volgorde uit de oorspronkelijke workflow is: behoud herkenbare merkelementen, maak drie zwart-witconcepten, controleer de SVG's technisch, toon één conceptoverzicht, wacht op de keuze van de eigenaar en maak dan pas kleur- en monochrome varianten, faviconbestanden, een presentatiebord en een korte gebruiksgids. Gebruik op het presentatiebord de echte bedrijfsnaam en contactgegevens. Houd het als concept tot de eigenaar het goedkeurt; laat officieel gebruik pas volgen na controle van eventuele merkrechten. De `logo-design`-skill en zijn hulpscripts staan in de gelinkte repository; controleer de installatie op iedere computer.

Behoud een bruikbare bestaande stack; kies bij nieuwbouw een stack die bij de klanttaken en kosten past. Inventariseer eerst de eigen bedrijfsfoto's, kies die waar bruikbaar en rechtmatig, en gebruik pas daarna sfeerbeeld. Gebruik echte reviews; vermeld onzekerheden. `humanizer` mag formuleringen natuurlijker maken, maar geen feiten veranderen. Houd plaatsen en diensten in afzonderlijke lijsten. Gebruik één hoofdkleur als accent, een samenhangend systeem voor hoeken en een duidelijke contactroute. Bij klantbeheer volg je ook [productie en content](production-and-content.md).

## 4. Componenten en beweging: bewuste keuze

Kies eerst één **betekenisvolle interactie** die de bezoeker helpt, niet alleen beweging om de pagina minder statisch te laten lijken. Voor een klusbedrijf kan dat een filter op echte projecten, een voor/na-vergelijking met twee echte foto's, een keuzehulp voor diensten of een werkgebiedkaart zijn. Zonder echte projectgegevens kies je een eerlijke interactie rond de contactvraag. Test bediening met muis, aanraking en toetsenbord en houd een bruikbare weergave zonder JavaScript. Noteer de gekozen interactie in het opleverrapport.

Bekijk eerst of CSS en bestaande componenten volstaan. Gebruik `find-animation-opportunities` en daarna `review-animations` als die skills beschikbaar zijn; anders beoordeel je elk effect zelf op frequentie, doel, snelheid en functie. Gebruik `emilkowal-animations` of een equivalent voor easing, duur en feedback. Beweging moet hiërarchie, verhaal, feedback of status verduidelijken.

| Tool of library | Gebruik wanneer |
| --- | --- |
| [GSAP](https://gsap.com/) | Er echte, gecoördineerde tijdlijnen of scrollvertelling nodig zijn. |
| [Lenis](https://lenis.darkroom.engineering/) | De pagina bewust rond scrollvertelling is ontworpen; toets verminderde beweging en toetsenbordgebruik. |
| [Motion](https://motion.dev/) | React-componenten doelgerichte toestandswisselingen of gebaren nodig hebben. |
| [anime.js](https://animejs.com/) | Een lichtere animatie voor SVG, stagger of specifieke DOM-details past; kies dit óf GSAP voor die rol. |
| [Magic UI](https://magicui.design/docs/installation) | Eén passend, aanpasbaar React-detail de hiërarchie of interactie verbetert; installeer volgens de actuele officiële documentatie. |
| [Kokonut UI](https://kokonutui.com/) | Een component als basis past bij het gekozen ontwerpsysteem. |
| [React Bits](https://reactbits.dev/) | Een effect of component werkelijk bij het merk past; controleer licentie en performance. |
| Bklit | Alleen als er echte gegevens te visualiseren zijn; controleer de actuele bron en licentie vóór gebruik. |

Gebruik maximaal 2–3 opvallende effecten op een pagina. Laat twee animatie-engines niet hetzelfde element besturen. Respecteer `prefers-reduced-motion`; test prestaties en leesbaarheid op mobiel. Kopieer voorbeeldcomponenten niet blind: pas kleur, ritme, inhoud en toegankelijkheid aan het bedrijf aan.

## 5. Details en kwaliteitscontrole

- Gebruik voor een donker thema systeemvoorkeur plus een handmatige keuze; onthoud die keuze en voorkom een flits van het verkeerde thema. Controleer de header op 320–430 px.
- Toon bij prijzen vooral de verschillen. Toon echte klantreacties zonder een gemiddelde score aan iedere quote te hangen.
- Bij een **demo**: zorg voor zichtbare conceptstatus, `noindex`, een demoformulier dat niets verstuurt, correcte contactlinks en een passende deelafbeelding. Bij **productie**: maak formulieren echt werkend, controleer juridische pagina's en bepaal de indexeerstatus met de eigenaar.
- Doe de TasteSkill preflight en een audit met [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines). Controleer met [Playwright CLI](https://github.com/microsoft/playwright-cli) of beschikbare browsertools de desktop- en mobiele weergave, toetsenbord, focus, formulieren, menu, afbeeldingen, links, console en thema's.
- Gebruik daarnaast `scripts/live_check.py` voor screenshots en mechanische controles. Controleer bronclaims, beeldkeuze en de algemene indruk zelf.
- Doe na deze controle altijd de [SEO-eindronde](seo-final-pass.md).

De oorspronkelijke werknotities verwezen naar lokale scripts en machinepaden die niet in deze repository zitten. Deze skill gebruikt relatieve paden en alleen het meegeleverde controlescript.
