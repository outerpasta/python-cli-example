#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
"""
Example cli tool
"""
import sys
import os
import argh

from example.commands import COMMANDS

def main():
    """
    Main entry point for the cli.
    """
    parser = argh.ArghParser()
    parser.add_commands(COMMANDS)
    parser.description = __doc__
    parser.dispatch()


def test_cli():
    """test"""
    from subprocess import check_call
    assert check_call([os.path.join(os.path.split(sys.executable)[0], 'example'), 'help']) == 0


if __name__ == '__main__':
    main()
