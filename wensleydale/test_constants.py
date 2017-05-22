#!/usr/bin/python
# -*- coding: utf-8 -*-

from wensleydale import constants


def test_version():
    '''
    Ensure the version is populated.
    '''
    assert isinstance(constants.VERSION, str)
