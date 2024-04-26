"""
Module tests for compatibility with Docker containers.
"""

# pylint: disable=unused-argument
import os
import subprocess
import time
from typing import List

import psutil
from netmiko import ConnectHandler
import pytest

IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS", None)

fakerouter1 = {
    "device_type": "cisco_ios",
    "host": "localhost",
    "username": "user",
    "password": "user",
    "port": 12723,
}

fakerouter2 = {
    "device_type": "cisco_ios",
    "host": "localhost",
    "username": "user",
    "password": "user",
    "port": 12724,
}


def check_docker_is_running() -> False:
    """Checks if Docker is running."""
    return "docker" not in (i.name() for i in psutil.process_iter())


@pytest.fixture
def setup():
    """Starts the docker containers."""
    try:
        subprocess.run(["docker", "compose", "-f", "docker/docker-compose.yaml", "up", "-d"], check=True)
        time.sleep(5)
        yield
    finally:
        subprocess.run(["docker", "compose", "-f", "docker/docker-compose.yaml", "down"], check=True)

@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Skipping test in GitHub Actions.")
@pytest.mark.skipif(check_docker_is_running(), reason="Docker is not running.")
def test_container(setup):
    """
    Test that we can connect to the device and run a command
    in the case that the device is a container.

    Specifically, in this test will connect to a Cisco IOS
    device running in a container and run the command "show clock".
    """
    times_to_collect: int = 100
    outputs: List[str] = []

    device = ConnectHandler(**fakerouter1)

    for _ in range(times_to_collect):
        outputs.append(device.send_command("show clock"))

    assert len(outputs) == times_to_collect
    assert all(isinstance(i, str) for i in outputs)
    assert all("Traceback" not in i for i in outputs)


@pytest.mark.skipif(check_docker_is_running(), reason="Docker is not running.")
def test_container_multiple_connections(setup):
    """
    Similar to test_container, but it runs multiple
    connections to the device.
    """
    connections_count = 10
    times_to_collect = 5

    outputs = {"device1": [], "device2": []}

    for _ in range(connections_count):
        device1 = ConnectHandler(**fakerouter1)
        device2 = ConnectHandler(**fakerouter2)

        for _ in range(times_to_collect):
            outputs["device1"].append(device1.send_command("show clock"))
            outputs["device2"].append(device2.send_command("show clock"))

        device1.disconnect()
        device2.disconnect()

    assert len(outputs["device1"]) == connections_count * times_to_collect
    assert all("Traceback" not in i for i in outputs["device1"])
    assert all(isinstance(i, str) for i in outputs["device1"])

    assert len(outputs["device2"]) == connections_count * times_to_collect
    assert all("Traceback" not in i for i in outputs["device2"])
    assert all(isinstance(i, str) for i in outputs["device2"])
