Executar FakeNOS en un contenedor permite muchos casos de uso de integración.

## Executar amb Docker

Contenedor pre-construido de FakeNOS publicado en
[repositorio DockerHUB](https://hub.docker.com/r/fakenos/fakenos)


## Construir y Executar amb Docker-Compose

El repositorio de GitHub de FakeNOS contiene archivos `docker-compose` y `Docker` para construir
y iniciar FakeNOS en un contenedor. Para utilizarlo, siempre que ya tengas instalado
[Docker](https://docs.docker.com/engine/install/),
[Docker-Compose](https://docs.docker.com/compose/install/) y
[GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) en el sistema:

```{ .bash .annotate }
git clone https://github.com/fakenos/fakenos.git   # (1)
cd fakenos/docker/                                # (2)
docker-compose up -d                              # (3)
ssh 10.100.0.2 -l user -p 6001                       # (4)
```

1. Clona el repositorio de FakeNOS de GitHub
2. Navega hasta la carpeta docker de fakenos
3. Construye e inicia el contenedor en modo desconectado (`-d`)
4. Inicia la conexión SSH al router FakeNOS

El contenedor `fakenos` utiliza por defecto la IP `10.100.0.2` como se especifica en `docker-compose.yaml`.

La carpeta `fakenos/docker/` contiene el archivo `fakenos_inventory.yaml`, con el inventario
que se utiliza para iniciar FakeNOS dentro de un contenedor:

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

Ajusta la configuración del inventario antes de ejecutar el contenedor o actualiza el contenido del inventario
y reinicia el contenedor `fakenos` para aplicar los cambios - `docker restart fakenos`

El archivo de inventario está ligado al contenedor `fakenos` como un `volume` en el archivo docker-compose,
como resultado cualquier cambio en el archivo `fakenos_inventory.yaml` es visible por el proceso `fakenos`
corriendo dentro del contenedor.
