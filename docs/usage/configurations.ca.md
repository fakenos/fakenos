# Configuracions
Un dels aspectes més guays de FakeNOS és que pots configurar els dispositius abans d'iniciar. Això serveix per exemple per especificar quina adreça IP té una interfície, o quines VLANs estan permeses en un port. Per defecte hi ha uns valors predefinits, però també pots canviar-los per adaptar-los a les teves necessitats.

Els arxius de configuració estan molt personalitzats per a cada marca i dispositiu, per la qual cosa, encara que estàs lliure de configurar-ho com vulguis, només canviar els valors finals de les variables és el més recomanable. Per poder utilitzar el teu propi arxiu de configuració, simplement has d'especificar la ruta a l'arxiu a l'arxiu de configuració de FakeNOS. Aquí tens un exemple:

```yaml
hosts:
  R1:
    username: user
    password: user
    port: 6000
    platform: cisco_ios
    configuration_file: my_configurations/cisco_ios.yaml.j2
```

En aquest cas, l'arxiu de configuració es troba a la carpeta `my_configurations` i es diu `cisco_ios.yaml.j2`.

Actualment FakeNOS accepta les configuracions en les següents plataformes:
- [cisco_ios](https://github.com/fakenos/fakenos/tree/master/fakenos/plugins/nos/platforms_py/configurations/cisco_ios.yaml.j2)
- [huawei_smartax](https://github.com/fakenos/fakenos/tree/master/fakenos/plugins/nos/platforms_py/configurations/huawei_smartax.yaml.j2) 
- [arista_eos](https://github.com/fakenos/fakenos/tree/master/fakenos/plugins/nos/platforms_py/configurations/arista_eos.yaml.j2)