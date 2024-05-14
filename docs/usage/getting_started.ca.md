# Ús bàsic
FakeNOS està construit amb alguns hosts per defecte que s'utilitzen en cas que no s'indiqui cap `inventari`. En aquest cas, s'obrirà el següent:

- **router_cisco_ios**: un dispositiu amb nom d'usuari `user` i contrasenya `user` al port 6000. La plataforma és `cisco_ios`.
- **router_huawei_smartax**: un dispositiu amb nom d'usuari `user` i contrasenya `user` al port 6001. La plataforma és `huawei_smartax`.
- **router_arista_eos**: un dispositiu amb nom d'usuari `user` i contrasenya `user` al port 6002. La plataforma és `arista_eos`.

En ambdós casos, els dispositius falsos s'estan executant a l'adreça localhost o 127.0.0.1. Per executar-los, només cal utilitzar el següent codi:

```python
from fakenos import FakeNOS

network = FakeNOS()
network.start()
```

Inicieu la connexió SSH utilitzant el nom d'usuari per defecte `user` i la contrasenya `user`:

```bash
ssh -p 6000 user@localhost # cisco_ios
ssh -p 6001 user@localhost # huawei_smartax
```

L'equivalent d'executar el codi anterior seria executar la interfície d'usuari de FakeNOS sense cap argument:

```bash
fakenos
```
