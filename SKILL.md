---
name: demo-sprint
description: Onderzoek, ontwerp, bouw en controleer een complete bedrijfswebsite vanaf nul of op basis van een bestaande site. Gebruik bij website-demo's, grote herontwerpen en productieklare bedrijfssites; inclusief echte content en beelden, Refero-onderzoek, passende designskills, bewerkbare content waar nodig, browsercontrole en een vaste SEO-eindronde. Niet voor kleine onderhoudswijzigingen.
---

# Demo Sprint

Bouw een website die bij het echte bedrijf past en door de opdrachtgever beoordeeld kan worden. Deze skill is een workflow, geen automatische toestemming voor publicatie, accountwijzigingen of berichten aan derden. Volg de actuele opdracht en projectinstructies. Gebruik externe skills, MCP's en libraries alleen als ze beschikbaar en passend zijn; zeg eerlijk wanneer een middel niet is gebruikt. De [README](README.md) geeft van elk middel de bronrepository.

## 1. Bepaal doel en oplevervorm

- Bepaal of de opdracht een nieuwe site, herontwerp of pitchdemo is. Leg doelgroep, conversiedoel, pagina's, merk, budget, gewenste preview en publicatiekanaal vast. Maak een eerste preview vóór outreach of livegang als de opdrachtgever die wil zien.
- Kies expliciet tussen **demo** en **productie**. Een demo krijgt duidelijke conceptstatus, `noindex` en geen schijnbaar werkend formulier. Productie vereist werkende contactstromen, inhoudsbeheer waar gevraagd, beheerrollen, privacy, beveiliging en herstelbaarheid. Lees voor productie [references/production-and-content.md](references/production-and-content.md).
- Onderzoek bij een bestaande site de relevante pagina's, socials, diensten, werkgebied, reviews, team, prijzen, projecten, contact en juridische informatie. Bij een nieuw bedrijf vraag je ontbrekende feiten of markeer je ze als concept. Houd bronlinks en onzekerheden bij.

## 2. Verzamel echte inhoud en beeld

- Maak eerst een inventaris van **foto's op de eigen bedrijfssite** en door de eigenaar aangeleverde beelden. Kies die voor diensten, projecten en over-ons als de kwaliteit en rechten volstaan. Gebruik stock of gegenereerd sfeerbeeld alleen als er geen bruikbaar echt beeld is, of als de opdrachtgever dat wil. Vermeld het onderscheid in de beeldlijst.
- Controleer gebruiksrechten, licenties en verplichte credits. Verwijder geen watermerken van materiaal zonder gebruiksrecht. Maak geen verzonnen reviews, beoordelingen, projectresultaten, garanties, keurmerken, prijzen, locaties of contactgegevens. Verifieer social links en veranderlijke gegevens opnieuw voor publicatie.
- Schrijf voor echte bezoekers en gebruik [`humanizer`](README.md#alle-skills-en-hun-repositories) voor natuurlijke formulering zonder feiten te veranderen. Bewaar per claim, review en foto de herkomst. Gebruik alleen echte toestemming voor hergebruik of publicatie.

## 3. Onderzoek ontwerp vóór implementatie

Lees [references/design-and-build.md](references/design-and-build.md) volledig. Maak een korte design read: doel, doelgroep, drie sfeerwoorden en concrete keuzes voor fotografie, typografie, kleur, compositie en de TasteSkill-dials `VARIANCE`, `MOTION`, `DENSITY`.

- **Refero is de primaire referentiebron en een echte bouwvoorwaarde.** Als de MCP beschikbaar is, voer de zoekopdrachten en inspectie uit vóór de eerste layout. Zoek stijlen vanuit 3–5 invalshoeken, bekijk passende stijlen, zoek schermen voor de benodigde secties en inspecteer 3–6 volledige voorbeelden. Kies één dominante referentie die bij dit bedrijf en zijn klanten past. Leg in een *reference lock* de bron-URL/ID, passende eigenschappen, concrete layout/typografie/fotografierollen en de aanpassing aan dit merk vast. Bouw tot de visuele kwaliteit en compositie van die richting overtuigend terugkomen; vergelijk screenshots en verbeter afwijkingen. Neem geen beschermd logo, tekst, foto of volledige unieke layout over. Als stijlen niets opleveren, probeer schermen; als Refero werkelijk niet beschikbaar is, gebruik verifieerbare publieke referenties en meld dat. Claim nooit onderzoek dat niet is uitgevoerd.
- Gebruik TasteSkill / `design-taste-frontend`, `design-md-library` en Awesome Design voor een samenhangend, bedrijfseigen ontwerpsysteem. Bekijk details.so en Design Spells voor gerichte afwerking. Gebruik `image-to-code` wanneer een concrete beeldreferentie vertaald moet worden. Maak geen referentiebeelden als de opdrachtgever die niet wil.
- Controleer of het bedrijf een eigen logo heeft. Bij een ontbrekend logo en opdracht voor merkontwikkeling gebruik je de [logo-design-skill](https://github.com/kaankiziltug/logo-design-skill/tree/main/skills/logo-design); presenteer het als concept tot goedkeuring. Kopieer geen bestaand merk of website.

## 4. Bouw met passende techniek

- Behoud een bruikbare bestaande stack. Kies bij nieuwbouw de eenvoudigste stack die de gevraagde inhoud, prestaties, beheerbaarheid en kosten draagt. Maak de route naar contact helder en de pagina's mobiel bruikbaar. Gebruik de ontwerpbeslissingen werkelijk in de interface.
- Kies uit Magic UI, Kokonut UI, React Bits, Bklit, GSAP, Lenis, Motion en anime.js **alleen wanneer hun concrete component of effect iets toevoegt**. De beslisregels en bronlinks staan in [references/design-and-build.md](references/design-and-build.md). Beperk opvallende animaties en respecteer verminderde beweging.
- **Elke nieuwe website of grote redesign krijgt minstens één betekenisvol dynamisch element.** Kies het op basis van echte content en het gebruiksdoel, bijvoorbeeld een projectfilter, voor/na-schuif, dienstenkiezer, interactieve werkgebiedkaart of nuttige formulierstap. Een hover, autoplay-effect of decoratieve animatie telt niet. Maak het bedienbaar met toetsenbord en op mobiel; test ook de lege en fouttoestand. Is er geen geschikte inhoud, maak dan een kleine maar nuttige interactie rond de contactroute in plaats van een verzonnen project of claim. Documenteer welk probleem het element oplost.
- Maak gevraagde dynamiek echt: definieer bewerkbare velden voor tekst, diensten, projecten, foto's, reviews en SEO, koppel ze aan een CMS of beheeromgeving en verifieer aanmaken, wijzigen en verwijderen via de gepubliceerde site. Zet klantcontent niet alleen in code als de klant zelf moet beheren. Volg [references/production-and-content.md](references/production-and-content.md).
- Bouw formulieren, uploads en integraties pas als de dataflow, toegang en privacy duidelijk zijn. Bewaar geheimen buiten de repository.

## 5. Controleer en doe altijd de SEO-eindronde

- Controleer met TasteSkill preflight, Vercel Web Interface Guidelines en Playwright CLI of beschikbare browsertools de echte desktop- en mobiele weergave, links, menu, focus, formulieren, **het dynamische element**, afbeeldingen, console en prestaties. Vergelijk de render met de Refero reference lock en corrigeer visuele drift. Test CMS-bewerkingen in productieprojecten. Het optionele `scripts/live_check.py` maakt screenshots en een rapport; zie [README](README.md#lokaal-gebruiken).
- Maak de toepassing controleerbaar: noteer per genoemde designskill of bibliotheek de concrete keuze die in de pagina te zien is, met een screenshot of bestandsverwijzing. Noem een middel niet "gebruikt" wanneer alleen de naam in het plan staat. Noteer bij niet-toepassing kort waarom het voor deze site geen waarde toevoegt. Corrigeer zichtbare afwijkingen van de gekozen regels voordat je oplevert.
- **Doe na inhoud, ontwerp en functionele controle altijd de SEO-eindronde in [references/seo-final-pass.md](references/seo-final-pass.md).** Controleer indexeerstatus, titels, beschrijvingen, koppen, interne links, beeldtekst, lokale gegevens, structured data, sitemap, prestaties en meetbaarheid. Bij een demo blijft `noindex` staan; leg productie-indexering als aparte beslissing vast.
- Gebruik in die ronde [mcp-gsc](https://github.com/AminForou/mcp-gsc) voor echte Search Console-data **als** een geverifieerde property en bevoegde toegang bestaan; [open-seo](https://github.com/every-app/open-seo) voor extra onderzoek/audits **als** het beschikbaar en zinvol is; en [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) voor een AI-vindbaarheidsaudit **als** de tool beschikbaar is. Deze middelen zijn geen vervanging voor de basiscontrole. Documenteer welke ervan daadwerkelijk zijn gebruikt en welke toegang ontbrak.

## 6. Lever op

Toon een lokale of deelbare preview, de Refero reference lock met concrete links, het gekozen dynamische element, gebruikte bronnen en beeldrechten, de QA- en SEO-uitkomsten, en open vragen voor de eigenaar. Bij productie: lever een korte beheerinstructie en test een wijziging in de beheeromgeving. Publiceer op GitHub/Railway/een andere host alleen binnen de gegeven toestemming en verifieer de uiteindelijke URL. Doe geen outreach zonder expliciete opdracht. Houd een demo herkenbaar als concept.
