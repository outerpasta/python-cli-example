#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
"""
Example cli tool
"""
import argh

from example.commands import COMMANDS

def main():
    """Main entry point for the cli."""
    parser = argh.ArghParser()
    parser.add_commands(COMMANDS)
    parser.description = __doc__
    parser.dispatch()


if __name__ == '__main__':
    main()
