
from kivy.clock import Clock
from kivy.lang import Builder
from Model.model import AnimationScreenModel
from View.AnimationScreen.animation_screen import AnimationScreenView
from kivg import Kivg
import importlib

import View.AnimationScreen.animation_screen

# Recargamos el módulo de la vista para aplicar cambios en caso de hot reload
importlib.reload(View.AnimationScreen.animation_screen)

Builder.load_file('View/AnimationScreen/animation_screen.kv')

class Controller:
    def __init__(self, model):
        self.model = model
        self.animation_screen_model = AnimationScreenModel()
        self.animacion = 1

        # Inicializa las vistas al crear el controlador
        self.animation_screen_view = AnimationScreenView(controller=self, model=self.animation_screen_model, name='animation')

        self.set_kivg_in_animation_screen()
        Clock.schedule_once(lambda dt: self.start_text_animation(), 0)
        self.reset_inactivity_timer()

    def set_kivg_in_animation_screen(self):
        self.animation_screen_view.s = Kivg(self.animation_screen_view.ids.svg_area)

    def start_text_animation(self):
        if self.animation_screen_view.s:
            self.animation_screen_view.s.draw('icons/text.svg', animate=True, fill=True, line_width=1.5)
        Clock.schedule_interval(lambda dt: self.shape_animate('icons/text.svg', 'text_config'), 6)

    def shape_animate(self, svg_file, config):
        if self.animation_screen_view.s:
            if self.animacion == 1:
                text_config = [
                    {"id_":"k","from_":"center_x", "t":"out_back", "d":.4},
                    {"id_":"i","from_":"center_y", "t":"out_bounce", "d":.4},
                    {"id_":"v","from_":"top", "t":"out_quint", "d":.4},
                    {"id_":"y","from_":"bottom", "t":"out_back", "d":.4},
                    {"id_":"m","from_":"center_y", "t":"out_back", "d":.4}
                ]
                helado_config = [
                    {"id_":"helado_inferior","from_":"top", "t":"out_bounce", "d":.6},
                    {"id_":"logo","from_":"top", "t":"out_bounce", "d":.6},
                    {"id_":"tapa","from_":"top", "t":"out_bounce", "d":.6},
                    {"id_":"helado_superior","from_":"bottom", "t":"out_bounce", "d":.8},
                ]   
                # self.animation_screen_view.s.shape_animate(svg_file, anim_config_list=text_config, on_complete=self.completed)
                self.animation_screen_view.s.shape_animate('icons/helado_en_vaso.svg', anim_config_list=helado_config, on_complete=self.completed)
                self.animacion = 0
            else:    
                self.animation_screen_view.s.draw('icons/text.svg', animate=True, fill=True, line_width=1)
                self.animacion = 1

    def reset_inactivity_timer(self):
        if hasattr(self, 'inactivity_event'):
            self.inactivity_event.cancel()
        self.inactivity_event = Clock.schedule_once(lambda dt: self.switch_to_animation(), 60)

    def switch_to_animation(self):
        self.animation_screen_view.manager.current = 'animation'
        self.reset_inactivity_timer()

    def switch_to_main(self):
        self.animation_screen_view.current = 'recipiente'
        
        self.reset_inactivity_timer()

    def completed(self, *args):
        pass

    def get_view(self)-> View.AnimationScreen.animation_screen.AnimationScreenView:
 
        return self.animation_screen_view
