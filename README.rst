Installation
------------

.. code-block:: sh

   pip install djld

Usage
-----

.. code-block:: python

   from djld.http import HttpCatResponse

   def my_view():
       return HttpCatResponse(status_code=200)

Run tests
---------

.. code-block:: sh

   $ pip install -r requirements-dev.txt
   $ make test
