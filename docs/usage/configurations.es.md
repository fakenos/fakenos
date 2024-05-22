# Configuraciones
Unas de las características más guays de FakeNOS es que puedes configurar los dispositivos antes de iniciar. Esto sirve por ejemplo para especificar que dirección IP tiene una interfaz, o que VLANs están permitidas en un puerto. Por defecto hay unos valores predefinidos, pero también puedes cambiarlos para adaptarlo a tus necesidades.

Los archivos de configuración son muy personalizados para cada marca y dispositivo, por lo que, aunque estás libre de configurarlo como quieras,  solo cambiar los valores finales de las variables es lo más recomendable. Para poder utilizar tu propio archivo de configuración, simplemente tienes que especificar la ruta al archivo en el archivo de configuración de FakeNOS. Aquí tienes un ejemplo:

```yaml
hosts:
  R1:
    username: user
    password: user
    port: 6000
    platform: cisco_ios
    configuration_file: my_configurations/cisco_ios.yaml.j2
```

En este caso, el archivo de configuración se encuentra en la carpeta `my_configurations` y se llama `cisco_ios.yaml.j2`.

Actualmente FakeNOS acepta las configuraciones en las siguientes plataformas:

- [cisco_ios](https://github.com/fakenos/fakenos/tree/master/fakenos/plugins/nos/platforms_py/configurations/cisco_ios.yaml.j2)
- [huawei_smartax](https://github.com/fakenos/fakenos/tree/master/fakenos/plugins/nos/platforms_py/configurations/huawei_smartax.yaml.j2) 
- [arista_eos](https://github.com/fakenos/fakenos/tree/master/fakenos/plugins/nos/platforms_py/configurations/arista_eos.yaml.j2)

