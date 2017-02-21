"""Import the commands you would like available into this module"""
import types
import sys

from .create_command import create_command


COMMANDS = [
    getattr(sys.modules[__name__], command) for command in dir(sys.modules[__name__])
    if isinstance(getattr(sys.modules[__name__], command), types.FunctionType)
]
