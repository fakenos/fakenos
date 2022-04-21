import pprint
import pytest
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command

def test_nornir_show_command_once():
    nr = InitNornir(config_file="assets/nornir_config.yaml")
    results = nr.run(
        task=netmiko_send_command,
        command_string="show clock",
    )
    pprint.pprint(results)
    
    assert len(results) == 10
    
    for hostname, result in results.items():
        print(f"{hostname}: {result.result}")
        assert result.failed == False
        assert not result.exception
        assert "Traceback" not in result.result
        assert isinstance(result.result, str)

# test_nornir_show_command_once()