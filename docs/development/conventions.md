# Conventions

Project configuration lives in `pyproject.toml`, and dependencies are locked in `uv.lock`.

## Environment: uv

Create or update the development environment with:

```bash
uv sync
```

Run project tools through `uv run` so they use the repository environment.

## Tests: pytest

```bash
uv run pytest
```

## Security: Bandit

```bash
uv run bandit -c pyproject.toml --recursive ./
```

## Linting and formatting: Ruff

```bash
uv run ruff check .
uv run ruff format --check
```

Apply automatic fixes and formatting locally with:

```bash
uv run ruff check . --fix
uv run ruff format
```

## Type checking: ty

```bash
uv run ty check fakenos tasks.py update_platforms.py
```

## Pre-commit

The pre-commit configuration runs Ruff, ty, Bandit, and basic repository hygiene checks:

```bash
uv run pre-commit run --all-files
```

## Coverage

```bash
uv run coverage run -m pytest
uv run coverage report -m
```
