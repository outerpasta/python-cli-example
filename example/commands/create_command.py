"""
Create a new sub command.
"""
from os.path import dirname, join
from os import listdir
from textwrap import dedent


def create_command(name):
    """
    Create a new sub command.

    Examples::

        $ example create-command greeting
    """
    commands_init_file = join(dirname(__file__), '__init__.py')
    function_name = name.replace('-', '_')
    file_name = function_name + ".py"

    assert file_name not in listdir(dirname(__file__)), \
        'There already exists a file example/commands/%s' % file_name

    with open(join(dirname(__file__), file_name), 'w') as new_file:
        new_file.write(dedent('''\
        """Module docs"""


        def {function_name}():
            """
            Description for {command_name}

            Examples::

                $ example {command_name}
            """
            return "Hello, you just ran {command_name}!"


        def test_{function_name}():
            """Test for {function_name}"""
            assert {function_name}() == "Hello, you just ran {command_name}!"
        '''.format(function_name=function_name, command_name=name)))

    with open(commands_init_file, 'r') as init_file:
        commands_init_file_lines = init_file.readlines()

    commands_init_file_lines.insert(4, 'from .{0} import {0}\n'.format(function_name))

    with open(commands_init_file, 'w') as init_file:
        for line in commands_init_file_lines:
            init_file.write(line)

    return 'Created new file: example/commands/%s' % file_name
