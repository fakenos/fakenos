# From PyPI using PIP

FakeNOS published to PyPI, to install it using PIP run:

`python3 -m pip install fakenos`

# From GitHub master branch

Install [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), next
install from GitHub master branch:

`python3 -m pip install git+https://github.com/dmulyalin/fakenos`

# Using Poetry

FakeNOS uses Python [Poetry](https://python-poetry.org/) to manage dependencies and 
virtual environments. Follow steps below to install FakeNOS using Poetry:

``` { .bash .annotate }
python3 -m pip install poetry # (1)
git clone https://github.com/dmulyalin/fakenos # (2)
cd fakenos # (3)
poetry install # (4)
```

1.  Install Poetry
2.  Clone FakeNOS repository from GitHub master branch
3.  Navigate to fakenos folder
4.  Run poetry to create virtual environment and install dependencies
