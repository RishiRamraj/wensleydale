#!/usr/bin/env python

from __future__ import print_function
import json
import click
from wensleydale import parser


@click.command()
@click.argument('path', type=str)
@click.argument('query', type=str)
@click.option('--level', type=str, help='Logging level to run with')
@click.option('--version', type=str, help='Wensleydale version to run with')
def main(path, query, level=None, version=None):
    '''
    Mr Wensleydale. Query the AST using ObjectPath and return JSON.
    '''
    # Run the query.
    result = parser.run(path, query)

    # Spit out the result.
    print(json.dumps(result))
