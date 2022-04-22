FROM rockylinux:8

# install misc libs
RUN dnf install -y python3.9 nano tree

# do python libs installation
RUN python3 -m pip install pip setuptools wheel --upgrade

# run FakeNOS installation from local files
COPY . /tmp/fakenos/
RUN python3 -m pip install /tmp/fakenos/ --upgrade

# copy inventory across for initial start
COPY ./docker/fakenos_inventory.yaml /tmp/fakenos_inventory/fakenos_inventory.yaml

ENTRYPOINT fakenos -i /tmp/fakenos_inventory/fakenos_inventory.yaml
