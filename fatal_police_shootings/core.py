#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main module.

Console script for fatal_police_shootings.
"""
import argparse
import logging
import sys

import numpy as np

def _parse_args():
    """Parse arguments given by the user.

    Returns
    -------
    args : :class:`argparse.NameSpace()`
        Arguments provided by the user and handled by argparse.

    """
    parser = argparse.ArgumentParser(
        prog="fatal_police_shootings",
        description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    )

    # parser.add_argument('_', nargs='*')

    parser.add_argument(
        "-l",
        "--log",
        action="store_false",
        help="Where to write log records to. Defaults to stdout.",
    )

    parser.add_argument(
        "-ll",
        "--log-level",
        dest="log_level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Log level. If logging is specified with '-l', defaults to INFO.",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_false",
        help="Shorthand to enable verbose logging and increase level to `debug`.",
    )

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        # This is actually annoying
        # raise argparse.ArgumentError(None, "Args not provided.")
        sys.exit()

    args = parser.parse_args()

    # handle a few of our args
    if args.log_level is None:
        # no LOG_LEVEL specified but -l was specified
        if hasattr(args, "log"):
            LOG_LEVEL = "logging.WARNING"
        else:
            # Don't log
            LOG_LEVEL = 99
    else:
        LOG_LEVEL = "logging." + args.log_level

    logging.basicConfig(level=LOG_LEVEL)

    return args


def main():
    """Console script for fatal_police_shootings."""
    args =_parse_args()

    shootings = np.genfromcsv("fatal_police_shootings.csv", encoding="utf-8")
    # so far nothing done but here's the info!
    # note that returns an np.recarray
    # it would probably be a good idea to either specify each columns dtype correctly
    # or reformat the data appropriately.
    print(shootings.dtype)

    # note: doesnt work. dtypes are all fucked up
    # shootings = np.loadtext("fatal_police_shootings.csv", delimiter=",", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

# Vim: set ft=jinja.python:
