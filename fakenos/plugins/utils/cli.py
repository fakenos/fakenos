"""
FakeNOS Command Line Tool for running fake servers.
"""

import argparse
import time

from fakenos import FakeNOS

__version__ = "0.1.0"

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
    net = FakeNOS(inventory=INVENTORY)
    net.start()
    print("Started servers:")
    print(net.list_hosts())


if __name__ == "__main__":
    run_cli()
