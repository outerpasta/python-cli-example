#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
"""
Example cli tool
"""
import types
import sys
import os

import argh
import example.commands 


def main():
    """
    Main entry point for the cli.
    """
    parser = argh.ArghParser()
    parser.description = __doc__
    parser.add_commands(_get_commands(example.commands.__name__))
    
    module_names = []
    for namespace in dir(example.commands):
        if not namespace.startswith('_'):
            module_names.append(getattr(example.commands, namespace).__name__)

    for module_name in module_names:
        namespace = module_name.split('.')[-1]
        parser.add_commands(
            _get_commands(module_name),
            namespace=namespace,
            namespace_kwargs=dict(
                title=getattr(example.commands, namespace).__doc__
            )
        )

    parser.dispatch()


def _get_commands(name):
    """Gather commands from a module name"""
    commands = []
    for command in dir(sys.modules[name]):
        func = getattr(sys.modules[name], command)
        if not command.startswith('_') and isinstance(func, types.FunctionType):
            commands.append(func)
    return commands


def test_cli():
    """test"""
    from subprocess import check_call
    assert check_call([os.path.join(os.path.split(sys.executable)[0], 'example'), 'help']) == 0


if __name__ == '__main__':
    main()
