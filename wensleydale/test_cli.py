#!/usr/bin/python
# -*- coding: utf-8 -*-

from wensleydale import cli
from click.testing import CliRunner


def test_run():
    '''
    Ensure the version is populated.
    '''
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Setup the test.
        with open('test.py', 'w') as file:
            file.write('a = 1')

        # Run the test.
        result = runner.invoke(cli.main, ['test.py', '$.classname'])

    # Check the result.
    assert result.exit_code == 0
    assert result.output == '"Module"\n'
