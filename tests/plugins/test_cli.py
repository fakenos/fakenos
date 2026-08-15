"""Tests for the FakeNOS command-line entry point."""

import importlib
import os
import sys
from unittest.mock import patch

import pytest


def test_cli_module_import_does_not_parse_process_arguments(monkeypatch):
    """Importing CLI helpers must not consume pytest or application arguments."""
    monkeypatch.setattr(sys, "argv", ["application", "--unrelated-option"])
    sys.modules.pop("fakenos.plugins.utils.cli", None)

    importlib.import_module("fakenos.plugins.utils.cli")


def test_run_cli_owns_start_stop_and_reload_environment():
    """The entry point parses its own arguments and always stops its network."""
    cli = importlib.import_module("fakenos.plugins.utils.cli")

    with (
        patch.object(cli, "FakeNOS") as mock_fakenos,
        patch.object(cli.time, "sleep", side_effect=KeyboardInterrupt),
    ):
        cli.run_cli(["--inventory", "inventory.yml", "--reload-commands"])

    mock_fakenos.assert_called_once_with(inventory="inventory.yml")
    mock_fakenos.return_value.start.assert_called_once_with()
    mock_fakenos.return_value.stop.assert_called_once_with()
    assert "FAKENOS_RELOAD_COMMANDS" not in os.environ


def test_run_cli_stops_partially_started_network():
    """Startup failures still trigger network cleanup."""
    cli = importlib.import_module("fakenos.plugins.utils.cli")

    with patch.object(cli, "FakeNOS") as mock_fakenos:
        mock_fakenos.return_value.start.side_effect = RuntimeError("startup failed")
        with pytest.raises(RuntimeError, match="startup failed"):
            cli.run_cli([])

    mock_fakenos.return_value.stop.assert_called_once_with()
