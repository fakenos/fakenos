# Github actions
Un característica molt interessant de tenir sempre és una plataforma totalment automatitzada que provi el codi en múltiples plataformes alhora. En aquest cas estem utilitzant Github Actions per fer-ho. La configuració es troba a la carpeta `.github/workflows`.

## Fluxe de treball actuals
Actualment, hi ha 2 fluxe de treball:

- `docs.yml`: Desplega automàticament una documentació actualitzada a la branca `gh-pages`.
- ``main.yml`: Assegura la correcció del codi. Executa la suite de proves completa en múltiples plataformes (Linux, MacOS i Windows) i també comprova l'estil del codi.

## Proves de fluxe de treball localment

En el cas que vulgueu canviar qualsevol dels fluxes de treball, en lloc de fer 1000 sol·licituds de tirada o compromisos per provar-ho, és possible (i recomanable) executar els fluxes de treball localment. Per fer-ho, heu d'instal·lar el paquet `act`. Consulteu la seva [documentació oficial](https://nektosact.com/) per obtenir més informació. Amb la comanda `act` podeu executar els fluxes de treball localment. Això és tot!

!!! tip
    La comanda completa és: **`act -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest`**

!!! failure
    Actualment, l'executor per defecte no funciona. Es recomana utilitzar el `ghcr.io/catthehacker/ubuntu:act-latest`. Per tant, la comanda completa és `act -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest`. En aquest cas la imatge és molt més gran... però funciona. També vegeu aquest [avís de Github](https://github.blog/changelog/2024-03-07-github-actions-all-actions-will-run-on-node20-instead-of-node16-by-default/).