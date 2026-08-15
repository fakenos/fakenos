# Documentation

Documentation source is stored under `docs/`, with navigation and theme configuration in
`zensical.toml`.

Build the site with:

```bash
uv run zensical build --clean
```

Serve it locally with:

```bash
uv run invoke docs --local
```

When adding or moving a page, update the navigation in `zensical.toml` and use links that are
relative to the Markdown file containing them.
