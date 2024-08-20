from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from Utility.observer import Observer

class BaseScreenView(MDScreen, ThemableBehavior, Observer):
    """
    A base class that implements a visual representation of the model data
    :class:`~Model.main_screen.MainScreenModel`.
    The view class must be inherited from this class.
    """

    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
        self.model.add_observer(self)

