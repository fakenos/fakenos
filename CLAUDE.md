# CLAUDE.md

This file gives Claude Code the key context needed to work productively in this repository.

## Project Overview

FakeNOS is a Python package for simulating network operating system CLI interactions. It starts fake SSH-accessible network devices and returns predefined or dynamically generated command output, making it useful for testing network automation without real routers, switches, or NOS VMs.

The project intentionally sits between unit-test mocks and full integration labs. It exercises connection establishment, SSH login, prompts, shells, and command responses, but it does not emulate network control, data, or management planes. Do not model it as a protocol emulator for BGP, LLDP, forwarding, routing, or vendor OS internals.

The public entry point is `FakeNOS`, exported from `fakenos/__init__.py` and implemented in `fakenos/core/fakenos.py`. The package also provides a `fakenos` test decorator and a `fakenos` CLI command via `fakenos.plugins.utils.cli:run_cli`.

Package metadata is in `pyproject.toml`:

- Package name: `fakenos`
- Current version: `1.1.0`
- Python support: `>=3.11,<3.15`
- Build backend: `uv_build`
- Core dependencies: `paramiko`, `pyyaml`, `pydantic`, `jinja2`, `detect`, `tomli`
- Dev dependencies include `pytest`, `pytest-timeout`, `pytest-repeat`, `ruff`, `bandit`, `coverage`, `invoke`, `netmiko`, docs tooling, and YAML tooling

## Repository Layout

- `fakenos/core/`: core framework classes and validation.
  - `fakenos.py`: `FakeNOS`, default inventory, lifecycle methods, plugin registration, test decorator.
  - `host.py`: host object that wires together server, shell, and NOS plugins.
  - `nos.py`: base NOS plugin loader for YAML and Python plugin files.
  - `servers.py`: base TCP server abstraction.
  - `pydantic_models.py`: inventory, host, server, shell, and NOS validation models.
- `fakenos/plugins/`: built-in plugin systems.
  - `servers/ssh_server_paramiko.py`: Paramiko-backed SSH server plugin.
  - `shell/cmd_shell.py`: command shell implementation.
  - `nos/platforms_yaml/`: YAML platform definitions.
  - `nos/platforms_py/`: Python-backed dynamic platform definitions and templates.
- `tests/`: pytest suite split into `core` and `plugins`.
- `tests/assets/`: test inventories, test NOS modules, YAML fixtures, and SSH test keys.
- `docs/`: Zensical/MkDocs documentation source.
- `tasks.py`: Invoke tasks for linting, tests, docs, Docker image build, and Netmiko checks.
- `docker/`: Dockerfile and compose file for container-based FakeNOS testing.

## Development Setup

CI uses `uv`, so prefer it when available:

```bash
uv sync --all-groups
```

Then run commands through `uv run`, for example:

```bash
uv run pytest
```

This repository also contains `poetry.lock`, and older docs mention Poetry. Treat Poetry as a legacy-compatible workflow unless you are specifically maintaining those docs. The current CI and build backend are `uv`-oriented.

## Running Tests

Run the whole pytest suite:

```bash
uv run pytest
```

If dependencies are already installed in the active environment, this also works:

```bash
python -m pytest
```

Run a specific test file:

```bash
uv run pytest tests/core/test_fakenos.py
```

Run a specific test:

```bash
uv run pytest tests/core/test_netmiko.py::TestNetmiko::test_testing_module
```

Run with coverage:

```bash
uv run coverage run -m pytest
uv run coverage report -m
uv run coverage html
```

Pytest configuration is in `pyproject.toml`; it sets `testpaths = ["tests"]` and `addopts = "-vv"`.

## Full Local Checks

The CI gates are Ruff, Bandit, and pytest. Run them locally with Invoke:

```bash
uv run invoke ruff --local
uv run invoke bandit --local
uv run invoke pytest --local
```

Or run the combined task:

```bash
uv run invoke tests --local
```

Important: Invoke tasks default to Docker execution unless `--local` is passed or `INVOKE_LOCAL=True` is set. On PowerShell:

```powershell
$env:INVOKE_LOCAL = "True"
uv run invoke tests
```

Without local mode, `invoke tests` expects the project Docker image to exist. Build it with:

```bash
uv run invoke build
```

The combined `tests` task currently runs Ruff, Bandit, and pytest. The YAML lint task exists but is commented out in `tasks.py` and disabled in CI.

## Invoke Tasks Reference

`tasks.py` defines project automation with Invoke. Run tasks as:

```bash
uv run invoke <task-name>
```

Most command-running tasks accept `--local`. Without `--local`, they run inside the Docker image named from `pyproject.toml` and tagged as `<version>-py<PYTHON_VER>`. Defaults are:

- `PYTHON_VER=3.14`
- `IMAGE_NAME=fakenos`
- `IMAGE_VER=1.1.0-py3.14`
- `INVOKE_LOCAL=False`

Environment variables can override these values.

Available tasks:

- `build`: builds the root `Dockerfile` image using `PYTHON_VER` as a build argument. Options: `--cache/--no-cache`, `--force-rm`, and `--hide`.
- `clean`: force-removes the project Docker image for the current `IMAGE_NAME:IMAGE_VER`.
- `rebuild`: runs `clean`, then rebuilds the Docker image without cache.
- `pytest`: runs `pytest`.
- `ruff`: runs `ruff check --diff`, then `ruff format --diff`.
- `yamllint`: runs `yamllint .`. This exists, but it is not part of the combined `tests` task right now.
- `bandit`: runs `bandit -c pyproject.toml --recursive ./`.
- `cli`: opens an interactive Bash shell inside the project Docker image with the repo mounted at `/local`.
- `tests`: runs the standard local quality gate: `ruff`, `bandit`, then `pytest`. It prints a success message after all pass.
- `docs`: serves docs with `mkdocs serve -v --dev-addr=0.0.0.0:8001`; in Docker mode it maps host port `8001` to container port `8001`.
- `gen-docs-platform-commands`: generates per-platform docs from platform YAML command definitions. Check this before using it: the current task points at `fakenos/plugins/nos/platforms`, while this repo currently stores YAML platforms in `fakenos/plugins/nos/platforms_yaml`.
- `netmiko-check`: starts one FakeNOS host for a supplied Netmiko `device_type`, connects with Netmiko to `localhost:6000`, waits briefly, stops FakeNOS, and prints success plus elapsed time. Example:

```bash
uv run invoke netmiko-check --device-type cisco_ios
```

## Test Notes And Gotchas

- Several tests start local TCP/SSH servers and use free or fixed localhost ports. Avoid running multiple full test suites in parallel on the same machine.
- Netmiko compatibility tests start FakeNOS instances and connect through SSH. These depend on `netmiko`, `paramiko`, and the platform definitions matching Netmiko expectations.
- Docker tests use `docker/docker-compose.yaml` and are skipped when Docker is unavailable. Locally, if Docker is running, those tests may build/start containers.
- Thread cleanup is important. `FakeNOS.stop()` joins non-main threads, and tests assert expected thread counts. Always stop networks in tests, preferably with `with FakeNOS(...)`.
- Default hosts are `router_cisco_ios` on port `6000`, `router_huawei_smartax` on port `6001`, and `router_arista_eos` on port `6002`, using username/password `user`/`user`.

## Linting And Formatting

Primary lint configuration is in `pyproject.toml` under Ruff:

```bash
uv run ruff check --diff
uv run ruff format --diff
```

The Invoke task runs those same diff-only checks:

```bash
uv run invoke ruff --local
```

Bandit security checks:

```bash
uv run bandit -c pyproject.toml --recursive ./
```

Pre-commit config exists, but it contains older Black/Flake8/Pylint local hooks. Prefer the current CI path unless the task specifically involves pre-commit maintenance.

## Platform Plugin Guidance

Supported platforms are listed in `fakenos/core/nos.py` as `available_platforms`. Tests compare this list with `docs/platforms/index.md` and assert both are alphabetically ordered.

Platform definitions are loaded lazily from:

- `fakenos/plugins/nos/platforms_yaml/*.yaml`
- `fakenos/plugins/nos/platforms_py/*.py`

If a platform has both YAML and Python definitions, both files are loaded, with Python adding dynamic behavior. Python platform modules should follow the pattern in `fakenos/plugins/nos/platforms_py/cisco_ios.py` and use `BaseDevice` when device state, configuration, or Jinja templates are needed.

When adding or changing a platform:

- Keep `available_platforms` sorted.
- Keep `docs/platforms/index.md` sorted and status-marked.
- Add or update tests when Netmiko behavior, prompts, command aliases, or dynamic output changes.
- Watch prompt transitions carefully: command `prompt` filters and `new_prompt` changes are central to shell behavior.

## Inventory Guidance

Inventories may be Python dictionaries or YAML files. They require a top-level `hosts` section and may include a top-level `default` section. Host values override defaults.

Common host fields:

- `username`
- `password`
- `port`
- `platform`
- `replicas`
- `server`
- `shell`
- `nos`
- `configuration_file`

If `replicas` is used, `port` must be a two-item list/range whose size matches the replica count. Without `replicas`, `port` must be an integer.

## Documentation

Docs source is under `docs/`. The documentation is part of the expected contribution surface: when behavior, platform support, CLI usage, inventory options, or plugin workflows change, update docs alongside code and tests.

CI builds documentation with:

```bash
uv run zensical build --clean
```

The Invoke docs task serves docs locally:

```bash
uv run invoke docs --local
```

Docs have multilingual support through filename suffixes. For example, a Spanish translation should use `.es.md`; the docs plugin selects localized files based on the suffix. Keep English source files as the baseline unless intentionally adding a translated variant.

Project overview docs define the mental model:

- FakeNOS is for lightweight network automation testing and development.
- The core flow is client input to server, server to shell, shell to NOS plugin, then command output back to the client.
- The plugin systems are NOS plugins, server plugins, and shell plugins.
- Dynamic output exists for Python-backed platforms, but many command outputs are intentionally predefined and exact-command based.

## Contribution And Conduct

The project follows the Contributor Covenant Code of Conduct in `CODE_OF_CONDUCT.md`. Contributions and reviews should be respectful, inclusive, and constructive. Assume maintainers and contributors are working from limited volunteer time; keep changes focused, explain intent clearly, and make review easy.

Expected contribution shape from the development docs:

- Define a clear goal for the change.
- Include code and tests whenever possible.
- Document user-facing behavior or development workflow changes.
- Run the project checks before submitting: `invoke tests` or, preferably in the current `uv` workflow, `uv run invoke tests --local`.

The Code of Conduct specifically calls for empathy, respectful disagreement, graceful acceptance of feedback, responsibility for mistakes, and focus on what benefits the broader community. It rejects harassment, personal attacks, publication of private information, and other unprofessional conduct. Report Code of Conduct issues to the maintainer address listed in `CODE_OF_CONDUCT.md`.

## CI And Workflow Notes

GitHub Actions live in `.github/workflows/`:

- `main.yml`: runs Ruff, Bandit, and pytest. Pytest is run across Python 3.11, 3.12, 3.13, and 3.14 on Linux, macOS, and Windows.
- `docs.yml`: builds and deploys docs.

When changing workflows, the docs recommend testing locally with `act`:

```bash
act -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest
```

The development docs also mention a command hot-reload mode for platform command development:

```bash
fakenos --reload-commands
```

This sets `FAKENOS_RELOAD_COMMANDS` and reloads changed files under `fakenos/plugins/nos/`. Reloading is additive: new and modified commands appear, but deleted commands require a server restart to disappear.

## Current Local Verification Note

On this machine, `uv` was not installed when this file was created. A direct `python -m pytest --collect-only -q` was attempted with Python 3.11.9 and failed during collection because project dependencies such as `detect`, `paramiko`, and `netmiko` were not installed in the active global environment. Install the project dev dependencies first, then rerun tests.
