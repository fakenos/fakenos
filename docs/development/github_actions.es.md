# Github actions
Una característica muy interesante de tener siempre es una plataforma totalmente automatizada que pruebe el código en múltiples plataformas a la vez. En este caso estamos utilizando Github Actions para hacerlo. La configuración se encuentra en la carpeta `.github/workflows`.

## Flujos de trabajo actuales
Actualmente, hay 2 flujos de trabajo:

- `docs.yml`: Despliega automáticamente una documentación actualizada en la rama `gh-pages`.
- ``main.yml`: Asegura la corrección del código. Ejecuta la suite de pruebas completa en múltiples plataformas (Linux, MacOS y Windows) y también comprueba el estilo del código.

## Pruebas de flujos de trabajo localmente

En el caso de que quieras cambiar alguno de los flujos de trabajo, en lugar de hacer 1000 solicitudes de tirada o compromisos para probarlo, es posible (y recomendable) ejecutar los flujos de trabajo localmente. Para hacerlo, debes instalar el paquete `act`. Consulta su [documentación oficial](https://nektosact.com/) para obtener más información. Con el comando `act` puedes ejecutar los flujos de trabajo localmente. ¡Eso es todo!

!!! tip
    La orden completa es: **`act -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest`**

!!! failure
    Actualmente, el ejecutor por defecto no funciona. Se recomienda utilizar el `ghcr.io/catthehacker/ubuntu:act-latest`. Por lo tanto, la orden completa es `act -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest`. En este caso la imagen es mucho más grande... pero funciona. También ve este [aviso de Github](https://github.blog/changelog/2024-03-07-github-actions-all-actions-will-run-on-node20-instead-of-node16-by-default/)