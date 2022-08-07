"""
FakeNOS Command Line Tool for running fake servers.
"""

import argparse
import time
import logging

from fakenos import FakeNOS

__version__ = "0.1.0"

log = logging.getLogger(__name__)

# form argparser menu:
description_text = """-i --inventory   OS Path to inventory file
"""

argparser = argparse.ArgumentParser(
    description="FakeNOS, version {}".format(__version__),
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
opts = argparser.add_argument_group(description=description_text)

opts.add_argument(
    "-i",
    "--inventory",
    action="store",
    dest="INVENTORY",
    default=None,
    type=str,
    help=argparse.SUPPRESS,
)


# extract argparser arguments:
args = argparser.parse_args()
INVENTORY = args.INVENTORY


def run_cli():
    """Function to start FakeNOS CLI"""
    fakenet = FakeNOS(inventory=INVENTORY)
    fakenet.start()
    print("Started servers:")
    print(fakenet.list_hosts())
    log.info("FakeNOS Started servers: {}".format(fakenet.list_hosts()))


if __name__ == "__main__":
    run_cli()
