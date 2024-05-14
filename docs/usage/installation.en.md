# Installation

## PyPi (Recommended)
FakeNOS has been published in PyPi. To install it using `pip` just run the following command
```bash
python3 -m pip install fakenos
```

## Git
The following methods are not recommended unless you are doing development. If this is the case, then we recommend following the `poetry` method, as it has all the features and will make you development process easier.

### Using pip
Before installing this way, you need to download and install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). If you have already installed `git` just run the following command:
```bash
python3 -m pip install git+https://github.com/dmulyalin/fakenos
```

# Using poetry (Recommended for dev)
FakeNOS uses [Poetry](https://python-poetry.org/) to manage dependencies and
virtual environments. Follow steps below to install FakeNOS using Poetry:

```{ .bash .annotate }
python3 -m pip install poetry                  # (1)
git clone https://github.com/dmulyalin/fakenos # (2)
cd fakenos                                     # (3)
poetry install                                 # (4)
```

1.  Install Poetry
2.  Clone FakeNOS repository from GitHub master branch
3.  Navigate to fakenos folder
4.  Run poetry to create virtual environment and install dependencies
