# Desarrollo de scripts

Cuando se desarrolla una tarea de automatización de red, normalmente se ejecuta el script contra un dispositivo a través de SSH. Para propósitos de desarrollo, un buen enfoque es utilizar un dispositivo falso. De esta manera, puedes probar tu script sin el riesgo de romper un dispositivo real. Ahí es donde entra en juego FakeNOS. Puedes crear esta plataforma falsa fácilmente en local, en lugar de tener que configurar un dispositivo real en una red real.

## Usando el YAML

Por ejemplo, creemos un dispositivo falso que ejecuta Huawei Smartax. Para crearlo, primero crea un archivo YAML con el siguiente contenido:
```yaml
hosts:
    myRouter:
        username: admin
        password: admin
        platform: huawei_smartax
        port: 6000
```
Puedes llamar a este archivo `inventory.yaml` 📕, pero cualquier otro nombre es válido. Siempre, en todos los archivos YAML, necesitamos poner nuestros dispositivos con `hosts:`. En los *hosts* podemos añadir tantos dispositivos como queramos, siempre que cada dispositivo tenga su propio puerto. Para añadir un dispositivo solo ponemos el nombre que queramos.

Para cada dispositivo, podemos establecer un `username`, `password`, `port` y `platform`. Todas las plataformas disponibles se pueden encontrar [aquí](../platforms.md). En este caso hemos seleccionado la plataforma `huawei_smartax` y las credenciales son el usuario `admin` y la contraseña `admin`.

Entonces, crea un script de Python con el siguiente contenido:
```python
from fakenos import FakeNOS
network_os = FakeNOS(inventory='inventory.yaml')
network_os.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    network_os.stop()
```
Este script pondrá en marcha el dispositivo falso que hemos definido en `inventory.yaml`. Estará ejecutándose hasta que hagamos `Ctrl+C`. Cuando presionamos eso, detendrá todos los procesos. Normalmente, tarda unos segundos porque necesitamos cerrar todos los hilos utilizados.

Para ejecutar el script de Python :snake: podemos usar el siguiente comando:
```bash
python main.py
```

Este script creará un dispositivo falso que ejecuta Huawei Smartax. Puedes conectarte a él utilizando cualquier cliente SSH, como `ssh`:
```bash
# Para conectarse al Huawei Smartax
ssh -p 6000 admin@localhost
```

Y aquí tienes algunos comandos que puedes probar:

-  `display version`
-  `display board`
-  `display sysman service state`

**¡Y eso es todo!** 💅 Hemos creado un dispositivo de red falso que emula el Huawei SmartAX y al que nos podemos conectar utilizando SSH.

Si quieres probar más, te animamos a probar más plataformas, cambiar las credenciales y los puertos para que puedas familiarizarte.

## Usando dict
También, es posible utilizar un diccionario en lugar de un archivo `.yaml` en los casos en los que quieras tener una manera programática de definir las variables. Es bastante similar al método descrito anteriormente, pero en este caso, en lugar de tener 2 archivos, mantendremos todo en 1 archivo.

Imagina que quieres poder especificar la plataforma utilizando la CLI. El siguiente script te permite hacer lo mismo, pero definiendo la `platform`:
```python
import argparse
from fakenos import FakeNOS

parser = argparse.ArgumentParser(
    description="Create a fake device specifying the platform."
    )

parser.add_argument(
    "platform", 
    type=str, 
    help="fake device network operating system"
    )

args = parser.parse_args()

inventory = {
    "hosts": {
        "mySwitch": {
            "username": "admin",
            "password": "admin",
            "platform": args.platform,
            "port": 6000
        }
    }
}

net = FakeNOS(inventory=inventory)
```

Por ejemplo, puedes ejecutarlo utilizando el siguiente comando:
```bash
python main.py huawei_smartax
```

**¡Eso es todo!** Puedes acceder de la misma manera que antes pero especificando cada tipo que es la plataforma. Por ejemplo, para hacerlo con Cisco IOS es lo mismo:
```bash
python main.py cisco_ios
```

Y con eso puedes crear un dispositivo Cisco IOS.

## Ejemplo utilizando Netmiko y NTC-Templates
El siguiente script extrae el número de serie de una ONT utilizando las librerías [Netmiko](https://github.com/ktbyers/netmiko) y [NTC-Templates](https://github.com/networktocode/ntc-templates). La idea es mostrar que el dispositivo falso actuaría en este caso de manera similar a lo que haría el dispositivo real.

Crea un dispositivo falso con la plataforma `huawei_smartax` como se muestra antes y utiliza el siguiente código:
```python
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output

credentials = {
    "host": "localhost",
    "username": "admin",
    "password": "admin",
    "port": 6000,
    "device_type": "huawei_smartax"
}

serial_number: str = ''
with ConnectHandler(**credentials) as conn:
    output = conn.send_command("display ont info summary ont")
    parsed_output = parse_output(
        platform="huawei_smartax", 
        command="display ont info summary 0/1/0", 
        data=output
    )
    serial_number = parsed_output[0]['serial_number']

print(f"Serial number of the first ONT: {serial_number}")
```