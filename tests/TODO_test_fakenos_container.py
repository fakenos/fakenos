import sys
import pprint
import time

sys.path.insert(0, "..")

from netmiko import ConnectHandler
from fakenos import FakeNOS

xesandbox_data = {
    "device_type": "cisco_xe",
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": 22,
}

fakerouter1 = {
    "device_type": "cisco_ios",
    "host": "10.100.0.2",
    "username": "user",
    "password": "user",
    "port": 6001,
}

fakerouter2 = {
    "device_type": "cisco_ios",
    "host": "10.100.0.2",
    "username": "user",
    "password": "user",
    "port": 6002,
}


def test_container_cisco_ios_netmiko_send_show_clock_100_times():
    times_to_collect = 100
    outputs = []

    # device = ConnectHandler(**xesandbox_data)
    device = ConnectHandler(**fakerouter1)

    for i in range(times_to_collect):
        outputs.append(device.send_command("show clock"))

    assert len(outputs) == times_to_collect
    assert all(isinstance(i, str) for i in outputs)
    assert all("Traceback" not in i for i in outputs)


# test_cisco_ios_netmiko_send_show_clock_100_times()


def test_container_cisco_ios_netmiko_multiple_connections():
    """Method to run multiple connection establishment and teardown"""
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

    pprint.pprint(outputs)

    assert len(outputs["device1"]) == connections_count * times_to_collect
    assert all("Traceback" not in i for i in outputs["device1"])
    assert all(isinstance(i, str) for i in outputs["device1"])

    assert len(outputs["device2"]) == connections_count * times_to_collect
    assert all("Traceback" not in i for i in outputs["device2"])
    assert all(isinstance(i, str) for i in outputs["device2"])


# test_cisco_ios_multiple_connections()
