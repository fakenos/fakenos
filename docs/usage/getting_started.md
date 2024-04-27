# Basic Usage
FakeNOS has some built in default hosts which are used in case that no `inventory` is given. In such case it will open the following:

- **router1**: a device with username `user` and password `user` in the port 6000. The platform is `cisco_ios`.
- **router2**: a device with username `user` and password `user` in the port 6001. The platform is `huawei_smartax`.

In both cases, the fake devices are running on the localhost or 127.0.0.1 address. To run those just use the following code:

```python
from fakenos import FakeNOS

network = FakeNOS()
network.start()
```

Initiate SSH connection using default username `user` and password `user`:

```bash
ssh -p 6000 user@localhost # cisco_ios
ssh -p 6001 user@localhost # huawei_smartax
```

!!! bug
    The CLI command is not currently available.

The equivalent to running above code would be to run FakeNOS CLI without
any arguments:

```bash
fakenos
```
