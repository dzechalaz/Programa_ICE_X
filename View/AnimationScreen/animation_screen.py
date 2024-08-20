from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.app import App

class AnimationScreenView(Screen):
    def __init__(self, controller, model, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.model = model
        
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Establece el color del fondo como blanco (R, G, B, A)
            self.bg = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        self.s = None  # Inicializar Kivg aquí si es necesario

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def on_touch_down(self, touch):
        self.controller.switch_to_main()
        return True
