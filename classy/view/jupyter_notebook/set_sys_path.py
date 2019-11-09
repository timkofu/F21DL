"""
Adds the root path of the classy package to sys.path when imported.
"""

import os
import sys


def set_path():
    """ Adds root of package to sys.path """

    sys.path.insert(
        0,
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(os.path.abspath(__file__))
                )
            )
        )
    )


set_path()
