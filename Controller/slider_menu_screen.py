from typing import NoReturn, Union

# For hinting.
from kivymd.uix.carousel import MDCarousel
from View.SliderMenuScreen.components.card.card import PizzaCard

from View.SliderMenuScreen.slider_menu_screen import SliderMenuScreenView

class SliderMenuScreenController:
    """
    The `SliderMenuScreenController` class represents a controller
    implementation. Coordinates work of the view with the model.

    The controller implements the strategy pattern. The controller connects
    to the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = SliderMenuScreenView(controller=self, model=self.model)

    
    def on_slide_complete(
        self,
        instance_carousel: MDCarousel,
        previous_slide: Union[PizzaCard, None],
        current_slide: PizzaCard,
        next_slide: Union[PizzaCard, None],
    ) -> NoReturn:
        """Called when slides stop (after swipe)."""

        self.view.do_animation_default_card_properties(
            instance_carousel, previous_slide, current_slide, next_slide
        )

    def on_slide_progress(
        self, instance_carousel: MDCarousel, progress_value: float
    ) -> NoReturn:
        """
        Called when the user swipes on the screen (the moment the slides move).
        """

        self.view.do_animation_card_content(instance_carousel, progress_value)

    def get_view(self) -> SliderMenuScreenView:
        return self.view
