# Automatic Testing

One of the most interesting use cases is the automatic testing. In this example it will be shown how FakeNOS can help easily doing the testing for you in your library. It is not intended to substitute other kind of tests, like unit tests, but rather complement those giving a light fake platform. We will do first the script and later the test, although it is recommended to do the other way around (TDD).

## Script
The following script is similar to the one explained before in the example [developing_scripts](developing_scripts.md). It is recommended to do first that example. Briefly, it enters a device Huawei SmartAX, it the value for all the ONTs in a port and then it looks for the serial number of the first one.

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
    It is important to notice that those credentials are not real.

The previous file we will name it `main.py`

## Testing
For now we have a script that has not been tested yet, and even though, it could be used already, it is recommended to do some kind of testing beforehand. Even better, now that you have FakeNOS you can use this awesome library 😝.

Let's write the test, and we do some explanation:
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
This test will perform the following steps:
1. Create the fake device and start it
2. Perform the action to be tested
3. Close the fake devices

In case of automatic testing, always needs to be followed the same structure. This sandwitch is needed. In case that you don't call the `net.stop()` the test suites will hang up as some underlying thread will be still wait for new connections.

!!! note
    There are plans to make with a decorator like `@fakenos(platform="cisco_ios")`, but for now
    this is the main way to do it. PR doing this are more than welcome! :smiley:
