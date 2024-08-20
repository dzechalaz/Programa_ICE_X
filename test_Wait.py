from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivg import Kivg

kv = """
<AnimationScreen>:
    canvas:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
            
    BoxLayout:
        orientation: "vertical"
        AnchorLayout:
            BoxLayout:
                id: svg_area
                size_hint: None, None
                size: 256, 256

<MainScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Volver a la animación'
            on_release: app.switch_to_animation()
"""

class AnimationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Establece el color del fondo como blanco (R, G, B, A)
            self.bg = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        self.s = None  # Inicializar Kivg aquí si es necesario

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def on_touch_down(self, touch):
        app = App.get_running_app()
        app.switch_to_main()
        return True

class MainScreen(Screen):
    pass

class KivgDemo(App):
    def build(self):
        self.root = Builder.load_string(kv)
        self.screen_manager = ScreenManager()
        self.animation_screen = AnimationScreen(name='animation')
        self.main_screen = MainScreen(name='main')
        self.screen_manager.add_widget(self.animation_screen)
        self.screen_manager.add_widget(self.main_screen)
        self.set_kivg_in_animation_screen()
        return self.screen_manager

    def set_kivg_in_animation_screen(self):
        # Este método asume que tienes un área en AnimationScreen para Kivg
        self.animation_screen.s = Kivg(self.animation_screen.ids.svg_area)

    def on_start(self):
        Clock.schedule_once(lambda dt: self.start_text_animation(), 0)
        self.reset_inactivity_timer()

    def start_text_animation(self):
        # Reemplaza 'your_svg_file.svg' con el nombre de tu archivo SVG real
        if self.animation_screen.s:
            self.animation_screen.s.draw('icons/text.svg', animate=True, fill=True, line_width=1)
        Clock.schedule_interval(lambda dt: self.shape_animate('icons/text.svg', 'text_config'), 5)

    def shape_animate(self, svg_file, config):
        if self.animation_screen.s:
            text_config = [
                {"id_":"k","from_":"center_x", "t":"out_back", "d":.4},
                {"id_":"i","from_":"center_y", "t":"out_bounce", "d":.4},
                {"id_":"v","from_":"top", "t":"out_quint", "d":.4},
                {"id_":"y","from_":"bottom", "t":"out_back", "d":.4},
                {"id_":"m","from_":"center_y", "t":"out_back", "d":.4}
            ]
            self.animation_screen.s.shape_animate(svg_file, anim_config_list=text_config, on_complete=self.completed)

    def reset_inactivity_timer(self):
        if hasattr(self, 'inactivity_event'):
            self.inactivity_event.cancel()
        self.inactivity_event = Clock.schedule_once(lambda dt: self.switch_to_animation(),10)

    def switch_to_animation(self):
        self.screen_manager.current = 'animation'
        self.reset_inactivity_timer()

    def switch_to_main(self):
        self.screen_manager.current = 'main'
        self.reset_inactivity_timer()

    def completed(self, *args):
        # Aquí puedes manejar eventos post-animación o repetir la animación
        pass

if __name__ == "__main__":
    KivgDemo().run()
