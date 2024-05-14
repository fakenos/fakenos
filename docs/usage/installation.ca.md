# Instal·lació

## PyPi (Recomanat)
FakeNOS ha estat publicat a PyPi. Per instal·lar-lo amb `pip` només cal executar la següent comanda
```bash
python3 -m pip install fakenos
```

## Git
Els següents mètodes no es recomanen a menys que estiguis fent desenvolupament. Si aquest és el cas, llavors recomanem seguir el mètode `poetry`, ja que té totes les característiques i et facilitarà el procés de desenvolupament.

### Utilitzant pip
Abans d'instal·lar d'aquesta manera, cal descarregar i instal·lar [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Si ja has instal·lat `git` només cal executar la següent comanda:
```bash
python3 -m pip install git+https://github.com/fakenos/fakenos
```

# Utilitzant poetry (Recomanat per a desenvolupadors)
FakeNOS utilitza [Poetry](https://python-poetry.org/) per gestionar les dependències i els entorns virtuals. Segueix els passos següents per instal·lar FakeNOS utilitzant Poetry:

```{ .bash .annotate }
python3 -m pip install poetry                  # (1)
git clone https://github.com/fakenos/fakenos # (2)
cd fakenos                                     # (3)
poetry install                                 # (4)
```

1.  Instal·la Poetry
2.  Clona el repositori de FakeNOS de la branca principal de GitHub
3.  Navega fins a la carpeta fakenos
4.  Executa poetry per crear l'entorn virtual i instal·lar les dependències