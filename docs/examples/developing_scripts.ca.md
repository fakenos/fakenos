# Desenvolupament de Scripts

Normalment, quan es desenvolupa una tasca d'automatització de xarxa, s'executa l'script contra un dispositiu a través de SSH. Per a propòsits de desenvolupament, un bon enfocament és utilitzar un dispositiu fals. D'aquesta manera, pots provar el teu script sense el risc de trencar un dispositiu real. Aquí és on entra en joc FakeNOS. Pots crear aquesta plataforma falsa fàcilment de manera local, en lloc de tenir que configurar un dispositiu real en una xarxa real.

## Utilitzant el YAML

Per exemple, creem un dispositiu fals que executa Huawei Smartax. Per crear-lo, primer cal crear un fitxer YAML amb el següent contingut:
```yaml
hosts:
    myRouter:
        username: admin
        password: admin
        platform: huawei_smartax
        port: 6000
```

Pots anomenar aquest fitxer `inventory.yaml` 📕, però qualsevol altre nom és vàlid. Sempre, en tots els fitxers YAML, hem de posar els nostres dispositius amb `hosts:`. En els *hosts* podem afegir tants dispositius com vulguem, sempre que cada dispositiu tingui el seu propi port. Per afegir un dispositiu només cal posar el nom que vulguem.

Per a cada dispositiu, podem establir un `username`, `password`, `port` i `platform`. Tots els plataformes disponibles es poden trobar [aquí](../platforms.md). En aquest cas hem seleccionat la plataforma `huawei_smartax` i les credencials són l'usuari `admin` i la contrasenya `admin`.

A continuació, crea un script de Python amb el següent contingut:
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
Aquest script posarà en marxa el dispositiu fals que hem definit a `inventory.yaml`. S'estarà executant fins que fem `Ctrl+C`. Quan premem això, aturarà tots els processos. Normalment, triga uns segons perquè hem de tancar tots els fils utilitzats.

Per executar l'script de Python :snake: podem utilitzar la següent comanda:
```bash
python main.py
```

Aquest script crearà un dispositiu fals que executa Huawei Smartax. Pots connectar-t'hi utilitzant qualsevol client SSH, com `ssh`:
```bash
# Connectar-se al Huawei Smartax
ssh -p 6000 admin@localhost
```

I aquí tens alguns comandaments que pots provar:

- `display version`
- `display board`
- `display sysman service state`

**I això és tot!** 💅 Hem creat un dispositiu de xarxa fals que emula el Huawei SmartAX i al qual ens podem connectar utilitzant SSH.

Si vols provar més, t'animem a provar més plataformes, canviar les credencials i els ports perquè puguis familiaritzar-te.

## Utilitzant el diccionari
També és possible utilitzar un diccionari en lloc d'un fitxer `.yaml` en els casos en què vulguis tenir una manera programàtica de definir les variables. És bastant similar al mètode descrit anteriorment, però en aquest cas, en lloc de tenir 2 fitxers, mantindrem tot en 1 fitxer.

Imagina que vols poder especificar la plataforma utilitzant la CLI. L'script següent et permet fer el mateix, però definint la `platform`:

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

Per exemple, pots executar-lo utilitzant la següent comanda:
```bash
python main.py huawei_smartax
```

**I això és tot!** Pots accedir de la mateixa manera que abans però especificant cada tipus que és la plataforma. Per exemple, per fer-ho amb Cisco IOS és el mateix:

```bash
python main.py cisco_ios
```

I amb això pots crear un dispositiu Cisco IOS.

## Exemple amb Netmiko i NTC-Templates
El següent script extreu el número de sèrie d'una ONT utilitzant les llibreries [Netmiko](https://github.com/ktbyers/netmiko) i [NTC-Templates](https://github.com/networktocode/ntc-templates). La idea és mostrar que el dispositiu fals actuarà en aquest cas de manera similar al que faria el dispositiu real.

Posa en marxa el dispositiu fals amb la plataforma `huawei_smartax` com s'ha mostrat abans i utilitza el següent codi:
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