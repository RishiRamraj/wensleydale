Getting Started
===============

Installation
------------

Install wensleydale using pip:

.. code-block:: sh

  $ pip install wensleydale

Usage
-----

.. code-block:: sh

  Usage: wensleydale [OPTIONS] PATH

    Mr Wensleydale. Query Python, get the AST as JSON.

  Options:
    --version  Show the version and exit.
    --help     Show this message and exit.

If we have the following script in a file called *test.py*:

.. code-block:: python

  print('Hello world!')

We can run wensleydale to get the AST, and use *jq* to pretty print the
result:

.. code-block:: sh

  $ wensleydale test.py | jq
  {
    "body": [
      {
        "col_offset": 0,
        "value": {
          "col_offset": 0,
          "args": [
            {
              "col_offset": 6,
              "s": "Hello world!",
              "lineno": 1,
              "classname": "Str"
            }
          ],
          "lineno": 1,
          "func": {
            "col_offset": 0,
            "lineno": 1,
            "id": "print",
            "ctx": {
              "classname": "Load"
            },
            "classname": "Name"
          },
          "keywords": [],
          "classname": "Call"
        },
        "lineno": 1,
        "classname": "Expr"
      }
    ],
    "classname": "Module"
  }

Understanding the AST
---------------------

The *classname* property of the reported dictionaries will map to the
`Abstract Grammar`_ of Python's syntax tree.

To get a full list of class names, using the following jq query:

.. code-block:: sh

  $ wensleydale test.py | jq '.. | .classname?' | sort | uniq
  "Module"
  "Expr"
  "Call"
  "Str"
  "Name"
  "Load"

You can then select details of individual grammars using:

.. code-block:: sh

  $ wensleydale test.py | jq '.. | select(.classname? == "Call")'
  {
    "args": [
      {
        "col_offset": 6,
        "s": "Hello world!",
        "lineno": 1,
        "classname": "Str"
      }
    ],
    "func": {
      "id": "print",
      "col_offset": 0,
      "lineno": 1,
      "ctx": {
        "classname": "Load"
      },
      "classname": "Name"
    },
    "keywords": [],
    "col_offset": 0,
    "classname": "Call",
    "lineno": 1
  }

.. _Abstract Grammar: https://docs.python.org/3.5/library/ast.html#abstract-grammar
