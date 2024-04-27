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
[pypi-pyversion-badge]:        https://img.shields.io/pypi/pyversions/fakenos.svg
[pepy-downloads-link]:         https://pepy.tech/project/fakenos
[pepy-downloads-badge]:        https://pepy.tech/badge/fakenos
[github-tests-badge]:          https://github.com/fakenos/fakenos/actions/workflows/main.yml/badge.svg
[github-tests-link]:           https://github.com/fakenos/fakenos/actions
[pypi-latest-release-badge]:   https://img.shields.io/pypi/v/fakenos.svg
[pypi-latest-release-link]:    https://pypi.python.org/pypi/fakenos
