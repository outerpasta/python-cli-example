from tabulate import tabulate

import example.settings


def settings():
    """
    Display settings data

    Examples::

        $ example create command greeting
    """
    return tabulate(
        [
            ['Barry', '12:30'],
            ['Anne', '11:00']
        ],
        headers=['NAME', 'TIME'],
        tablefmt='fancy_grid'
    )
