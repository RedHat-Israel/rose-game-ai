"""
This driver does not do any action.
"""

from rose.common import obstacles, actions  # NOQA

driver_name = "MyDriver"


def drive(world):
    return actions.NONE
