# Testing automàtic

Un dels casos d'ús més interessants és el testing automàtic. En aquest exemple es mostrarà com FakeNOS pot ajudar a fer fàcilment el testing per tu en la teva llibreria. No està destinat a substituir altres tipus de proves, com les proves unitàries, sinó més aviat complementar-les donant una plataforma falsa lleugera. Primer farem l'script i després la prova, encara que es recomana fer-ho al revés (TDD).

## Script
L'script següent és similar al que s'explica abans a l'exemple [developing_scripts](developing_scripts.md). Es recomana fer primer aquest exemple. En resum, entra en un dispositiu Huawei SmartAX, obté el valor de totes les ONTs en un port i després busca el número de sèrie de la primera.

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
    És important notar que aquestes credencials no són reals.

L'anterior fitxer el nomenarem `main.py`

## Testing
Per ara tenim un script que encara no s'ha provat, i tot i així, ja es podria utilitzar, es recomana fer algun tipus de prova abans. Encara millor, ara que tens FakeNOS pots utilitzar aquesta increïble llibreria 😝.

Escriurem la prova, i farem alguna explicació:
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

Aquest test realitzarà els següents passos:
1. Crear el dispositiu fals i iniciar-lo
2. Realitzar l'acció a provar
3. Tancar els dispositius falsos

En cas de testing automàtic, sempre cal seguir la mateixa estructura. Aquest sandvitx és necessari. En cas que no cridis al `net.stop()` les suites de proves es quedaran penjades ja que algun fil intern seguirà esperant noves connexions.

!!! note
    Hi ha plans per fer-ho amb un decorador com `@fakenos(platform="cisco_ios")`, però per ara
    aquesta és la principal manera de fer-ho. Les PR que ho facin són més que benvingudes! :smiley:

## Implementat amb el `with`

!!! new
    Implementat a la versió: v1.0.2

L'exemple anterior es pot implementar utilitzant l'expressió `with`. Aquesta és una manera més pythonica de fer-ho, i es recomana utilitzar-la. L'exemple anterior es podria reescriure de la següent manera:

```python
from fakenos import FakeNOS

with FakeNOS(inventory=inventory) as net:
    result = main.get_serial_number(0)
```
