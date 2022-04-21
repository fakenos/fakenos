FakeNOS GitHub repository contains `docker-compose` and `Docker` files to build
and start FakeNOS in a container. To use it, providing that GIT, Docker and
Docker-Compose installed on the system:

1. Clone FakeNOS repository: `git clone https://github.com/dmulyalin/fakenos.git`
2. Build container: `docker-compose up`
3. Access FakeNOS router: `ssh 10.100.0.2 -l user -p 6001`
