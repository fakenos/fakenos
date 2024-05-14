Executar FakeNOS en un contenidor permet molts casos d'ús d'integració.

## Executar amb Docker

Pre-construït contenidor de Docker de FakeNOS publicat a
[repositori DockerHUB](https://hub.docker.com/r/fakenos/fakenos)

## Construir i Executar amb Docker-Compose

El repositori de GitHub de FakeNOS conté fitxers `docker-compose` i `Docker` per construir
i iniciar FakeNOS en un contenidor. Per utilitzar-ho, sempre que ja tinguis instal·lat
[Docker](https://docs.docker.com/engine/install/),
[Docker-Compose](https://docs.docker.com/compose/install/) i
[GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) al sistema:

```{ .bash .annotate }
git clone https://github.com/fakenos/fakenos.git   # (1)
cd fakenos/docker/                                # (2)
docker-compose up -d                              # (3)
ssh 10.100.0.2 -l user -p 6001                    # (4)
```

1. Clona el repositori de FakeNOS de GitHub
2. Navega fins a la carpeta docker de fakenos
3. Construeix i inicia el contenidor en mode desconnectat (`-d`)
4. Inicia la connexió SSH al router FakeNOS

El contenidor `fakenos` utilitza per defecte la IP `10.100.0.2` com s'especifica al `docker-compose.yaml`.

La carpeta `fakenos/docker/` conté el fitxer `fakenos_inventory.yaml`, amb l'inventari
que s'utilitza per iniciar FakeNOS dins d'un contenidor:

```yaml
default:
  username: "user"
  password: "user"
  port: [10000, 60000]
  server:
    plugin: "ParamikoSshServer"
    configuration:
      address: "0.0.0.0"
      timeout: 1
  shell: {plugin: "CMDShell", configuration: {}}
  nos: {plugin: "cisco_ios", configuration: {}}

hosts:
  router: {count: 10, port: [6001, 7000]}
```

Ajusta la configuració de l'inventari abans d'executar el contenidor o actualitza el contingut de l'inventari
i reinicia el contenidor `fakenos` per aplicar els canvis - `docker restart fakenos`

El fitxer d'inventari està lligat al contenidor `fakenos` com a `volume` al fitxer docker-compose,
com a resultat qualsevol canvi al fitxer `fakenos_inventory.yaml` és visible pel procés `fakenos`
que s'està executant dins del contenidor.