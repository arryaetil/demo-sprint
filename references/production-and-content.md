# Productie, dynamische content en beheer

Gebruik dit wanneer een klant tekst, foto's of andere onderdelen zelf moet aanpassen. Bepaal deze route vóór de bouw of migratie; maak in een demo duidelijk wat nu al werkt en wat voor productie nog nodig is.

## Kies een passende beheerroute

1. **Eenvoudige content met weinig wijzigingen:** een kleine CMS-laag of Git-gebaseerd beheer kan volstaan, mits de klant er echt mee kan werken.
2. **Bestaande React/Vite-site behouden:** koppel een passend headless CMS of eigen beheeromgeving aan de bestaande componenten. Houd hosting, dataopslag en beheerkosten zichtbaar in de keuze.
3. **WordPress als klantenpaneel:** bouw een passend thema of blokpatronen en maak contentvelden en media via WordPress bewerkbaar. Controleer of het ontwerp, gedrag en de performance van de demo behouden blijven.

Kies op basis van klanttaken, kosten, onderhoud, leveranciersafhankelijkheid en bestaande code. Een eigen beheeromgeving betekent ook eigen verantwoordelijkheid voor authenticatie, updates, back-ups en herstel; bouw die alleen als een bestaande oplossing niet past.

## Minimaal contentmodel

| Inhoud | Bewerkbare velden |
| --- | --- |
| Algemene pagina's | Titel, intro, secties, call-to-action, SEO-titel/beschrijving en deelafbeelding. |
| Diensten | Naam, uitleg, voordelen, foto, volgorde, URL en SEO-velden. |
| Projecten | Titel, plaats/werkgebied indien toestemming, beschrijving, echte foto's, alt-tekst en publicatiestatus. |
| Reviews | Originele tekst, naam/toestemming, bron, datum en publicatiestatus. |
| Team en contact | Naam, rol, foto, telefoon, e-mail, openingstijden en verifieerbare socials. |
| Beelden | Bestand, bron/rechten, uitsnede, alt-tekst, volgorde en vervanging/verwijdering. |

Scheid concept en gepubliceerd. De beheerder moet zonder code een tekst aanpassen, een foto toevoegen/verwijderen en een pagina publiceren; controleer die drie acties op de zichtbare site. Leg vast wie eigenaar van bronfoto's en accountgegevens is en hoe data geëxporteerd kan worden.

## Productiecontrole

- Geef klanten de minst ruime benodigde rol; beveilig inloggen met sterke authenticatie en waar mogelijk MFA. Bewaar geheimen in omgevingsvariabelen, niet in code of documentatie.
- Beperk bestandstypen en uploadgrootte; scan of valideer uploads, verwijder onnodige metadata en voorkom dat een upload uitvoerbare code wordt. Maak afbeeldingen in passende formaten en groottes.
- Valideer formulierinvoer serverzijde; bescherm tegen spam en misbruik. Bevestig waar inzendingen terechtkomen en hoe persoonsgegevens worden bewaard/verwijderd.
- Houd CMS, plugins, dependencies en server bijgewerkt. Maak automatische back-ups en test herstel. Gebruik HTTPS, redirects, logging en een privacyverklaring die bij de werkelijke verwerking past.
- Controleer rollen, contactstromen, contentwijzigingen en verwijderingen in staging vóór livegang. Houd staging buiten de index; bepaal daarna expliciet de indexeerstatus van productie in de [SEO-eindronde](seo-final-pass.md).
