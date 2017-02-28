Python Example CLi project
==========================
- [Development](#development)
- [Distribute](#distribute)
- [Test](#test)

Development
-----------
- Ensure you have [any version of Python greater than 2.5](http://docs.python-guide.org/en/latest/starting/installation/)
- Install tox.

        pip install -U tox

- Create virtualenv

        tox -e dev

- Run `example` command

        eval "$(./.tox/dev/bin/register-python-argcomplete example)"  # setup shell completion
        ./.tox/dev/bin/example help

Distribute
----------
Package as a single [pex executable](https://github.com/pantsbuild/pex):

    tox -e package

    PEX_VERBOSE=1 ./dist/example            # test it out
    mv dist/example /usr/local/bin/example  # move to usr/local/bin
    scp ./dist/example ...                  # copy to remote machine, etc.

Test
----
Run tests

    tox
