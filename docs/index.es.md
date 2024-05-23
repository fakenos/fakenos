[![PyPI versions][pypi-pyversion-badge]][pypi-pyversion-link]
[![PyPI][pypi-latest-release-badge]][pypi-latest-release-link]
[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
[![Tests][github-tests-badge]][github-tests-link]
[![Downloads][pepy-downloads-badge]][pepy-downloads-link]

# Fake Network Operating Systems - FakeNOS

> "La realidad es una simple ilusión, pero una muy persistente."
>
> ~ Albert Einstein

FakeNOS simula interacciones de sistemas operativos de red. Puedes simular
interacciones de dispositivos de red como Cisco IOS o Huawei SmartAX sobre
SSH con poco esfuerzo. Este proyecto está principalmente destinado a pruebas
y desarrollo.

[Instalación](usage/installation.md) | [Ejemplos](examples.md) | [Plataformas](platforms.md)


## Instalación
[![PyPI versions][pypi-pyversion-badge]][pypi-pyversion-link]

El paquete está disponible en PyPI, por lo que puedes instalarlo usando pip:
```bash
pip install fakenos
```

## Uso
Este es un ejemplo de simulación en el que simulamos dos dispositivos, uno
ejecutando Cisco IOS y otro ejecutando Huawei SmartAX. Para ejecutarlo, crea
un archivo `inventory.yaml` con el siguiente contenido:
```yaml
hosts:
  R1:
    username: admin
    password: admin
    platform: cisco_ios
    port: 6000
  R2:
    username: admin
    password: admin
    platform: huawei_smartax
    port: 6001
```

Luego crea un archivo `main.py` con el siguiente contenido:
```python
from fakenos import FakeNOS
network_os = FakeNOS(inventory='inventory.yaml')
network_os.start()
```

Ejecuta el script:
```bash
python main.py
```

¡Y Voilà! :dizzy: Tienes dos dispositivos en ejecución, uno con Cisco IOS y otro con Huawei SmartAX.
En caso de que quieras conectarte a ellos, puedes usar cualquier cliente SSH, como `ssh`:
```bash
# Para conectarte a Cisco IOS
ssh -p 6000 admin@localhost

# Para conectarte a Huawei Smartax
ssh -p 6001 admin@localhost
```

Y aquí tienes algunos comandos :computer: que puedes probar:

1. Comandos de Cisco IOS:
    - `show version`
    - `show interfaces`
    - `show ip interface brief`
2. Comandos de Huawei SmartAX:
    - `display version`
    - `display board`
    - `display sysman service state`

!!! tip
    Muchas veces, no tenemos tiempo para leer la documentación. Hay un simple comando `help` que muestra todos los comandos disponibles. Se puede llamar usando `help` o `?`.


## Línea de comandos
FakeNOS viene con una herramienta CLI que te permite iniciar la simulación desde la
línea de comandos. Puedes probar un ejemplo predefinido ejecutando:
```bash
fakenos
```

En este caso se crearán 3 dispositivos:

- Dispositivo Cisco IOS con nombre de usuario `user` y contraseña `user` en el puerto `6000`
- Dispositivo Huawei SmartAX con nombre de usuario `user` y contraseña `user` en el puerto `6001`
- Dispositivo Arista EOS con nombre de usuario `user` y contraseña `user` en el puerto `6002`

También puedes especificar el archivo de inventario a utilizar:
```bash
fakenos --inventory inventory.yaml
```


[github-discussions-link]:     https://github.com/fakenos/fakenos/discussions
[github-discussions-badge]:    https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[black-badge]:                 https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]:                  https://github.com/psf/black
[pypi-pyversion-link]:         https://pypi.python.org/pypi/fakenos/
[pypi-pyversion-badge]:        https://img.shields.io/pypi/pyversions/fakenos.svg?logo=python
[pepy-downloads-link]:         https://pepy.tech/project/fakenos
[pepy-downloads-badge]:        https://pepy.tech/badge/fakenos
[github-tests-badge]:          https://github.com/fakenos/fakenos/actions/workflows/main.yml/badge.svg
[github-tests-link]:           https://github.com/fakenos/fakenos/actions
[pypi-latest-release-link]:    https://pypi.python.org/pypi/fakenos
[pypi-latest-release-badge]:   https://img.shields.io/pypi/v/fakenos.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyBpZD0iTGF5ZXJfMiIgZGF0YS1uYW1lPSJMYXllciAyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NC41OSA2NC41OCI+CiAgPGRlZnM+CiAgICA8c3R5bGU+CiAgICAgIC5jbHMtMSB7CiAgICAgICAgZmlsbDogIzQwMmE1OTsKICAgICAgfQoKICAgICAgLmNscy0xLCAuY2xzLTIgewogICAgICAgIHN0cm9rZS13aWR0aDogMHB4OwogICAgICB9CgogICAgICAuY2xzLTIgewogICAgICAgIGZpbGw6ICNmZmY7CiAgICAgIH0KICAgIDwvc3R5bGU+CiAgPC9kZWZzPgogIDxnIGlkPSJMYXllcl8xLTIiIGRhdGEtbmFtZT0iTGF5ZXIgMSI+CiAgICA8Zz4KICAgICAgPHBhdGggY2xhc3M9ImNscy0xIiBkPSJNOS42NywwaDQ1LjVjNS4xNS44LDguNTUsMy44NCw5LjQyLDkuMDR2NDYuNjJjLS42OCw0Ljc0LTQuNTQsOC4xNy05LjIzLDguNjctNy40Ni43OS0zNS0uNjYtNDUuMzIsMC00LjQxLjAxLTkuMTUtMy4xMy05Ljc5LTcuNzRDLS4wOCw1NC4xOS0uMDksMTAuMzQuMjUsNy45My44NSwzLjY3LDUuNTMuMjUsOS42NywwWiIvPgogICAgICA8Zz4KICAgICAgICA8cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0xMC4yMyw1Ljc4YzIuMTgtLjMxLDQxLjgzLS4zLDQ0LjAxLDAsMi4xNi4zLDMuOTUsMS43Myw0LjU3LDMuODItLjQyLDcuNjIuNTUsNDIuMDEsMCw0NS4zMi0uMzEsMS44Ni0yLjEsMy4xOC0zLjgyLDMuNjQtOC40OC0uNTctNDAuNDIuODctNDQuOTQuMTktMS45My0uMjktMy44OC0yLjA2LTQuMi00LjAxLS4zNi0yLjIxLS4zNi00Mi41NSwwLTQ0Ljc2LjM0LTIuMDksMi4yOC0zLjksNC4zOC00LjJaIi8+CiAgICAgICAgPHBhdGggY2xhc3M9ImNscy0xIiBkPSJNNDkuNTgsMTkuMDJjMTIuOTksMTYuNzEtMy4yMywzOS44My0yMy41LDM0LjMxLTEuMjMtLjMzLTcuMS0zLjAzLTYuOTktNC4wMWwzLjgyLTQuMmMxMi40MSw4LjgzLDI4LjQ3LTMuMzksMjQuNzEtMTcuMjUtMS40My01LjI3LTQuNS0yLjYyLDEuOTYtOC44NloiLz4KICAgICAgICA8cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik00MS40NywxOS41OGMtMTQuMzgtOS42Ni0zMS40OCw2LjczLTIyLjU2LDIxLjI2LS4wNSwxLjMtMi45NSwzLjM5LTMuODIsNC42NkMtLjM4LDI1LjIyLDI0Ljg3LjQyLDQ1LjM4LDE1LjAxYy4wNy4zMy0zLjM2LDQuMTgtMy45Miw0LjU3WiIvPgogICAgICAgIDxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTQxLjQ3LDE5LjU4Yy0xLjUzLDEuMDctMy0uNjMtNC45NC0xLjEyLTYuNDItMS42MS0xMy4zNi44OS0xNi44OCw2LjYyLTEsMS42Mi0xLjUyLDMuNDgtMi4yNCw1LjIyLS4wOC4yLS40Mi0uMzEtLjU2LDAtLjcsMS41NS4xOSw1LjkzLjc1LDcuNjUuMzcsMS4xNCwxLjM1LDEuNjgsMS4zMSwyLjg5LTguOTItMTQuNTMsOC4xOS0zMC45MSwyMi41Ni0yMS4yNloiLz4KICAgICAgICA8Zz4KICAgICAgICAgIDxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTM0LjQ3LDI0LjYyYzMuNTEtLjI0LDUuNzUsMyw0LjU3LDYuMjUtLjM3LDEuMDMtNi4wMSw3LjA4LTYuOTksNy43NC00LjM5LDIuOTMtOC4wMi0uNjQtNi44MS00Ljk0LjI3LS45Niw2LjU3LTguODYsOS4yMy05LjA0WiIvPgogICAgICAgICAgPHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMzUuMjIsMjUuOTJjMS43Ni4wNywyLjkzLDIuMDEsMi43LDMuNjQtLjExLjgxLTguOTUsMTMuNTktMTEuNTYsNi41My0uNzUtMi40OSw2LjkzLTEwLjI0LDguODYtMTAuMTZaIi8+CiAgICAgICAgPC9nPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgo8L3N2Zz4=
