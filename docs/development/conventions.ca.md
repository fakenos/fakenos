# Convencions
En aquesta secció s'intenta explicar breument totes les eines utilitzades dins del projecte. Aquestes eines són principalment per assegurar que el codi estigui escrit i provat correctament.

## General: Poetry
Poetry és una eina per gestionar les dependències de Python i empaquetar projectes. Simplifica el procés de gestió de dependències proporcionant una manera consistent i declarativa de especificar-les en un fitxer `pyproject.toml`. Poetry també gestiona la creació de l'entorn virtual, la construcció del paquet i la publicació. Sovint és preferit pels desenvolupadors per la seva facilitat d'ús i integració amb altres eines de l'ecosistema de Python.

Totes les configuracions del projecte es poden trobar al `pyproject.toml`. Aquí teniu algunes comandes bàsiques:

- `poetry install`: utilitzeu-la per instal·lar totes les dependències.
- `poetry update`: utilitzeu-la per actualitzar les dependències.
- `poetry shell`: entra a l'intèrpret creat utilitzant poetry install.

## Tests: Pytest
Pytest és un marc de proves per a Python que facilita l'escriptura de proves senzilles i escalables. Us permet escriure casos de proves com a funcions Python normals, utilitzant assercions per verificar els resultats esperats. Pytest proporciona funcionalitats potents com ara fixtures per configurar entorns de proves, proves parametritzades i connectors per ampliar la funcionalitat. És àmpliament utilitzat a la comunitat de Python per la seva simplicitat, flexibilitat i extens ecosistema de connectors.

Per executar les proves feu el següent:
```bash
pytest
```

## Comprovació de seguretat: Bandit
Bandit és una eina de seguretat per a codi Python que detecta problemes de seguretat i vulnerabilitats comuns. Analitza el codi Python estàticament per identificar possibles amenaces de seguretat com l'ús insegur de mòduls, crides a funcions insegures i riscos de seguretat potencials. Bandit proporciona un conjunt de connectors que comproven diversos problemes de seguretat i es poden integrar fàcilment en fluxos de treball de desenvolupament, ajudant els desenvolupadors a identificar i solucionar problemes de seguretat aviat en el procés de desenvolupament. És una eina valuosa per millorar la postura de seguretat de les aplicacions i llibreries de Python.

Per executar l'eina bandit feu el següent:
```bash
bandit -c pyproject.toml -r .
```

## Formateig bàsic: Black
Black és un formatador de codi Python que formata automàticament el codi Python segons un conjunt estricte de regles de format. Garanteix un estil de codi consistent en un projecte aplicant automàticament el format com la indentació, la longitud de línia i l'espaiat. Black segueix el principi de "format de codi sense configuració", el que significa que aplica les seves regles de format de manera uniforme sense requerir cap configuració o ajust manual. Sovint s'utilitza per imposar un estil de codi consistent en projectes de Python i per estalviar temps als desenvolupadors mitjançant l'automatització del procés de format del codi.

Per executar l'eina black feu el següent:
```bash
black .
```

## Complexitat i conformitat del codi: Flake8
Flake8 és una eina popular de Python que combina diverses eines de comprovació de codi i estil de Python en un paquet únic. Executa diverses comprovacions en el codi Python per a possibles errors, violacions de l'estil de codi i adhesió a les directrius d'estil PEP 8. Flake8 integra eines com PyFlakes, pycodestyle (anteriorment conegut com a pep8) i comprovador de complexitat McCabe, permetent als desenvolupadors detectar errors i fer complir els estàndards de codificació en el seu codi Python. S'utilitza sovint com a part del flux de treball de desenvolupament per mantenir la qualitat del codi i la llegibilitat.

Per executar flake8 feu el següent:
```bash
flake8 .
```

## Linting del codi: Pylint
Pylint és una eina de linting de codi Python que analitza el codi font per a detectar errors de programació, estil de codi i convencions de codificació. Pylint comprova el codi Python per a possibles problemes com a errors de sintaxi, variables no utilitzades, noms de variables no convencionals i altres violacions de les directrius de codificació. És una eina valuosa per millorar la qualitat del codi, identificar problemes de codificació i mantenir la coherència en els estàndards de codificació.

Per executar l'eina pylint feu el següent:
```bash
pylint fakenos
```

## Cobertura de codi: coverage
La cobertura és una eina utilitzada en el desenvolupament de programari per mesurar l'extensió a la qual el codi font d'un programa s'executa durant les proves. Ajuda els desenvolupadors a entendre fins a quin punt les seves proves exerceixen el codi font proporcionant mètriques de cobertura de codi, normalment expressades com a percentatge. Les eines de cobertura segueixen quines línies o branques de codi s'executen durant les proves i generen informes que destaquen les àrees que estan cobertes i les que no ho estan. Aquesta informació permet als desenvolupadors identificar camins de codi no provats i millorar l'eficàcia dels seus esforços de proves.

Per executar la cobertura en conjunt amb pytest feu el següent:
```bash
coverage run -m pytest
```

Generarà un informe que es pot veure a `coverage report -m` o `coverage html`.