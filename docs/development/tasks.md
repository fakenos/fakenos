# Invoke Tasks

Invoke tasks provide shortcuts for common development workflows. They are defined in
`tasks.py` and can be listed with `uv run invoke --list`.

Run a task locally with:

```bash
uv run invoke <task-name> --local
```

The available tasks include:

- `pytest`: Run the pytest suite.
- `ruff`: Check linting and formatting.
- `bandit`: Run the configured security checks.
- `tests`: Run Ruff, Bandit, and pytest.
- `docs`: Serve the Zensical documentation on port 8001.
- `gen-docs-platform-commands`: Generate missing platform command pages from bundled YAML definitions.
- `netmiko-check`: Start one platform and verify that Netmiko can connect to it.

Without `--local`, supported tasks run in the project Docker image. Build that image first with
`uv run invoke build`.
