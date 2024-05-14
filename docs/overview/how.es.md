# ¿Cómo?

Envía una entrada y obtén la salida: así es como interactuamos con muchos sistemas operativos de red. FakeNOS permite predefinir la salida que se enviará en respuesta a ciertos comandos de entrada, lo que lo hace ideal para pruebas de funciones aisladas.

FakeNOS es un marco de microkernel que ya tiene muchos sistemas operativos de red como Cisco IOS, Alcatel AOS o Huawei SmartAX y se puede extender utilizando complementos. El núcleo se mantiene pequeño y optimizado mientras que la mayor parte de la funcionalidad se descarga a los complementos.

!!! info
    Si quieres ver todas las plataformas disponibles actualmente, mira [aquí](../platforms.md).


!!! note
    Esta parte a continuación se moverá en el futuro.

Actualmente, FakeNOS permite los siguientes plugins:

- **NOS plugins:** plugins para simular comandos de sistemas operativos de red. Aquí es donde se guardan los comandos y sus respuestas.
- **Server Plugins:** plugins responsables de ejecutar varios servidores para conectarse. Actualmente, solo admite `paramiko`.
- **Shell Plugins:** plugins para simular la interfaz de línea de comandos. Analiza y procesa los comandos. Es el middleware entre el servidor y el NOS.

``` mermaid
sequenceDiagram
Cliente->>Servidor: "show clock"
Servidor->>Shell: get "show clock"
Shell->>NOS: get "show clock"
NOS->>Shell: respuesta "show clock"
Shell->>Servidor: respuesta "show clock"
Servidor->>Cliente: "14:38:11.292 PST Tue Feb 10 2009"
```