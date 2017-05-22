#!/usr/bin/python
# -*- coding: utf-8 -*-

from wensleydale import cli
from unittest.mock import patch
from click.testing import CliRunner


@patch('wensleydale.cli.print')
@patch('wensleydale.cli.parser')
def test_run(parser, print):
    '''
    Ensure the version is populated.
    '''
    # Setup the test.
    parser.run.return_value = 'Module'

    # Run the test.
    result = CliRunner().invoke(cli.main, ['path', ''])

    # Check the result.
    assert result.exit_code == 0
    print.assert_called_once_with('"Module"')
