# Què no?

FakeNOS és un simulador, no emula cap dels plans de Control de Xarxa, Dades o Gestió, simplement pren els comandaments com a entrada i respon amb una sortida predefinida. Tot i que hi ha plans per afegir alguna sortida dinàmica, no hi ha plans per emular el comportament del protocol subjacent.

En cas que estiguis buscant un emulador de xarxa que emuli els protocols subjacents com BGP, LLDP, etc., aquí tens alguns que poden resultar-te interessants:

- [GNS3](https://www.gns3.com/)
- [EVE-NG](https://www.eve-ng.net/)
- [Cisco Packet Tracer](https://www.netacad.com/es/courses/packet-tracer)

La idea d'aquesta llibreria és que es pot integrar en programari automatitzat que interactua amb equips de xarxa, emulant el comportament d'alt nivell.