[![PyPI versions][pypi-pyversion-badge]][pypi-pyversion-link]
[![PyPI][pypi-latest-release-badge]][pypi-latest-release-link]
[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
[![Tests][github-tests-badge]][github-tests-link]
[![Downloads][pepy-downloads-badge]][pepy-downloads-link]

# Fake Network Operating Systems - FakeNOS

> "Reality is merely an illusion, albeit a very persistent one."
>
> ~ Albert Einstein

FakeNOS simulates Network Operating Systems interactions. You can simulate 
network devices like Cisco IOS or Huawei SmartAX interactions over
SSH with little effort. This project it is mainly intented for testing 
and development purposes.

[Installation](usage/installation.en.md) | [Examples](examples.en.md) | [Platforms](platforms.en.md)


## Installation
[![PyPI versions][pypi-pyversion-badge]][pypi-pyversion-link]

The package is currently available in PyPI, so you can install it using pip:
```bash
pip install fakenos
```


## Usage
This is sample example in which we simulate two devices, one running Cisco IOS 
and another running Huawei SmartAX. To run it, create `inventory.yaml` file with
the following content:
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

Then create `main.py` file with the following content:
```python
from fakenos import FakeNOS
network_os = FakeNOS(inventory='inventory.yaml')
network_os.start()
```

Run the script:
```bash
python main.py
```

And Voila! :dizzy: You have two devices running, one with Cisco IOS and another with Huawei SmartAX.
In case you want to connect to them, you can use any SSH client, like `ssh`:
```bash
# To connect to Cisco IOS
ssh -p 6000 admin@localhost

# To connect to Huawei Smartax
ssh -p 6001 admin@localhost
```

And here are some commands :computer: you can try:

1. Cisco IOS commands:
    - `show version`
    - `show interfaces`
    - `show ip interface brief`
2. Huawei SmartAX commands:
    - `display version`
    - `display board`
    - `display sysman service state`

!!! tip
    Many times, we don't have time to read the documentation. There is a simple `help` command which shows all the available commands. It can be called using `help` or `?`.

## CLI Usage
FakeNOS comes with a CLI tool that allows you to start the simulation from the
command line. You can try a predefined example by running:
```bash
fakenos
```

In this case 3 devices will be created:
- Cisco IOS device with username `user` and password `user` on port `6000`
- Huawei SmartAX device with username `user` and password `user` on port `6001`
- Arista EOS device with username `user` and password `user` on port `6002`

You can also specify the inventory file to use:
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
