"""
FakeNOS Command Line Tool for running fake servers.
"""

import argparse
import logging

from fakenos import FakeNOS

__version__ = "1.0.0"

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


args = argparser.parse_args()

logging.basicConfig(level=args.LOG_LEVEL.upper())


def run_cli():
    """Function to start FakeNOS CLI"""
    print("Initiating FakeNOS")
    fakenet = FakeNOS(inventory=args.INVENTORY)
    log.info("Initiating FakeNOS")
    fakenet.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        log.info("Shutting down FakeNOS")
        fakenet.stop()


if __name__ == "__main__":
    run_cli()
