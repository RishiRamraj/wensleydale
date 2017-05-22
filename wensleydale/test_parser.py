#!/usr/bin/python
# -*- coding: utf-8 -*-

from ast import parse
from wensleydale import parser

def dparse(string):
    return parser.dictify(parse(string))
def test_int():
    '''
    An int object is properly decoded.
    '''
    int_ast = dparse('1')
    assert int_ast['body'][0]['lineno'] == 1

def test_whitespacing_creates_different_asts():
    'column offset should be preserved in asts'
    properly_whitespaced_loop = dparse('for n in range(5):\n    print(n)'))
    improperly_whitespaced_loop = dparse('for n in range(5):\n print(n)'))
    assert properly_whitespaced_loop != improperly_whitespaced_loop

def shadowing_creates_different_asts():
    """ a class which shadows the AST internal name of a built-in should have a distinct abstract syntax tree
    from the built-in it shadows """
    shadowed_int = dparse('Num(1)')
    normal_int = dparse('1')
    assert shadowed_int != normal_int
