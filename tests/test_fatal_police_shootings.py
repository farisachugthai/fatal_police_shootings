#!/usr/bin/env python
"""Tests for `fatal_police_shootings` package."""
import pytest

from fatal_police_shootings import core
@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

if __name__ == "__main__":
    pytest.main()

# Vim: set ft=jinja.python:
