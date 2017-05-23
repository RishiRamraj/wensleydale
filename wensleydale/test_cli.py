#!/usr/bin/python
# -*- coding: utf-8 -*-

from wensleydale import cli
from click.testing import CliRunner
import json


def test_run():
    '''
    The tool runs end to end.
    '''
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Setup the test.
        with open('test.py', 'w') as file:
            file.write('1')

        # Run the test.
        result = runner.invoke(cli.main, ['test.py'])

    # Check the result.
    assert result.exit_code == 0
    output = json.loads(result.output)
    assert output['classname'] == 'Module'
    assert output['body'][0]['classname'] == 'Expr'
    assert output['body'][0]['value']['classname'] == 'Num'
