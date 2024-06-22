[![Downloads][pepy-downloads-badge]][pepy-downloads-link]
[![PyPI][pypi-latest-release-badge]][pypi-latest-release-link]
[![PyPI versions][pypi-pyversion-badge]][pypi-pyversion-link]
[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
[![Code style: black][black-badge]][black-link]
[![Tests][github-tests-badge]][github-tests-link]

# Fake Network Operating Systems - FakeNOS

> "Reality is merely an illusion, albeit a very persistent one."
>
> ~ Albert Einstein

FakeNOS created to simulate Network Operating Systems interactions.

[Documentation](https://fakenos.github.io/fakenos/)

## Why?

Crucial aspect of writing applications or scripts for Network Automation is 
testing, often testing done using physical or virtual instances of network
appliances running certain version of Network Operating System (NOS). That
approach, while gives best integration results, in many cases carries a lot
of overhead to setup, run and tear down as well as putting significant burden
on compute and storage resource utilization.

Other approach is to mock underlying libraries methods to fool applications
under testing into believing that it is getting output from real devices. That
approach works very well for unit testing, but fails to simulate such aspects
as connection establishment and handling.

FakeNOS positions itself somewhere in the middle between full integration testing
and testing that mocks device interactions. FakeNOS allows to create NOS plugins
to produce pre-defined output to test applications behavior while running servers 
to establish connections with.

## What?

FakeNOS can:

- Run thousands of servers to stress test applications
- Simulate Network Operating Systems Command Line Interface (CLI) interactions
- Provide high-level API to create custom NOS plugins
- Run in docker container to simplify integration with your infrastructure
- Make use of FakeNOS CLI tool for quick run and prototype simulations
- Works on Windows, MAC and Linux under major Python version

## How?

Send input and get the output - this is how we interact with many 
Network Operating Systems, FakeNOS allows to pre-define the output 
to sent in response to certain input commands, making it ideal for
isolated feature testing.

FakeNOS is a micro-kernel framework that can be extended using plugins. 
The core is kept small and optimized while most of the functionality 
offloaded to plugins.

FakeNOS has these pluggable systems:

- Server Plugins - plugins responsible for running various servers to connect with
- Shell Plugins - plugins to simulate command line interface shell
- NOS plugins - plugins to simulate Network Operating System commands

## What not?

FakeNOS is a simulator, it does not emulate any of Network Control, Data 
or Management planes, it merely takes the commands as input and responds
with predefined output.

## FakeNOS inspired by and borrowed from

- [sshim](https://pythonhosted.org/sshim/) - library for testing and debugging SSH automation clients
- [PythonSSHServerTutorial](https://github.com/ramonmeza/PythonSSHServerTutorial) - tutorial on creating paramiko based SSH server
- [fake-switches](https://github.com/internap/fake-switches) - pluggable switch/router command-line simulator
- [ncs-netsim](https://developer.cisco.com/docs/nso/guides/#!the-network-simulator) - tool to simulate a network of devices
- [cisshgo](https://github.com/tbotnz/cisshgo) - concurrent SSH server to emulate network equipment for testing purposes
- [scrapli-replay](https://pypi.org/project/scrapli-replay/) - tools to enable easy testing of SSH programs and to create semi-interactive SSH servers


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
