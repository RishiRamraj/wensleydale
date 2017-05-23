#!/usr/bin/python
# -*- coding: utf-8 -*-

import ast
from io import StringIO
from unittest.mock import patch
from wensleydale import parser


def dparse(string):
    '''
    Parse and dictify a string.
    '''
    return parser.dictify(ast.parse(string))


def test_int():
    '''
    An int object is properly decoded.
    '''
    int_ast = dparse('1')
    assert int_ast['body'][0]['lineno'] == 1


def test_whitespacing_creates_different_asts():
    '''
    Column offset should be preserved in asts.
    '''
    properly_whitespaced_loop = dparse('for n in range(5):\n    print(n)')
    improperly_whitespaced_loop = dparse('for n in range(5):\n print(n)')
    assert properly_whitespaced_loop != improperly_whitespaced_loop


def test_shadowing_creates_different_asts():
    '''
    A class which shadows the AST internal name of a built-in should have a
    distinct abstract syntax tree from the built-in it shadows.
    '''
    shadowed_int = dparse('Num(1)')
    normal_int = dparse('1')
    assert shadowed_int != normal_int


@patch('wensleydale.parser.open')
def test_parse_file(open):
    '''
    A file is properly opened and parsed.
    '''
    # Create fake data.
    open.return_value.__enter__.return_value = StringIO('1')
    path = 'path'

    # Run the test.
    result = parser.parse_file(path)

    # Check the result.
    value = parser.dictify(result)['body'][0]['value']
    assert value['classname'] == 'Num'
    assert value['n'] == 1
    assert value


@patch('wensleydale.parser.parse_file')
def test_run(parse_file):
    '''
    An int object is properly decoded.
    '''
    # Create fake data.
    parse_file.return_value = ast.parse('1')
    path = 'path'

    # Run the test.
    result = parser.run(path)

    # Check the result.
    parse_file.assert_called_once_with(path)
    assert result['classname'] == 'Module'
    assert result['body'][0]['classname'] == 'Expr'
    assert result['body'][0]['value']['classname'] == 'Num'
