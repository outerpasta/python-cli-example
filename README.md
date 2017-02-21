Development
-----------
To start developing:

    ./build -e dev
    ./.tox/dev/bin/example help

To package as a single pex executable:

    ./build -e package
    ./example.pex help
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
