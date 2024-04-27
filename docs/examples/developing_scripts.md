# Developing Scripts

Usually, when developing a network automation task, you will run the script against a device via SSH. For development purposes, a good approach is to use a fake device. This way, you can test your script without the risk of breaking a real device. That's where FakeNOS comes in. You can create this fake platform easily in local, instead of having to set up a real device in a real network.

## Using the YAML

For example, let's create a fake device running Huawei Smartax. To create it, you need to create first a YAML file with the following content:
```yaml
hosts:
    myRouter:
        username: admin
        password: admin
        platform: huawei_smartax
        port: 6000
```
You can call this file `inventory.yaml` 📕, but any other name is fine. Always, in all the YAML files,
we need to put our devices with the `hosts:`. In the *hosts* we can add as many devices as we want
as long as they each device has its own port. To add a devices we just put whichever name we want.

For each device, we can set a `username`, `password`, `port` and `platform`. All the available platforms can be found [here](/platforms). In this case we have selected the platform `huawei_smartax` and credentials are username `admin` and password `admin`.

Then, create a Python script with the following content:
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
This script will spin up the fake device that we defined in `inventory.yaml`. It will keep running until we do `Ctrl+C`. Whenever we press that it will stop all the processes. Usually, it takes roughly a few seconds because we need to close all the threads used.

To run the python :snake: script we can use the following command :
```bash
python main.py
```

This script will create a fake device running Huawei Smartax. You can connect to it using any SSH client, like `ssh`:
```bash
# To connect to Huawei Smartax
ssh -p 6000 admin@localhost
```

And here are some commands you can try:

-  `display version`
-  `display board`
-  `display sysman service state`

**And that's all!** 💅 We that we have create a fake network device that emulates the Huawei SmartAX and to which we can connect to using SSH.

If you want to try more, we want to encourage you to try more platforms, change the credentials and the ports so you can get familiar.

## Using the dict
As well, it is possible to use a dictionary instead of a `.yaml` file in the cases that you may want to have a programmatic way to define the variables. It is fairly similar to the other method described before, but in this case instead of having 2 files, we will keep all in 1 file.

Imagine you want to be able to specify the platform using the CLI. The following script allows you to do the same,. but defining the `platform`:

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

For example, you can run it using the following command:
```bash
python main.py huawei_smartax
```

**That's all!** You can access the same way as before but specifying each type which is the platform. For example to do it with Cisco IOS is the same:

```bash
python main.py cisco_ios
```

And with that you can create a Cisco IOS device.

## Example with Netmiko and NTC-Templates
The following script extracts the serial number of an ONT using the [Netmiko](https://github.com/ktbyers/netmiko) and the [NTC-Templates](https://github.com/networktocode/ntc-templates) libraries. The idea is to show that the fake device would act in this case similar to what the real device would.

Spin up the fake device with the platform `huawei_smartax` as shown before and use the following code:
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