#!/usr/bin/env python

from __future__ import print_function
import json
import click
import objectpath
from wensleydale import parser


@click.command()
@click.argument('path', type=str)
@click.argument('query', type=str)
@click.option('--level', type=str, help='Logging level to run with')
@click.option('--version', type=str, help='Wensleydale version to run with')
def run(path, query, level=None, version=None):
    '''
    Mr Wensleydale. Query the AST using ObjectPath and return JSON.
    '''
    # Load the file.
    node = parser.parse_file(path)

    # Convert it to objects.
    objs = parser.dictify(node)

    # Run the query.
    result = objectpath.Tree(objs).execute(query)

    # Spit out the result.
    print(json.dumps(result))
