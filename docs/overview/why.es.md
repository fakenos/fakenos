# ¿Por qué FakeNOS?

Testing es un aspecto crucial de la ingeniería de software moderna y, por lo tanto, es
importante en la Automatización de Redes. FakeNOS resuelve el problema de probar scripts
de una manera ligera y fácil de usar. Permite crear un entorno de prueba con múltiples
dispositivos ejecutando diferentes Sistemas Operativos de Red (NOS) en cuestión de minutos.

## Problema con las pruebas de integración
Un aspecto crucial de escribir aplicaciones o scripts para la Automatización de Redes es
la prueba. A menudo, las pruebas se realizan utilizando instancias físicas o virtuales de
aparatos de red que ejecutan cierta versión del Sistema Operativo de Red (NOS). Ese
enfoque, aunque da los mejores resultados de integración, en muchos casos conlleva una
gran cantidad de sobrecarga para configurar, ejecutar y desmontar, así como poner una
carga significativa en la utilización de recursos de computación y almacenamiento.

Además, muchas veces sucede que el proveedor no da acceso al dispositivo para fines de
prueba o que no tienes la imagen para ejecutar en un entorno virtual. En tales casos, es
muy difícil probar la aplicación o script que has escrito.

También, en caso de que queramos crear un entorno de prueba con múltiples dispositivos
ejecutando diferentes NOS, es muy difícil configurar y ejecutar dicho entorno. A pesar de
que existen herramientas como [GNS3](https://www.gns3.com/) o [EVE-NG](https://www.eve-ng.net/),
no siempre son la mejor solución para fines de prueba.

## Problema con las pruebas unitarias
Otro enfoque es simular los métodos de las bibliotecas subyacentes para engañar a las
aplicaciones bajo prueba para que crean que están recibiendo la salida de dispositivos
reales. Ese enfoque funciona muy bien para las pruebas unitarias, pero no simula aspectos
como el establecimiento y manejo de la conexión.

Además, el principal problema con dicho enfoque es que necesitas especificar la salida
para cada comando que deseas probar. Esto es muy consumidor de tiempo y no siempre es
la mejor solución.

## Nuestro enfoque
FakeNOS se posiciona en algún lugar intermedio entre las pruebas de integración completas
y las pruebas que simulan interacciones de dispositivos. FakeNOS permite crear plugins de
NOS para producir la salida predefinida para probar el comportamiento de las aplicaciones
mientras se ejecutan servidores para establecer conexiones con.

Lo hace de una manera ligera y fácil de usar. Puedes crear un entorno de prueba con
múltiples dispositivos ejecutando diferentes NOS en cuestión de minutos. Es simplemente
una biblioteca de Python que inicia un servidor SSH y falsifica la salida de los comandos
que especificas.

!!! note

    En el enfoque actual, la salida está predefinida y siempre será la misma y responderá
    al mismo comando exacto. Hay un esfuerzo en curso para inferir los comandos (similar
    a ntc-templates) y hacer que la salida sea dinámica (usando Jinja2).