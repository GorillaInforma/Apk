from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MiniAppLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        self.contador = 0

        # Titulo
        self.add_widget(Label(text="Mi Mini App", font_size=28, size_hint=(1, 0.2)))

        # Input para nombre
        self.nombre_input = TextInput(hint_text="Escribe tu nombre", multiline=False, size_hint=(1, 0.2))
        self.add_widget(self.nombre_input)

        # Label de saludo
        self.saludo = Label(text="Hola!", font_size=22, size_hint=(1, 0.2))
        self.add_widget(self.saludo)

        # Boton saludar
        btn_saludar = Button(text="Saludarme", size_hint=(1, 0.2), background_color=(0.2, 0.6, 1, 1))
        btn_saludar.bind(on_press=self.saludar)
        self.add_widget(btn_saludar)

        # Contador
        self.label_contador = Label(text="Contador: 0", font_size=20, size_hint=(1, 0.2))
        self.add_widget(self.label_contador)

        # Botones + y -
        caja_botones = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.2))
        btn_mas = Button(text="+1")
        btn_menos = Button(text="-1")
        btn_mas.bind(on_press=self.sumar)
        btn_menos.bind(on_press=self.restar)
        caja_botones.add_widget(btn_menos)
        caja_botones.add_widget(btn_mas)
        self.add_widget(caja_botones)

    def saludar(self, instance):
        nombre = self.nombre_input.text
        if nombre:
            self.saludo.text = f"Hola, {nombre}! 👋"
        else:
            self.saludo.text = "¡Escribe tu nombre!"

    def sumar(self, instance):
        self.contador += 1
        self.label_contador.text = f"Contador: {self.contador}"

    def restar(self, instance):
        self.contador -= 1
        self.label_contador.text = f"Contador: {self.contador}"

class MiApp(App):
    def build(self):
        return MiniAppLayout()

MiApp().run()
