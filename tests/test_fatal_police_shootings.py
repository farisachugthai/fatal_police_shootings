#!/usr/bin/env python
"""Tests for `fatal_police_shootings` package."""
import pytest

from fatal_police_shootings import core


def test_main():
    shootings = core.main()
    assert hasattr(shootings, "dtype")


def test_data_frame():
    df = core.data_frame()
    assert hasattr(df, "date")


if __name__ == "__main__":
    pytest.main()
