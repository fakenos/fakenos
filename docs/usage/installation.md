# Installation

## PyPI (Recommended)

FakeNOS is published on PyPI. Install it with `pip`:

```bash
python3 -m pip install fakenos
```

## Development

For development, clone the main repository and synchronize its dependencies with `uv`.

```{ .bash .annotate }
python3 -m pip install uv                         # (1)
git clone https://github.com/fakenos/fakenos.git  # (2)
cd fakenos                                       # (3)
uv sync                                          # (4)
```

1. Install `uv`.
2. Clone the FakeNOS repository.
3. Enter the repository directory.
4. Create the virtual environment and install project and development dependencies.
