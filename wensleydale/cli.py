#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json
import click
from wensleydale import parser


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.argument('query', type=str)
@click.version_option()
def main(path, query):
    '''
    Mr Wensleydale. Query the AST using ObjectPath and return JSON.
    '''
    # Run the query.
    result = parser.run(path, query)

    # Spit out the result.
    print(json.dumps(result))
