#!/usr/bin/python
# -*- coding: utf-8 -*-

import ast
from wensleydale import parser


def test_int():
    '''
    An int object is properly decoded.
    '''
    # Create fake data.
    obj = ast.parse('a = 1')

    # Run the test.
    result = parser.dictify(obj)

    # Check the result.
    assert result['body'][0]['lineno'] == 1
