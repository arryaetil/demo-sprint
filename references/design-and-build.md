# Ontwerp- en bouwkeuzes uit de oorspronkelijke demo-sprint

Lees dit bij een nieuwe demo of een groot herontwerp. De hulpmiddelen hieronder zijn opties, geen verplichte installatielijst. Controleer actuele documentatie, beschikbaarheid en licentie voordat je een externe dienst of bibliotheek inzet.

## Ontwerponderzoek

- Formuleer een TasteSkill-achtige design read: paginatype, doelgroep, sfeer, visuele familie en passende niveaus voor variatie, beweging en informatiedichtheid.
- Vergelijk hoogstens enkele passende voorbeelden. Mogelijke bronnen uit de oorspronkelijke notities: design-md-library, details.so, designspells.com en Refero. Zoek bij Refero op patroon of onderdeel (hero, prijs, reviews, werkwijze, galerij, contact) als de sector weinig voorbeelden heeft. Noteer per overgenomen idee welke referentie het inspireerde.
- Laat de merkidentiteit voortkomen uit bedrijfsfoto's, logo, locatie en publiek. Vermijd standaard AI-webpatronen zoals willekeurige donkere secties, overmatige pillen, ongefundeerde cijfers en een rij effectkaarten.

## Logo als afzonderlijke keuze

Als het bedrijf geen bruikbaar eigen logo heeft en een nieuw logo in scope is: maak meerdere zwart-witconcepten, controleer vectorbestanden, toon een overzicht en wacht op een keuze. Gebruik daarna pas kleurvarianten, favicon en gebruiksgids. Zet naam en contact van de echte eigenaar op presentatiemateriaal. Houd het logo als concept totdat de eigenaar het goedkeurt en laat merkenrecht controleren voor officieel gebruik.

## Beweging en componenten

De oorspronkelijke notities noemen GSAP, Lenis, Motion, anime.js, Magic UI, Kokonut UI, React Bits en Bklit. Kies ze alleen als ze een concreet probleem oplossen. Gebruik bij een eenvoudige lokale bedrijfsdemo doorgaans CSS en bestaande componenten. Lenis past alleen bij echte scrollvertelling. Gebruik maximaal enkele opvallende effecten met een duidelijke reden; controleer mobiel, toegankelijkheid en verminderde beweging.

## Details die vaak vergeten worden

- Scheid plaatsen en diensten in tekst en navigatie.
- Gebruik één accentkleur en een consistent systeem voor hoeken.
- Toon bij een prijsoverzicht vooral verschillen, geen identieke lijsten op elke kaart.
- Toon echte klantreacties waar mogelijk samen en koppel een gemiddelde score niet aan elke afzonderlijke quote.
- Als donker thema onderdeel van de opdracht is: volg systeemvoorkeur, onthoud een handmatige keuze en voorkom een flits van het verkeerde thema. Controleer 320–430 px schermbreedte.
- Gebruik een absolute `og:image`, `noindex` voor een concept, een zichtbare conceptmelding, en links naar de echte juridische pagina's.
- Controleer bij een bestaande Lovable-repository de tweeweg Git-koppeling en push alleen normale commits naar de gekoppelde branch.

## Oorspronkelijke fasen

1. Onderzoek bedrijfsfeiten, beelden, reviews, logo en juridische pagina's.
2. Toon een korte ontwerpdiagnose en kies referenties; behandel een nieuw logo als apart besluit.
3. Bouw met echte inhoud en doelgerichte beweging.
4. Controleer in browser en met `scripts/live_check.py`.
5. Lever preview, bronnotities en eventueel een geverifieerde Railway-deploy.

De oorspronkelijke tekst verwees naar drie niet-meegeleverde controlescripts en een Windows-pad. Deze repository bevat één draagbaar controlescript voor de mechanische controles. Gebruik per project het werkelijke pad en de beschikbare tools.
