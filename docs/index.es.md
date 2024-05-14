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
[pypi-pyversion-badge]:        https://img.shields.io/pypi/pyversions/fakenos.svg
[pepy-downloads-link]:         https://pepy.tech/project/fakenos
[pepy-downloads-badge]:        https://pepy.tech/badge/fakenos
[github-tests-badge]:          https://github.com/fakenos/fakenos/actions/workflows/main.yml/badge.svg
[github-tests-link]:           https://github.com/fakenos/fakenos/actions
[pypi-latest-release-badge]:   https://img.shields.io/pypi/v/fakenos.svg
[pypi-latest-release-link]:    https://pypi.python.org/pypi/fakenos
