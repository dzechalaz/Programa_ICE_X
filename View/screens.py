# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.slider_menu_screen import SliderMenuScreenModel
from Controller.slider_menu_screen import SliderMenuScreenController

from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController

from Model.slider_menu_screen_topping import SliderMenuScreenModelTopping

from Model.model import AnimationScreenModel
from Controller.controller import Controller

from Model.slider_menu_screen_recipiente import SliderMenuScreenModelRecipiente

screens = {
    "animation": {
        "model": AnimationScreenModel,
        "controller": Controller,
    },
    "recipiente": {
        "model": SliderMenuScreenModelRecipiente,
        "controller": SliderMenuScreenController,
    },
    "slider menu screen": {
        
        "model": SliderMenuScreenModel,  # class of model
        "controller": SliderMenuScreenController,  # class of controller
    },    
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
    "topping": {
        "model": SliderMenuScreenModelTopping,
        "controller": SliderMenuScreenController,
    },
}
