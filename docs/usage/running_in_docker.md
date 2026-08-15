# Running in a Docker Container

FakeNOS publishes a pre-built image in the [Docker Hub repository](https://hub.docker.com/r/fakenos/fakenos).

## Build and run with Docker Compose

The repository also includes `docker/docker-compose.yaml`, `docker/Dockerfile`, and
`docker/inventory.yaml` for a local two-device example.

```{ .bash .annotate }
git clone https://github.com/fakenos/fakenos.git  # (1)
cd fakenos/docker                                # (2)
docker compose up -d --build                     # (3)
ssh -p 12723 user@localhost                      # (4)
```

1. Clone the FakeNOS repository.
2. Enter its Docker directory.
3. Build and start the service in detached mode.
4. Connect to the first replica. The second replica is exposed on local port `12724`.

The bundled inventory creates two Cisco IOS replicas:

```yaml
hosts:
  fakerouter:
    username: user
    password: user
    port:
      - 6001
      - 6002
    replicas: 2
    platform: cisco_ios
```

The inventory is copied into the image during the build. After changing it, rebuild and restart
the service with `docker compose up -d --build`.
