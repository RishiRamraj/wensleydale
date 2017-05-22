#!/usr/bin/env python

import click


@click.command()
@click.argument('path', type=str)
@click.argument('query', type=str)
@click.option('--level', type=str, help='Logging level to run with')
@click.option('--version', type=str, help='Wensleydale version to run with')
def run(path, query, level=None, version=None):
    pass
