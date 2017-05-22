#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Parse python code into the abstract syntax tree and represent as JSON
'''
from __future__ import print_function
from itertools import chain
import ast


def dictify(obj):
    '''
    Convert an ast object into a a collection of dicts, lists and strings.

    Args:
        obj: An AST object.

    Returns:
        result (dict): A collection of dicts, lists and strings.
    '''
    if hasattr(obj, "__dict__"):
        result = {
            k: dictify(v)
            for k, v in chain(obj.__dict__.items(), [("classname",
                                                      obj.__class__.__name__)])
        }
        return result
    elif isinstance(obj, list):
        return [dictify(x) for x in obj]
    else:
        return obj


def parse_file(filename):
    '''
    Parse a file and convert it to an ast object.

    Args:
        obj: An AST object.

    Returns:
        result (dict): A collection of dicts, lists and strings.
    '''
    with open(filename) as f:
        source = f.read()
        return ast.parse(source, filename=filename, mode="exec")
