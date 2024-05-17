# Testing automático

FakeNOS es una herramienta muy versátil y puede ser utilizada en muchos casos. Uno de los casos de uso más interesantes es el testing automático. En este ejemplo se mostrará cómo FakeNOS puede ayudar a hacer fácilmente las pruebas por ti en tu librería. No está destinado a sustituir otros tipos de pruebas, como las pruebas unitarias, sino más bien a complementarlas dando una plataforma falsa ligera. Primero haremos el script y luego la prueba, aunque se recomienda hacerlo al revés (TDD).

## Script
El siguiente script es similar al que se explica antes en el ejemplo [developing_scripts](developing_scripts.md). Se recomienda hacer primero ese ejemplo. En resumen, entra en un dispositivo Huawei SmartAX, obtiene el valor de todas las ONTs en un puerto y luego busca el número de serie del primero.

```python
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output

credentials = {
    "host": "192.168.0.1",
    "username": "admin",
    "password": "admin",
    "port": 22,
    "device_type": "huawei_smartax"
}


def get_serial_number(sn_index: int = 0) -> str:
    """
    This functions connects to the device and get
    the ONT in the indicated index.
    """
    ont_serial_number: str = ''
    with ConnectHandler(**credentials) as conn:
        output = conn.send_command("display ont info summary ont")
        parsed_output = parse_output(
            platform="huawei_smartax",
            command="display ont info summary 0/1/0",
            data=output
        )
        ont_serial_number = parsed_output[0]['serial_number']
    return ont_serial_number

if __name__ == "__main__":
    serial_number_first_ont = get_serial_number(0)
    print(f"Serial number of the first ONT: {serial_number_first_ont}")
```

!!! note
    Es importante notar que esas credenciales no son reales.

El archivo anterior lo nombraremos `main.py`

## Testing
Por ahora tenemos un script que aún no se ha probado, y aunque, ya se podría utilizar, se recomienda hacer algún tipo de prueba antes. Aún mejor, ahora que tienes FakeNOS puedes utilizar esta increíble librería 😝.

Escribiremos la prueba, y haremos alguna explicación:
```python
from unittest.mock import patch
from fakenos import FakeNOS
import main

inventory = {
    "hosts": {
        "R1": {
            "username": "user",
            "password": "user",
            "port": 6000,
            "platform": "huawei_smartax",
        }
    }
}

fake_credentials = {
    "host": "localhost",
    "username": "user",
    "password": "user",
    "port": 6000,
    "device_type": "huawei_smartax",
}

@patch('main.credentials', fake_credentials)
def test_get_serial_number():
    """
    It tests that the function get_serial_number() gets
    the first ONT serial number correctly.
    """
    net = FakeNOS(inventory=inventory)
    net.start()
    result = main.get_serial_number(0)
    assert result == "1234567890ABCDEF"

    net.stop()

if __name__ == "__main__":
    test_get_serial_number()
    print("All test passed ✅")
```
Este test realizará los siguientes pasos:
1. Crear el dispositivo falso y arrancarlo
2. Realizar la acción a probar
3. Cerrar los dispositivos falsos

En caso de testing automático, siempre se necesita seguir la misma estructura. Este sandwich es necesario. En caso de que no llames al `net.stop()` las suites de test se quedarán colgadas ya que algún hilo subyacente seguirá esperando nuevas conexiones.

!!! note
    Hay planes para hacerlo con un decorador como `@fakenos(platform="cisco_ios")`, pero por ahora
    esta es la forma principal de hacerlo. ¡Los PR que hagan esto son más que bienvenidos! :smiley:

## Implementado con el `with`
!!! new
    Implementado en la versión: v1.0.2

El ejemplo anterior se puede implementar utilizando la declaración `with`. Esta es una forma más pythonica de hacerlo, y se recomienda usarla. El ejemplo anterior se puede reescribir de la siguiente manera:

```python
from fakenos import FakeNOS

with FakeNOS(inventory=inventory) as net:
    result = main.get_serial_number(0)
    assert result == "1234567890ABCDEF"
```

## Implementado con un decorador
!!! new
    Implementado en la versión: v1.0.2

Además, el ejemplo anterior se puede implementar utilizando un decorador. Esta es una forma aún más pythonica de hacerlo. Personalmente, es mi forma favorita. El ejemplo anterior se puede reescribir de la siguiente manera:
    
```python
from fakenos import fakenos

@fakenos(platform="huawei_smartax")
def test_get_serial_number():
    """
    It tests that the function get_serial_number() gets
    the first ONT serial number correctly.
    """
    result = main.get_serial_number(0)
    assert result == "1234567890ABCDEF"
```

El decorador maneja el inicio y el final de los dispositivos falsos, creando el inventario antes de comenzar y deteniéndolo después de la prueba. Este decorador es perfectamente adecuado para probar solo una plataforma. Pero también, sobre muchas plataformas usando tu inventario personalizado.

```python
from fakenos import fakenos

@fakenos(inventory=inventory)
def test_get_serial_number():
    """
    It tests that the function get_serial_number() gets
    the first ONT serial number correctly.
    """
    result = main.get_serial_number(0)
    assert result == "1234567890ABCDEF"
```

Finalmente, en caso de que quieras acceder a los dispositivos falsos, puedes hacerlo añadiendo el parámetro `return_instance` al decorador. Esto devolverá la instancia de los dispositivos falsos a la prueba. Esto es útil cuando quieres hacer algunas pruebas adicionales sobre los dispositivos falsos o conectarte directamente a ellos.

```python
from fakenos import fakenos

@fakenos(platform="huawei_smartax", return_instance=True)
def get_ports_used_in_decorator():
    """ We want to see the ports of the fake device """
    host_ports = [host.port for hosts in net.hosts.values()]
    print(host_ports)
```

En este caso obtengo el siguiente resultado:
```bash
>> [60231]
```

!!! note
    Por defecto el `return_instance` es `False`, así que si quieres usarlo, necesitas estable

!!! note
    Cuando se usa el parámetro de la plataforma, se asignará un puerto aleatorio. Esta decisión es intencional para que las pruebas no afecten a otros sistemas. Si quieres usar un puerto específico, puedes especificarlo usando el inventario.