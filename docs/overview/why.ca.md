# Per què FakeNOS?

La prova és un aspecte crucial de l'enginyeria de programari modern i, per tant, és important en l'Automatització de Xarxes. FakeNOS resol el problema de provar scripts de manera lleugera i fàcil d'utilitzar. Permet crear un entorn de proves amb diversos dispositius que executen diferents Sistemes Operatius de Xarxa (NOS) en qüestió de minuts.

## Problema amb el "integration testing"

Un aspecte crucial de l'escriptura d'aplicacions o scripts per a l'Automatització de Xarxes és la prova. Sovint, les proves es realitzen utilitzant instàncies físiques o virtuals d'aparells de xarxa que executen una certa versió del Sistema Operatiu de Xarxa (NOS). Aquest enfocament, tot i que dóna els millors resultats d'integració, en molts casos comporta una gran quantitat de sobrecàrrega per configurar, executar i desmuntar, així com posar una càrrega significativa en la utilització de recursos de computació i emmagatzematge.

A més, moltes vegades succeeix que el proveïdor no dóna accés al dispositiu per a fins de prova o que no tens la imatge per executar en un entorn virtual. En aquests casos, és molt difícil provar l'aplicació o script que has escrit.

També, en cas que vulguem crear un entorn de prova amb diversos dispositius que executen diferents NOS, és molt difícil configurar i executar aquest entorn. Tot i que existeixen eines com [GNS3](https://www.gns3.com/) o [EVE-NG](https://www.eve-ng.net/), no sempre són la millor solució per a fins de prova.

## Problema amb el "unit testing"

Un altre enfocament és simular els mètodes de les biblioteques subjacents per enganyar les aplicacions sota prova perquè creguin que estan rebent la sortida de dispositius reals. Aquest enfocament funciona molt bé per a les proves unitàries, però no simula aspectes com l'establiment i maneig de la connexió.

A més, el principal problema amb aquest enfocament és que necessites especificar la sortida per a cada comandament que vols provar. Això és molt consumidor de temps i no sempre és la millor solució.

## El nostre enfocament
FakeNOS es posiciona en algun lloc intermig entre les proves d'integració completes i les proves que simulen interaccions de dispositius. FakeNOS permet crear plugins de NOS per produir la sortida predefinida per provar el comportament de les aplicacions mentre s'executen servidors als que es pot establir la connexió.

Ho fa d'una manera lleugera i fàcil d'utilitzar. Pots crear un entorn de prova amb diversos dispositius que executen diferents NOS en qüestió de minuts. És simplement una biblioteca de Python que inicia un servidor SSH i falsifica la sortida dels comandaments que especifiques.

!!! note

    En l'enfocament actual, la sortida està predefinida i sempre serà la mateixa i respondrà al mateix comandament exacte. Hi ha un esforç en curs per inferir els comandaments (similar a ntc-templates) i fer que la sortida sigui dinàmica (utilitzant Jinja2).