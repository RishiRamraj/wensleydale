#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json
import click
from wensleydale import parser


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.version_option()
def main(path):
    '''
    Mr Wensleydale. Query Python, get the AST as JSON.
    '''
    print(json.dumps(parser.run(path)))
