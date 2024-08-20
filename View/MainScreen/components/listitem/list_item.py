from kivymd.uix.list import (
    BaseListItem,
    IRightBodyTouch,
    OneLineRightIconListItem,
    TwoLineRightIconListItem,
)
from kivy.properties import BooleanProperty

from kivymd.uix.selectioncontrol import MDSwitch


class BaseListItemWithSwitch(BaseListItem):
    """Base class for one-line and two-line items in thw settings list."""

    active = BooleanProperty(False)  # active/inactive switch


class RightSwitchContainer(IRightBodyTouch, MDSwitch):
    """
    The class implements a container for placing the switch on the right side
    of the settings list item.
    """


class OneLineListItemWithSwitch(OneLineRightIconListItem, BaseListItemWithSwitch):
    """The class implements a one-line item of the settings list."""


class TwoLineListItemWithSwitch(TwoLineRightIconListItem, BaseListItemWithSwitch):
    """The class implements a two-line item of the settings list."""
