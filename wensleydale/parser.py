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

    return obj


def parse_file(path):
    '''
    Parse a file and convert it to an ast object.

    Args:
        path (str): Path to a python file.

    Returns:
        result (ast.AST): An AST node.
    '''
    with open(path) as file:
        return ast.parse(file.read(), filename=path, mode="exec")


def run(path):
    '''
    Run the AST parser and return the result.

    Args:
        path: The python file you want to load.

    Returns:
        result (dict): A collection of dicts, lists and strings.
    '''
    return dictify(parse_file(path))
