# Configurations
One of the coolest features of FakeNOS is that you can configure the devices before starting. This is useful, for example, to specify the IP address of an interface, or which VLANs are allowed on a port. By default there are some predefined values, but you can also change them to adapt it to your needs.

The configuration files are very customized for each brand and device, so, although you are free to configure it as you want, it is most recommended to only change the final values of the variables. To be able to use your own configuration file, you just have to specify the path to the file in the FakeNOS configuration file. Here is an example:

```yaml
hosts:
  R1:
    username: user
    password: user
    port: 6000
    platform: cisco_ios
    configuration_file: my_configurations/cisco_ios.yaml.j2
```

In this case, the configuration file is located in the `my_configurations` folder and is called `cisco_ios.yaml.j2`.

Currently FakeNOS accepts configurations in the following platforms:
- [cisco_ios](https://github.com/fakenos/fakenos/tree/master/fakenos/plugins/nos/platforms_py/configurations/cisco_ios.yaml.j2)
- [huawei_smartax](https://github.com/fakenos/fakenos/tree/master/fakenos/plugins/nos/platforms_py/configurations/huawei_smartax.yaml.j2) 
- [arista_eos](https://github.com/fakenos/fakenos/tree/master/fakenos/plugins/nos/platforms_py/configurations/arista_eos.yaml.j2)