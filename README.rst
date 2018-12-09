
Djld
====

Structured data with Django


.. image:: https://img.shields.io/pypi/v/djld.svg
   :target: https://pypi.python.org/pypi/djld/
   :alt: Latest Version


.. image:: https://codecov.io/gh/lotrekagency/djld/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lotrekagency/djld
   :alt: codecov


.. image:: https://travis-ci.org/lotrekagency/djld.svg?branch=master
   :target: https://travis-ci.org/lotrekagency/djld
   :alt: Build Status


.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/lotrekagency/djld/blob/master/LICENSE
   :alt: License: MIT


Installation
------------

.. code-block:: sh

   pip install djld

Configuration
-------------

Add ``djld`` to your INSTALLED_APPS in settings.py, you can specify the folder containing your structured data overriding the ``LD_JSON_PATH`` variable

Usage
-----

To render structured data in your templates you need the ``structured_data`` template tag

.. code-block:: py

   {% load djld %}

   {% structured_data 'mydata.json' %}

You can use Django template sintax in your json files, and pass a context to the template tag

.. code-block:: py

   render(request, 'myapp/index.html', {
       'user_data' : {
           'url' : 'https://lotrek.it',
           'name' : 'Human Before Digital'
       }
   })

.. code-block:: py

   {% load djld %}

   {% structured_data 'mydata.json' user_data %}

You can also render a structured data from a dictionary, without using templates

.. code-block:: py

   render(request, 'myapp/index.html', {
       'user_data' : {
           'url' : 'https://lotrek.it',
           'name' : 'Human Before Digital'
       }
   })

.. code-block:: py

   {% load djld %}

   {% structured_data user_data %}

Run tests
---------

.. code-block:: sh

   $ pip install -r requirements-dev.txt
   $ make test
