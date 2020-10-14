#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main module.

Console script for fatal_police_shootings.
"""
import argparse
import logging
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def _parse_args():
    """Parse arguments given by the user.

    Returns
    -------
    args : :class:`argparse.NameSpace()`
        Arguments provided by the user and handled by argparse.

    """
    parser = argparse.ArgumentParser(
        prog="fatal_police_shootings",
        description=("Load police shooting data and analyze it."),
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
        choices=[10, 20, 30, 40, 50],
        default=None,
        help="Log level. If logging is specified with '-l', defaults to INFO.",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_false",
        help="Shorthand to enable verbose logging and increase level to `debug`.",
    )

    args = parser.parse_args()

    # handle a few of our args
    if args.log_level is None:
        # no LOG_LEVEL specified but -l was specified
        if args.log is True:
            LOG_LEVEL = 30
        else:
            # Don't log
            LOG_LEVEL = 99
    else:
        LOG_LEVEL = args.log_level

    logging.basicConfig(level=LOG_LEVEL)
    return args


def main():
    """Console script for fatal_police_shootings."""
    # Yeah unfortunately this doesn't do much
    # args = _parse_args()

    csv_file = os.path.abspath("./fatal_police_shootings.csv")
    shootings = np.recfromcsv(csv_file, encoding="utf-8")

    return shootings


def data_frame():
    shootings = main()
    df = pd.DataFrame(shootings)
    return df


def plotting():
    """So far nothing done but here's the info!

    Note that returns an np.recarray
    it would probably be a good idea to either specify each columns dtype correctly
    or reformat the data appropriately.

    print(shootings.dtype)

    note: doesnt work. dtypes are all fucked up
    shootings = np.loadtext("fatal_police_shootings.csv", delimiter=",", encoding="utf-8")

    This also does arguably nothing of importance or that makes any sense however
    We raised no errors and it works.
    """
    df = data_frame()
    df.plot(x="date", y="id")
    plt.show()

    return df


def different_plot():
    """Doesn't work and actually crashed my interpreter."""
    df = data_frame()
    df[["id", "date"]].sort_values(
            by=["id", "date"], ascending=True
        ).plot(x="id", y="date", kind="scatter")
    plt.show()
    return df


if __name__ == "__main__":
    sys.exit(plotting())  # pragma: no cover
