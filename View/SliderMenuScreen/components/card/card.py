from kivy.properties import StringProperty, NumericProperty
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.templates import ScaleWidget, RotateWidget, StencilWidget


class PizzaImage(Image, ScaleWidget, RotateWidget):
    """The class implements the pizza image in the slide card."""

    angle = NumericProperty(0)
    scale = NumericProperty(1)


class PizzaCard(MDBoxLayout, StencilWidget):
    """The class implements the slide card."""

    pizza_name = StringProperty()
    pizza_description = StringProperty()
    pizza_cost = StringProperty()
    source = StringProperty()
    source_bg = StringProperty()
