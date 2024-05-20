# Extras
En esta sección se describen otras cosas que pueden ser útiles para el desarrollo de las aplicaciones.

## CLI desarrollo
Unos de los mayores problemas que hemos identificado a la hora de desarrollar es que hacemos un pequeño cambio y nos gustaría que este se viera reflejado de manera inmediata en la aplicación. Para ello hemos creado una opción en el CLI que nos permite cargar la aplicación en modo desarrollo y que se recargue automáticamente cada vez que se haga un cambio en el código. Esta función solo está disponible para el desarrollo de los comandos. De esta manera si ya tienes establecida la conexión SSH no hará falta que la reinicies, ejecutando el comando que hayas querido cambiar se verá reflejado en la aplicación. Esto está pensando para el desarrollo de plataformas nuevas, por lo que archivos que estén fuera de la carpeta `fakenos/plugins/nos/` no se verán reflejados en la aplicación.

El comando es el siguiente:

```bash
fakenos --reload-commands
```

!!! warning
    Los cambios son aditivos. Esto quiere decir que si introduces un nuevo comando verás el cambio reflejado y lo mismo si modificas el comando. Pero si eliminas un comando, este no se eliminará de la aplicación hasta que no se reinicie el servidor.

La manera en la que se consigue esto es instalando una variable de entorno que se llama "FAKENOS_RELOAD_COMMANDS". Si esta se encuentra, entonces el hot-reload estará activado. Si no se encuentra, entonces no se activará. Al finalizar el CLI, la variable se eliminará.