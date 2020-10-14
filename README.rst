======================
fatal_police_shootings
======================


.. image:: https://img.shields.io/pypi/v/fatal_police_shootings.svg
        :target: https://pypi.python.org/pypi/fatal_police_shootings

.. image:: https://img.shields.io/travis/farisachugthai/fatal_police_shootings.svg
        :target: https://travis-ci.com/farisachugthai/fatal_police_shootings

.. image:: https://readthedocs.org/projects/fatal-police-shootings/badge/?version=latest
        :target: https://fatal-police-shootings.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/farisachugthai/fatal_police_shootings/shield.svg
     :target: https://pyup.io/repos/github/farisachugthai/fatal_police_shootings/
     :alt: Updates

* Free software: MIT license
* Documentation: https://fatal-police-shootings.readthedocs.io.


Features
--------

Rough template for analyzing the data found at 538 aggregated
on fatal police shootings from 2015 to 2020.


Running the Tests
-----------------

.. warning::
   Running the tests currently is a little odd.

The tests need to be run in an exact way so that pytest can maintain
it's typical ``rootdir`` setup but still find the csv file correctly.

Run the following in a shell of your choice.

.. code-block:: bash

   cd fatal_police_shootings
   pytest ../tests/test_fatal_police_shootings.py

And the tests will pass.


Credits
-------

This package was created with Cookiecutter_ and the
`farisachugthai/cookiecutter-lib`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`farisachugthai/cookiecutter-lib`: https://github.com/farisachugthai/cookiecutter-lib
