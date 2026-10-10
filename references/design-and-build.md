# Designworkflow en gereedschap voor demo-sprint

Dit is de uitvoerbare ontwerpstap van de skill. Doorloop hem bij iedere nieuwe demo en bij een groot herontwerp. Een tool die niet beschikbaar is, vervang je door handmatig onderzoek met dezelfde uitkomst; sla de ontwerpbeslissing niet over. Controleer actuele documentatie en licenties voordat je externe code of beelden gebruikt.

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

1. Doe `refero_search_styles` vanuit 3–5 invalshoeken: sfeer, doelgroep, gewenste uitstraling en vergelijkbare merken. Bekijk de beste drie met `refero_get_style`.
2. Doe `refero_search_screens` voor de secties die deze demo nodig heeft: hero, diensten, prijzen, reviews, werkwijze, galerij, contactformulier en footer. Bekijk de beste 3–6 volledige schermen met `refero_get_screen_image`.
3. Noteer per ontwerpbesluit de concrete referentie en wat je ervan gebruikt, bijvoorbeeld een reviewswand in plaats van een carrousel. Gebruik de referentie als inzicht, niet als kopie.

Bekijk daarnaast [details.so](https://details.so/) voor hero, navigatie, footer en overgangen, en [Design Spells](https://designspells.com/) voor hoogstens één sterk interactiedetail. Als de gebruiker een eigen screenshot of ontwerp aanlevert, kan **`image-to-code`** helpen om die visueel te analyseren en nauwkeurig te implementeren. Genereer geen referentiebeelden wanneer de gebruiker die niet wil.

## 3. Logo, inhoud en bouw

Als een bestaand logo bruikbaar is, behoud het. Als er geen goed logo is en een nieuw logo binnen de opdracht valt, gebruik `logo-design` als die skill aanwezig is: drie zwart-witconcepten, controle van de SVG's, één conceptoverzicht, dan keuze van de opdrachtgever; werk pas daarna varianten en een korte gebruiksgids uit. Houd het als concept tot de eigenaar het goedkeurt.

Bouw in de bestaande stack. Gebruik echte en rechtmatig bruikbare foto's en reviews; vermeld onzekerheden. `humanizer` mag formuleringen natuurlijker maken, maar geen feiten veranderen. Houd plaatsen en diensten in afzonderlijke lijsten. Gebruik één hoofdkleur als accent, een samenhangend systeem voor hoeken en een duidelijke contactroute.

## 4. Componenten en beweging: bewuste keuze

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
- Zorg voor zichtbare conceptstatus, `noindex`, een demoformulier dat niets verstuurt, echte juridische links, correcte contactlinks en een absolute `og:image`.
- Doe de TasteSkill preflight en een audit met [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines). Controleer met [Playwright CLI](https://github.com/microsoft/playwright-cli) of beschikbare browsertools de desktop- en mobiele weergave, toetsenbord, focus, formulieren, menu, afbeeldingen, links, console en thema's.
- Gebruik daarnaast `scripts/live_check.py` voor screenshots en mechanische controles. Controleer bronclaims, beeldkeuze en de algemene indruk zelf.

De oorspronkelijke werknotities verwezen naar lokale scripts en machinepaden die niet in deze repository zitten. Deze skill gebruikt relatieve paden en alleen het meegeleverde controlescript.
