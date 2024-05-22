# Afegir noves plataformes
FakeNOS està dissenyat per ser fàcilment extensible. Està dissenyat de manera que afegir noves plataformes sigui senzill i es pugui fer utilitzant diferents mètodes. De moment, només és possible utilitzant mòduls de Python o fitxers YAML.

!!! tip
    Hi ha implementat un hot-reloader que recarrega automàticament els mòduls de Python i YAML quan es modifiquen dins de `fakenos/plugins/nos`. Per executar-lo simplement fer `fakenos --reload-commands`.

## Fitxers YAML
Aquest és el mètode preferit en cas que la plataforma que voleu implementar encara no existeixi. El gran avantatge d'aquest mètode és que és bastant senzill afegir noves plataformes. No obstant això, no és tan flexible com el mètode de mòduls de Python ja que no és possible implementar un comportament dinàmic.

Els fitxers YAML es troben al directori `fakenos/plugins/nos/platforms_yaml`.

## Mòduls de Python
Aquest mètode és més flexible que el mètode de fitxers YAML. És possible implementar un comportament dinàmic i utilitzar tot el potencial de Python. No obstant això, és una mica més difícil d'implementar. Els mòduls de Python es troben al paquet `fakenos/plugins/nos/platforms_py`.