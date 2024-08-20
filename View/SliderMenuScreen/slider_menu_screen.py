import os
from typing import Union, NoReturn

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ObjectProperty

from kivymd.uix.button import MDRoundFlatButton

# For hinting.
from kivymd.uix.carousel import MDCarousel

from kivymd.uix.screen import MDScreen

from View.SliderMenuScreen.components import PizzaCard
from View.SliderMenuScreen.components.card_topping.card_topping import ToppingCard
from View.SliderMenuScreen.components.card_recipiente.card_recipiente import RecipienteCard

from Utility.observer import Observer

from kivy.app import App

class SliderMenuScreenView(MDScreen, Observer):

    controller = ObjectProperty()

    model = ObjectProperty()

    manager_screens = ObjectProperty()


    _cursor_pos_x = 0

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.current_slide = 0



    def generate_and_added_slides_to_carousel(self):
        for pizza_name in self.model.pizza_description.keys():
            
            pizza_name = pizza_name.lower()
            scale = 1 if pizza_name == "mexican" else 2
            
            if pizza_name == "chispas_de_chocolate" or pizza_name == "chispas_de_vainilla":
                card = ToppingCard(
                    pizza_name=pizza_name.replace("_"," ").capitalize(),
                    pizza_description=self.model.pizza_description[pizza_name.capitalize()][
                        0
                    ],
                    pizza_cost= self.model.pizza_description[pizza_name.capitalize()][1] if pizza_name == "arma_tu_helado" else "$" + self.model.pizza_description[pizza_name.capitalize()][1],
                    source=os.path.join("assets", "images", f"{pizza_name}.png"),
                    source_bg=os.path.join("assets", "images", f"{pizza_name}-bg.png"),
                )
            elif pizza_name == "cono" or pizza_name == "vaso":
                card = RecipienteCard(
                    pizza_name=pizza_name.replace("_"," ").capitalize(),
                    pizza_description=self.model.pizza_description[pizza_name.capitalize()][
                        0
                    ],
                    pizza_cost= self.model.pizza_description[pizza_name.capitalize()][1] if pizza_name == "arma_tu_helado" else "$" + self.model.pizza_description[pizza_name.capitalize()][1],
                    source=os.path.join("assets", "images", f"{pizza_name}.png"),
                    source_bg=os.path.join("assets", "images", f"{pizza_name}-bg.png"),
                )
            # if pizza_name == "arma_tu_helado":
            #     card = ArmarCard(
            #         pizza_name=pizza_name.replace("_"," ").capitalize(),
            #         pizza_description=self.model.pizza_description[pizza_name.capitalize()][
            #             0
            #         ],
            #         pizza_cost= self.model.pizza_description[pizza_name.capitalize()][1] if pizza_name == "arma_tu_helado" else "$" + self.model.pizza_description[pizza_name.capitalize()][1],
            #         source=os.path.join("assets", "images", f"{pizza_name}.png"),
            #         source_bg=os.path.join("assets", "images", f"{pizza_name}-bg.png"),
            #     )
            else:
                card = PizzaCard(
                    pizza_name=pizza_name.replace("_"," ").capitalize(),
                    pizza_description=self.model.pizza_description[pizza_name.capitalize()][
                        0
                    ],
                    pizza_cost= self.model.pizza_description[pizza_name.capitalize()][1] if pizza_name == "arma_tu_helado" else "$" + self.model.pizza_description[pizza_name.capitalize()][1],
                    source=os.path.join("assets", "images", f"{pizza_name}.png"),
                    source_bg=os.path.join("assets", "images", f"{pizza_name}-bg.png"),
                )
                    
            
            
            card.ids.pizza_image.scale = scale
            self.ids.carousel.add_widget(card)

        self.ids.carousel.padding = dp(10)
        self.ids.carousel.spacing = dp(10)
        self.ids.carousel.current_slide.ids.pizza_name.x = dp(20)

    def on_enter(self):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """

        # Checks if slides have already been created.
        if not self.ids.carousel.slides:
            self.generate_and_added_slides_to_carousel()

    def on_index(self, instance, value):
        """
        Callback method called when the index of the carousel changes.
        """
        self.current_slide = value
        
    def do_animation_default_card_properties(
        self,
        carousel: MDCarousel,
        previous_slide: Union[PizzaCard, None],
        current_slide: PizzaCard,
        next_slide: Union[PizzaCard, None],
    ):
        """Called when slides stop (after swipe)."""

        if next_slide:
            Animation(angle=0, scale=1.5, d=0.2).start(next_slide.ids.pizza_image)

    def do_animation_card_content(self, carousel: MDCarousel, progress_value: float):
        direction = self.get_direction_swipe(progress_value)
        self._cursor_pos_x = progress_value
        offset_value = max(min(abs(progress_value) / Window.width, 1), 0)

        if direction == "left":
            # Current slide.
            #carousel.current_slide.ids.image_bg.width += offset_value
            carousel.current_slide.ids.pizza_image.scale = 1.5 - offset_value
            carousel.current_slide.ids.pizza_image.angle = 0
            carousel.current_slide.ids.pizza_name.x = (
                self.width - abs(progress_value - self.width) + dp(20)
            )
            # Next slide.
            if carousel.next_slide:
                carousel.next_slide.ids.image_bg.width += offset_value
                carousel.next_slide.ids.pizza_image.scale = 2.5 - offset_value
                #carousel.next_slide.ids.pizza_image.angle = offset_value
                carousel.next_slide.ids.pizza_name.x = (
                    self.width - abs(progress_value) + dp(20)
                )
            # Previous slide.
            if carousel.previous_slide:
                #carousel.previous_slide.ids.image_bg.width += offset_value
                carousel.previous_slide.ids.pizza_image.scale = 2.5 - offset_value
                #carousel.previous_slide.ids.pizza_image.angle += offset_value
                carousel.previous_slide.ids.pizza_name.x = dp(20) - abs(progress_value)
        elif direction == "right":
            # Current slide.
            #carousel.current_slide.ids.image_bg.width -= offset_value
            carousel.current_slide.ids.pizza_image.scale = 1.5 - offset_value
            #carousel.current_slide.ids.pizza_image.angle = 0
            carousel.current_slide.ids.pizza_name.x = (
                self.width - abs(progress_value - self.width) + dp(20)
            )
            # Next slide.
            if carousel.next_slide:
                #carousel.next_slide.ids.image_bg.width -= offset_value
                carousel.next_slide.ids.pizza_image.scale = 2.5 - offset_value
                #carousel.next_slide.ids.pizza_image.angle -= offset_value
            # Previous slide.
            if carousel.previous_slide:
                #carousel.previous_slide.ids.image_bg.width -= offset_value
                carousel.previous_slide.ids.pizza_image.scale = 2.5 - offset_value
                #carousel.previous_slide.ids.pizza_image.angle -= offset_value
                carousel.previous_slide.ids.pizza_name.x = -(
                    self.width - (progress_value + dp(20))
                )

    def get_direction_swipe(self, progress_value: float) -> str:
        if self._cursor_pos_x > progress_value:
            direction = "left"
        else:
            direction = "right"
        return direction

    def model_is_changed(self) -> NoReturn:
        """
        The method that will be called on the observer when the model changes.
        """
