Wensleydale
===========

Mr Wensleydale. Query Python, get the AST as JSON.

Why?
----

The :py:mod:`ast`, or abstract syntax tree, is a set of data structures that
describe your python script. By exposing the AST to json, it can be treated as
data, which means it can be reported on.

Sample use cases include:

* Visualizing the routing tree of a web application.
* Visualizing a class hierarchy.
* Auditing large code bases using queries.

Support
-------

Currently only Python 3.5 is supported.

Upcoming features:

* *Recursive imports:* Trace into calls.
* *Pythonic paths:* Use python dotted paths instead of file paths.
