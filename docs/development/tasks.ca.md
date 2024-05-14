Per tal de facilitar el desenvolupament, s'han desenvolupat diverses tasques petites. Sentiu-vos lliure d'afegir més. Totes aquestes tasques es poden trobar al `tasks.py`. Per executar-les, podeu utilitzar la següent comanda:
```bash
invoke <task_name>
```

Les tasques disponibles són:

-  `tests`: Crearà un contenidor Docker que realitzarà totes les proves necessàries per assegurar que el codi passi totes les proves, convencions de format, etc. Està destinat a ajudar a garantir un bon manteniment del projecte. Hi ha una opció que és `--local` perquè no s'executi en un contenidor Docker.

-  `gen-docs-platform-commands`: Genera automàticament la documentació per a una plataforma. Originalment estava destinat a documentar totes les comandes a la primera versió del projecte, però es pot utilitzar per documentar qualsevol plataforma.

-  `netmiko-check`: Netmiko és una llibrería ampliamente utilitzada en el món de l'automatisme de xarxa. FakeNOS pretén ser utilitzada com una llibrería de testing per aquesta, i com a tal, és important asegurar-se que totes les plataformes disponibles són compatibles amb Netmiko. Aquesta tasca genera un script que es pot utilitzar per provar la compatibilitat d'una plataforma amb Netmiko. Si tot va bé, dirà `Tot correcte! ✅`.