# Release Notes

## 1.2.1

### Bug Fixes

- Bundled Python platform configurations now resolve from the installed package instead of failing outside the repository root.

## 1.2.0

### Features

- Custom NOS plugins can now run with a built-in platform or without platform metadata.
- All bundled YAML platform definitions are now available for inventory platform validation.

### Changes

- Inventory defaults now merge recursively while preserving explicit host and default NOS choices.
- Replica names and ports now use deterministic ordered mappings.
- Development commands, CI configuration, and contributor documentation now follow the current `uv`, Ruff, and Zensical workflow.

### Bug Fixes

- Server shutdown now closes active SSH transports and joins only threads owned by each server.
- Shell output now preserves literal braces while replacing only the supported `{base_prompt}` token.
- Invoke tasks now avoid unsupported PTY handling on Windows.
- CLI startup failures now clean up partially started FakeNOS instances.

### Miscellaneous

- Documentation wording, navigation, examples, and broken links were improved and corrected.
- Type annotations were corrected and expanded across core runtime and development tooling.
- Various dead, unused, and redundant code paths were removed.
