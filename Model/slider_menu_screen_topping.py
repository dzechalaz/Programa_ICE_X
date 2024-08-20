# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.

import os

from Model.dafault_data import get_data, DATA_DIR


class SliderMenuScreenModelTopping:
    """Implements screen logic for pizza variety slides."""

    def __init__(self):
        # Data:
        #  {
        #      'Pizza name': 'Pizza description', ...
        #  }
        self.pizza_description = get_data(
            os.path.join(DATA_DIR, "topping-description.json")
        )
        if not self.pizza_description:
            self.pizza_description = {}
        # List of observer classes. In our case, this will be the
        # `View.SliderMenuScreen.slider_menu_screen.SliderMenuScreenView`
        # class. See `__init__` method of the above class.
        self._observers = []

    def notify_observers(self):
        """
        The method that will be called on the observer when the model changes.
        """

        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
