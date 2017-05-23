Samples
=======

We are always looking for useful queries. If you find one, please shoot us a
`pull request`:

.. _pull request: https://github.com/RishiRamraj/wensleydale

Test Code
---------

The samples in this document all query the following Python code:

.. code-block:: python

  import this as python


  def main():
      '''
      Print Hello World!
      '''
      assert python
      print('Hello world!')


  if __name__ == '__main__':
      main()

Finding Calls
-------------

To find the list of function calls in this code:

.. code-block:: sh

  $ wensleydale test.py | jq '.. | select(.classname? == "Call") | {name: .func.id, lineno: .lineno}'
  {
    "name": "print",
    "lineno": 9
  }
  {
    "name": "main",
    "lineno": 13
  }

Finding Imports
---------------

To find the list of function calls in this code:

.. code-block:: sh

  $ wensleydale test.py | jq '.. | select(.classname? == "Import") | [{name: .names[].name, alias: .names[].asname}]'
  [
    {
      "name": "this",
      "alias": "python"
    }
  ]
