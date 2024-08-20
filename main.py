from typing import Union, NoReturn
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.carousel import MDCarousel
from View.screens import screens
import os
import sys
import threading
from xarm.wrapper import XArmAPI

import Scripts.Sub_Ir_Cono_1 as Sub_Ir_Cono_1
import Scripts.Sub_Ir_Cono_2 as Sub_Ir_Cono_2
import Scripts.Sub_Ir_Vaso as Sub_Ir_Vaso
import Scripts.Sub_C_Helado_1 as Sub_C_Helado_1
import Scripts.Sub_C_Helado_2 as Sub_C_Helado_2
import Scripts.Sub_C_Helado_3 as Sub_C_Helado_3
import Scripts.Sub_C_Topping_1 as Sub_C_Topping_1 
import Scripts.Sub_C_Topping_2 as Sub_C_Topping_2

import Scripts.Sub_V_Helado_1 as Sub_V_Helado_1
import Scripts.Sub_V_Helado_2 as Sub_V_Helado_2
import Scripts.Sub_V_Helado_3 as Sub_V_Helado_3

import Scripts.Sub_Entrega_V as Sub_Entrega_V

import Scripts.Sub_Entrega_C as Sub_Entrega_C

import Scripts.Sub_V_Topping_1 as Sub_V_Topping_1

import Scripts.Sub_V_Topping_2 as Sub_V_Topping_2

import Guardar_pedido

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

import Scripts.mdb as mdb # Importar el archivo mdb.py
from Scripts.mdb import g

from kivy.core.window import Window
from kivy.config import Config
Window.fullscreen = True

class PizzaAppConcept(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ip = self.get_ip_address()
        self.arm = self.initialize_arm(self.ip)
        self.load_all_kv_files(self.directory)
        self.manager_screens = ScreenManager()
        self.pedido = ["", "",""] 
        self.precio_pedido = ["", ""]
        self.dialog = None
        self.nombre_pedido = ""

    def get_ip_address(self) -> str:
        if len(sys.argv) >= 2:
            return sys.argv[1]
        else:
            try:
                from configparser import ConfigParser
                parser = ConfigParser()
                parser.read('robot.conf')
                return parser.get('xArm', 'ip')
            except:
                ip = input('Introduce su IP:')
                if not ip:
                    print('Error en la IP')
                    sys.exit(1)
                return ip

    def initialize_arm(self, ip: str) -> XArmAPI:
        arm = XArmAPI(ip)
        arm.motion_enable(enable=True)
        arm.set_mode(0)
        arm.set_state(0)
        return arm
    
    def chocolate(self,pizza_cost):
        self.pedido[0] = 1
        self.precio_pedido[0] = pizza_cost
        self.nombre_pedido = self.nombre_pedido + "/ Helado de chocolate "

        print(self.pedido[0])
    
    def megamix(self,pizza_cost):
        self.pedido[0] = 2
        self.precio_pedido[0] = pizza_cost
        self.nombre_pedido = self.nombre_pedido + "/ Helado de megamix "
        print(self.pedido[0])
    
    def vainilla(self,pizza_cost):
        self.pedido[0] = 3
        self.precio_pedido[0] = pizza_cost
        self.nombre_pedido = self.nombre_pedido + "/ Helado de vainilla "
        print(self.pedido[0])

    def topping_1(self,pizza_cost):
        self.pedido[1] = 1
        self.precio_pedido[1] = pizza_cost
        self.nombre_pedido = self.nombre_pedido + "/ topping 1"
        print(self.pedido)
    
    def topping_2(self,pizza_cost):
        self.pedido[1] = 2
        self.precio_pedido[1] = pizza_cost
        self.nombre_pedido = self.nombre_pedido + "/ topping 2"
        print(self.pedido)

    def topping_3(self,pizza_cost):
        self.pedido[1] = 3
        self.precio_pedido[1] = pizza_cost
        self.nombre_pedido = self.nombre_pedido + "/ sin topping"
        print(self.pedido)   

    def recipiente_vaso(self):
        self.pedido[2] = 1
        self.nombre_pedido = "Vaso"
    
    def recipiente_cono(self):
        self.pedido[2] = 2
        self.nombre_pedido = "Cono"

    def moverheladp_1(self):
        if self.pedido[2] == 1:
            Sub_Ir_Vaso.Sub_Ir_Vaso(self.arm)
            Sub_V_Helado_1.Sub_V_Helado_1(self.arm)
            
        if self.pedido[2] == 2:
            Sub_Ir_Cono_1.Sub_Ir_Cono_1(self.arm)
            Sub_C_Helado_1.Sub_C_Helado_1(self.arm)
        
        if self.pedido[1] == 1 and self.pedido[2] == 2:
            Sub_C_Topping_1.Sub_C_Topping_1(self.arm)
        if self.pedido[1] == 2 and self.pedido[2] == 2:
            Sub_C_Topping_2.Sub_C_Topping_2(self.arm)

        if self.pedido[1] == 1 and self.pedido[2] == 1:
            Sub_V_Topping_1.Sub_V_Topping_1(self.arm)
        if self.pedido[1] == 2 and self.pedido[2] == 1:
            Sub_V_Topping_2.Sub_V_Topping_2(self.arm)

        if self.pedido[2] == 1:
            Sub_Entrega_V.Sub_Entrega_V(self.arm)
        if self.pedido[2] == 2:
            Sub_Entrega_C.Sub_Entrega_C(self.arm)  
        
    def moverheladp_2(self):
        if self.pedido[2] == 1:
            Sub_Ir_Vaso.Sub_Ir_Vaso(self.arm)
            Sub_V_Helado_2.Sub_V_Helado_2(self.arm)
        if self.pedido[2] == 2:
            Sub_Ir_Cono_1.Sub_Ir_Cono_1(self.arm)
            Sub_C_Helado_2.Sub_C_Helado_2(self.arm)       
        if self.pedido[1] == 1 and self.pedido[2] == 2:
            Sub_C_Topping_1.Sub_C_Topping_1(self.arm)
        if self.pedido[1] == 2 and self.pedido[2] == 2:
            Sub_C_Topping_2.Sub_C_Topping_2(self.arm)
        if self.pedido[1] == 1 and self.pedido[2] == 1:
            Sub_V_Topping_1.Sub_V_Topping_1(self.arm)
        if self.pedido[1] == 2 and self.pedido[2] == 1:
            Sub_V_Topping_2.Sub_V_Topping_2(self.arm)    
        if self.pedido[2] == 1:
            Sub_Entrega_V.Sub_Entrega_V(self.arm)
        if self.pedido[2] == 2:
            Sub_Entrega_C.Sub_Entrega_C(self.arm)

    def moverheladp_3(self):

        if self.pedido[2] == 1:
            Sub_Ir_Vaso.Sub_Ir_Vaso(self.arm)
            Sub_V_Helado_3.Sub_V_Helado_3(self.arm)
            
        if self.pedido[2] == 2:
            Sub_Ir_Cono_1.Sub_Ir_Cono_1(self.arm)
            Sub_C_Helado_3.Sub_C_Helado_3(self.arm)
        
        if self.pedido[1] == 1 and self.pedido[2] == 2:
            Sub_C_Topping_1.Sub_C_Topping_1(self.arm)
        if self.pedido[1] == 2 and self.pedido[2] == 2:
            Sub_C_Topping_2.Sub_C_Topping_2(self.arm)

        if self.pedido[1] == 1 and self.pedido[2] == 1:
            Sub_V_Topping_1.Sub_V_Topping_1(self.arm)
        if self.pedido[1] == 2 and self.pedido[2] == 1:
            Sub_V_Topping_2.Sub_V_Topping_2(self.arm)

        if self.pedido[2] == 1:
            Sub_Entrega_V.Sub_Entrega_V(self.arm)
        if self.pedido[2] == 2:
            Sub_Entrega_C.Sub_Entrega_C(self.arm)

    def show_insufficient_funds_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Falta Dinero",
                text="No hay suficiente dinero para completar la transacción.",
                buttons=[
                    MDRaisedButton(
                        text="Aceptar",
                        on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def pedirHelado(self,pizza_name,pizza_cost):
        carousel = MDCarousel
        print(pizza_name,pizza_cost)
        if pizza_name == 'Helado chocolate':
            self.chocolate(pizza_cost)
        if pizza_name == 'Megamix':
            self.megamix(pizza_cost)
        if pizza_name == 'Helado vainilla':
            self.vainilla(pizza_cost) 
        if pizza_name == 'Chispas de chocolate':
            self.topping_1(pizza_cost)
        if pizza_name == 'Chispas de vainilla':
            self.topping_2(pizza_cost)
        if pizza_name == 'Sin topping':
            self.topping_3(pizza_cost)
        if pizza_name == 'Cono':  
            self.recipiente_cono()
        if pizza_name == 'Vaso':  
            self.recipiente_vaso()

    def servirhelado(self):
        precio_helado=self.precio_pedido[0].replace("$","")
        precio_topping=self.precio_pedido[1].replace("$","")
        precio_helado = float(precio_helado)
        precio_topping =float(precio_topping)
        precio_total = precio_helado + precio_topping
        cambio = precio_total - g.total_money
        Guardar_pedido.guardar_pedido_excel(self.nombre_pedido,precio_total,g.total_money,cambio)        
        if g.total_money >= precio_helado + precio_topping: 
            if self.arm.get_cgpio_digital(9)[1] == 1:
                if self.pedido[0] == 1:
                    Guardar_pedido.guardar_pedido_excel(self.nombre_pedido,precio_total,g.total_money,cambio)
                    t = threading.Thread(target=self.moverheladp_1)
                    t.start()
                if self.pedido[0] == 2:
                    Guardar_pedido.guardar_pedido_excel(self.nombre_pedido,precio_total,g.total_money,cambio)
                    t = threading.Thread(target=self.moverheladp_2)
                    t.start()   
                if self.pedido[0] == 3:
                    Guardar_pedido.guardar_pedido_excel(self.nombre_pedido,precio_total,g.total_money,cambio)
                    t = threading.Thread(target=self.moverheladp_3)
                    t.start()
            else:
                print("aun hay vaso")
        else:
            self.show_insufficient_funds_dialog()

    def handle_touch(self, *args):
        self.root.current = 'recipiente'
    
        # Lógica adicional que deseas ejecutar cuando se toca la pantalla
    def cancelar_venta(self):
        print("Cancelando venta")
        mdb.mdb_coin_change(g.total_money)
        g.total_money = 0  # Llama a la función para cancelar la venta cashless
        self.root.current = 'recipiente'

    def build(self) -> ScreenManager:
        return self.manager_screens
    
    def change_to_slider_menu(self, *args):
        self.root.current = 'recipiente'

    def change_to_slider_menu_variable(self, pizza_name, *args):


        if pizza_name == "Cono" or pizza_name == "Vaso":
            self.root.current = 'slider menu screen'  

        elif pizza_name == "Helado chocolate" or pizza_name == "Helado vainilla" or pizza_name == "Megamix":
            self.root.current = 'topping'      
        else:
            self.root.current = 'main screen'

    def generate_application_screens(self, interval: Union[int, float]) -> NoReturn:
        for name_screen in screens.keys():
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

    def on_start(self) -> NoReturn:
        Clock.schedule_once(self.generate_application_screens, 1)
        Clock.schedule_once(self.schedule_update_total_money_label, 2)  # Programa la actualización después de un pequeño retraso
        Clock.schedule_once(self.setup_mdb, 2)  # Asegúrate de que setup_mdb se llame

    def schedule_update_total_money_label(self, dt):
        Clock.schedule_interval(self.update_total_money_label, 1)  # Actualiza el label cada segundo

    def update_total_money_label(self, dt):
        try:
            total_money_label = self.root.get_screen('main screen').ids.total_money_label
            total_money_label.text = f"Total dinero: {g.total_money} pesos"
            amount_to_charge_label = self.root.get_screen('main screen').ids.amount_to_charge_label
            precio_helado=self.precio_pedido[0].replace("$","")
            precio_topping=self.precio_pedido[1].replace("$","")
            precio_helado = float(precio_helado)
            precio_topping =float(precio_topping)
            amount_to_charge_label.text = f"Monto a cobrar: {precio_helado + precio_topping - g.total_money} pesos" 
        except KeyError:
            print("No se pudo encontrar el ID total_money_label")
        except Exception as e:
            print(f"Error al actualizar el label: {e}")

    def setup_mdb(self, dt=None):
        port = '/dev/ttyUSB0'  # Cambia esto según tu sistema operativo
        ser = mdb.connect_to_mdb_rs232(port)
        if ser:
            mdb.enable_coin_acceptor(ser)
            print("Iniciando hilo de lectura del puerto MDB")
            mdb_thread = threading.Thread(target=mdb.mdb_read_and_parse)
            mdb_thread.daemon = True
            mdb_thread.start()

PizzaAppConcept().run()
