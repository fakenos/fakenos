# Extras
En aquesta secció es descriuen altres coses que poden ser útils per al desenvolupament de les aplicacions.

## CLI desenvolupament
Un dels majors problemes que hem identificat a l'hora de desenvolupar és que fem un petit canvi i ens agradaria que aquest es veiés reflectit de manera immediata en l'aplicació. Per això hem creat una opció en el CLI que ens permet carregar l'aplicació en mode desenvolupament i que es recarregui automàticament cada vegada que es faci un canvi en el codi. Aquest funcionalitat nomès està disponible en els comandaments. D'aquesta manera si ja tens establerta la connexió SSH no farà falta que la reinicis, executant el comandament que hagis volgut canviar es veurà reflectit en l'aplicació. Això està pensant per al desenvolupament de plataformes noves, per la qual cosa arxius que estiguin fora de la carpeta `fakenos/plugins/nos/` no es veuran reflectits en l'aplicació.

El comandament és el següent:

```bash
fakenos --reload-commands
```

!!! warning
    Els canvis són additius. Això vol dir que si introduïu un nou comandament veureu el canvi reflectit i el mateix si modifiqueu el comandament. Però si elimineu un comandament, aquest no s'eliminarà de l'aplicació fins que no es reiniciï el servidor.

La manera en la que s'aconsegueix això és instal·lant una variable d'entorn que es diu "FAKENOS_RELOAD_COMMANDS". Si aquesta es troba, llavors el hot-reload estarà activat. Si no es troba, llavors no s'activarà. Al finalitzar el CLI, la variable s'eliminarà.
