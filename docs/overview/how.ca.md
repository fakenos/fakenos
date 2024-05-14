# Com funciona?

Envia una entrada i obté una sortida: així és com interactuem amb molts sistemes operatius de xarxa. FakeNOS permet predefinir la sortida que s'enviarà en resposta a certs comandaments d'entrada, el que el fa ideal per a proves de funcions aïllades.

FakeNOS és un marc de microkernel que ja té molts sistemes operatius de xarxa com Cisco IOS, Alcatel AOS o Huawei SmartAX i es pot estendre utilitzant complements. El nucli es manté petit i optimitzat mentre que la major part de la funcionalitat es descarrega als complements.

!!! info
    Si vols veure totes les plataformes disponibles actualment, mira [aquí](../platforms.md).

!!! note
    Aquesta part a continuació es mourà en el futur.

Actualment, FakeNOS permet els següents plugins:

- **NOS plugins:** plugins per simular comandaments de sistemes operatius de xarxa. Aquí és on es guarden els comandaments i les seves respostes.
- **Server Plugins:** plugins responsables d'executar diversos servidors per connectar-se. Actualment, només admet `paramiko`.
- **Shell Plugins:** plugins per simular la interfície de línia de comandes. Analitza i processa els comandaments. És el middleware entre el servidor i el NOS.

``` mermaid
sequenceDiagram
Client->>Servidor: "show clock"
Servidor->>Shell: get "show clock"
Shell->>NOS: get "show clock"
NOS->>Shell: resposta "show clock"
Shell->>Servidor: resposta "show clock"
Servidor->>Client: "14:38:11.292 PST Tue Feb 10 2009"
```