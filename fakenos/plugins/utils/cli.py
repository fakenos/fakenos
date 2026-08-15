"""
FakeNOS Command Line Tool for running fake servers.
"""

import argparse
from importlib.metadata import PackageNotFoundError, version
import logging
import os
import time
from typing import Optional, Sequence

from fakenos import FakeNOS

try:
    __version__ = version("fakenos")
except PackageNotFoundError:
    __version__ = "unknown"

log = logging.getLogger(__name__)

DESCRIPTION_TEXT = """-i --inventory   OS Path to inventory file
"""

argparser = argparse.ArgumentParser(
    description=f"FakeNOS, version {__version__}",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
opts = argparser.add_argument_group(description=DESCRIPTION_TEXT)

opts.add_argument(
    "-i",
    "--inventory",
    action="store",
    dest="INVENTORY",
    default=None,
    type=str,
    help=argparse.SUPPRESS,
)

opts.add_argument(
    "-l",
    "--log-level",
    action="store",
    dest="LOG_LEVEL",
    default="INFO",
    type=str,
    help="Log level",
)

opts.add_argument(
    "-r",
    "--reload-commands",
    action="store_true",
    dest="RELOAD_COMMANDS",
    default=False,
    help="Dev mode: Reload commands",
)


def run_cli(argv: Optional[Sequence[str]] = None) -> None:
    """Function to start FakeNOS CLI"""
    args = argparser.parse_args(argv)
    logging.basicConfig(level=args.LOG_LEVEL.upper())
    if args.RELOAD_COMMANDS:
        os.environ["FAKENOS_RELOAD_COMMANDS"] = "ON"

    fakenet = None
    try:
        fakenet = FakeNOS(inventory=args.INVENTORY)
        log.info("Initiating FakeNOS")
        fakenet.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log.info("Shutting down FakeNOS")
    finally:
        if fakenet is not None:
            fakenet.stop()
        if args.RELOAD_COMMANDS:
            os.environ.pop("FAKENOS_RELOAD_COMMANDS", None)


if __name__ == "__main__":
    run_cli()
