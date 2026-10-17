# Vaste SEO-eindronde

Doorloop dit **na** de inhoudelijke, visuele en functionele QA van iedere nieuwe site, grote redesign en demo. Rapporteer wat gecontroleerd, aangepast en nog niet meetbaar is. Een toolscore is geen bewijs van vindbaarheid; zoekmachines beslissen zelf over indexering en weergave.

## 1. Bepaal de indexeerstatus

| Omgeving | Actie |
| --- | --- |
| Lokale preview of klantdemo | Houd `noindex` en conceptstatus intact. Controleer dat de canonieke URL, sitemap en gedeelde previews niet per ongeluk als officiële productieversie worden gepresenteerd. Verander geen beveiliging, toegangscontrole of crawlbeperking om een audit te laten slagen. |
| Productie met definitief domein | Controleer met de eigenaar welke pagina's openbaar mogen zijn; test robots-regels, `noindex`, canonical, redirects en sitemap tegen dat besluit. Dien de sitemap alleen in bij een geverifieerde property en wanneer dit binnen de opdracht valt. |

## 2. Controleer elke belangrijke pagina

- Unieke, beschrijvende title en meta description; één duidelijke H1; logische H2's; tekst die dienst, doelgroep en locatie natuurlijk uitlegt. Geen gekopieerde of automatisch gegenereerde plaatsvarianten zonder unieke waarde.
- Interne links naar relevante diensten, werkvoorbeelden, contact en juridische pagina's. Werkende navigatie, bruikbare URL's, juiste redirects en geen kapotte links.
- Echte foto's waar mogelijk, passende resoluties, beschrijvende alt-tekst voor informatieve beelden, moderne formaten en lazy loading onder de eerste schermhoogte. Meet Core Web Vitals en mobiel gebruik; los echte knelpunten op.
- Open Graph en deelafbeelding, canonieke URL en sitemap waar passend. Controleer dat de gegevens bij de juiste productie-URL horen. Maak geen dubbele pagina's voor zoekwoorden.
- Voor lokale bedrijven: consistente, geverifieerde naam, adres/werkgebied, telefoon, openingstijden en dienstinformatie. Gebruik `LocalBusiness`-schema alleen voor feiten die zichtbaar en verifieerbaar zijn; verzin geen ratings of reviews in structured data. Test markup met Google's hulpmiddelen.
- In een CMS: titel, beschrijving, URL, beeldtekst en delen van de pagina moeten door de klant kunnen worden beheerd zonder code. Voorkom dat publicaties of verwijderingen dode links en verouderde sitemaps opleveren.

## 3. Gebruik de drie extra bronnen als ze passen

| Bron | Wanneer | Wat je doet | Grens |
| --- | --- | --- | --- |
| [AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc) | Een geverifieerde Google Search Console-property en bevoegde toegang bestaan. Vooral waardevol na livegang. | Bekijk property, zoekprestaties, indexdekking, URL-inspectie en sitemapstatus; kies verbeteringen op basis van echte data. | Een nieuwe demo heeft doorgaans geen GSC-data. Sla geen OAuth-gegevens of serviceaccounts in de repo op. Voer geen destructieve acties uit zonder opdracht. |
| [every-app/open-seo](https://github.com/every-app/open-seo) | De suite of MCP is beschikbaar en het onderzoek past bij tijd en budget. | Gebruik audits, zoekwoord- en concurrentieonderzoek als input voor betere pagina's en prioriteiten. | De zelf gehoste variant kan een DataForSEO-sleutel en kosten vereisen. Meld wanneer je hem niet hebt gebruikt; verzin geen resultaten. |
| [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | Er is een openbare URL of een bereikbare preview en de skill/CLI is beschikbaar. | Audit voor machineleesbaarheid, heldere entiteiten, bronverwijzingen en technische fouten; controleer adviezen tegen echte bedrijfsfeiten. | Een GEO-score garandeert geen AI-vermelding. `llms.txt` is optioneel. Bij een demo is beperkte crawlbaarheid bewust en geen reden om `noindex` te verwijderen. |

Als de tools ontbreken, voer de basiscontrole handmatig of met beschikbare browsertools uit. Installeer of configureer externe diensten alleen als dat binnen de opdracht en toegangsrechten valt. Noteer per tool: gebruikt / niet beschikbaar / niet van toepassing, plus de reden.

## 4. Afronden

Leg de belangrijkste fouten vast, herstel wat binnen de opdracht valt, test opnieuw en vermeld het resterende effect of de onzekerheid. Geef bij een nieuwe productiepagina pas later een tweede analyse met echte Search Console-data; de eerste eindronde kan geen ranking beloven.

Basis voor de controle: [Google Search Essentials](https://developers.google.com/search/docs/essentials), [technische vereisten](https://developers.google.com/search/docs/essentials/technical) en [LocalBusiness structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business).
