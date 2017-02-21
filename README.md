Development
-----------
To start developing:

    ./build -e dev
    ./.tox/dev/bin/example help

Adding commands is easy:

    $ ./.tox/dev/bin/example create-command new-command
    Created new file: example/commands/new_command.py
    $ ./.tox/dev/bin/example new-command
    Hello, you just ran new-command!

To package as a single [pex executable](https://github.com/pantsbuild/pex):

    ./build -e package
    scp example.pex ...

To run the tests

    ./build

Notes
-----
For historical reasons, here is how the 'build' file was created:

    virtualenv -p python2 venv && \
    source venv/bin/activate && \
    pip install pex && \
    pex tox -c tox -o build && \
    deactivate && \
    rm -rf venv
