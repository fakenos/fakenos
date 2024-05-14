# uso básico
FakeNOS tiene algunos hosts predeterminados que se utilizan en caso de que no se proporcione un `inventario`. En tal caso, se abrirá lo siguiente:

- **router_cisco_ios**: un dispositivo con nombre de usuario `user` y contraseña `user` en el puerto 6000. La plataforma es `cisco_ios`.
- **router_huawei_smartax**: un dispositivo con nombre de usuario `user` y contraseña `user` en el puerto 6001. La plataforma es `huawei_smartax`.
- **router_arista_eos**: un dispositivo con nombre de usuario `user` y contraseña `user` en el puerto 6002. La plataforma es `arista_eos`.

En ambos casos, los dispositivos falsos se están ejecutando en la IP localhost o 127.0.0.1 Para ejecutarlos, solo use el siguiente código:

```python
from fakenos import FakeNOS

network = FakeNOS()
network.start()
```

Inicie la conexión SSH utilizando el nombre de usuario predeterminado `user` y la contraseña `user`:

```bash
ssh -p 6000 user@localhost # cisco_ios
ssh -p 6001 user@localhost # huawei_smartax
```

El equivalente a ejecutar el código anterior sería ejecutar la interfaz de usuario de FakeNOS sin argumentos:

```bash
fakenos
```
