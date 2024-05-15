[![PyPI versions][pypi-pyversion-badge]][pypi-pyversion-link]
[![PyPI][pypi-latest-release-badge]][pypi-latest-release-link]
[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
[![Tests][github-tests-badge]][github-tests-link]
[![Downloads][pepy-downloads-badge]][pepy-downloads-link]

# Fake Network Operating Systems - FakeNOS

> "La realitat no és més que una il·lusió, pero una molt persistent."
>
> ~ Albert Einstein

FakeNOS simula interaccions de sistemes operatius de xarxa. Pots simular
interaccions de dispositius de xarxa com Cisco IOS o Huawei SmartAX sobre
SSH amb poc esforç. Aquest projecte està principalment destinat a proves
i desenvolupament.

[Instal·lació](usage/installation.md) | [Exemples](examples.md) | [Plataformes](platforms.md)


## Instal·lació
[![PyPI versions][pypi-pyversion-badge]][pypi-pyversion-link]

El paquet està disponible a PyPI, així que pots instal·lar-lo amb pip:
```bash
pip install fakenos
```

## Ús
Aquest és un exemple de simulació en el qual simulem dos dispositius, un
executant Cisco IOS i un altre executant Huawei SmartAX. Per executar-ho,
crea un fitxer `inventory.yaml` amb el següent contingut:
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

A continuació, crea un fitxer `main.py` amb el següent contingut:
```python
from fakenos import FakeNOS
network_os = FakeNOS(inventory='inventory.yaml')
network_os.start()
```

Executa l'script:
```bash
python main.py
```

I Voilà! :dizzy: Tens dos dispositius en execució, un amb Cisco IOS i un altre amb Huawei SmartAX.
En cas que vulguis connectar-t'hi, pots utilitzar qualsevol client SSH, com `ssh`:
```bash
# Per connectar-te a Cisco IOS
ssh -p 6000 admin@localhost

# Per connectar-te a Huawei Smartax
ssh -p 6001 admin@localhost
```

I aquí tens alguns comandaments :computer: que pots provar:

1. Comandaments de Cisco IOS:
    - `show version`
    - `show interfaces`
    - `show ip interface brief`

2. Comandaments de Huawei SmartAX:
    - `display version`
    - `display board`
    - `display sysman service state`

!!! tip
    Moltes vegades, no tenim temps per llegir la documentació. Hi ha un senzill comandament `help` que mostra tots els comandaments disponibles. Es pot cridar amb `help` o `?`.


## Línia de comandaments
FakeNOS ve amb una eina CLI que et permet iniciar la simulació des de la
línia de comandaments. Pots provar un exemple predefinit executant:
```bash
fakenos
```

En aquest cas es crearan 3 dispositius:

- Dispositiu Cisco IOS amb nom d'usuari `user` i contrasenya `user` al port `6000`
- Dispositiu Huawei SmartAX amb nom d'usuari `user` i contrasenya `user` al port `6001`
- Dispositiu Arista EOS amb nom d'usuari `user` i contrasenya `user` al port `6002`

També pots especificar el fitxer d'inventari a utilitzar:
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
