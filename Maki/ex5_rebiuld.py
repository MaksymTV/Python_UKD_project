from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label


class FirstScreen(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        layout = FloatLayout()

        # Додамо кнопки для переходу на кожний екран
        for screen_name in ["second", "third", "fourth", "fifth"]:
            btn = Button(text=f"Go to {screen_name.capitalize()} Screen", size_hint=(0.4, 0.1),
                         pos_hint={'x': 0.3, 'y': 0.8 - 0.2 * ["second", "third", "fourth", "fifth"].index(screen_name)})
            btn.on_press = lambda screen_name=screen_name: self.go_to_screen(screen_name)
            layout.add_widget(btn)

        self.add_widget(layout)

    def go_to_screen(self, screen_name):
        self.manager.transition.direction = "up"
        self.manager.current = screen_name


class BaseScreen(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        layout = FloatLayout()

        # Додамо кнопку для повернення на головний екран
        btn_back = Button(text="Back to First Screen", size_hint=(0.4, 0.1), pos_hint={'x': 0.3, 'y': 0.05})
        btn_back.on_press = self.go_to_first_screen
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def go_to_first_screen(self, *args):
        self.manager.transition.direction = "down"
        self.manager.current = "first"


class SecondScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(name='second', **kwargs)
        layout = self.children[0]

        # Додамо фотографію
        img = Image(source='img/second.jpg', size_hint=(None, None), size=(350, 350), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(img)

        # Додамо текстовий елемент з відступом
        lbl = Label(text="Boromir from The Lord of the Rings", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        lbl.y -= 10  # Зміщення вниз на 10 пікселів
        layout.add_widget(lbl)


class ThirdScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(name='third', **kwargs)
        layout = self.children[0]

        # Додамо фотографію
        img = Image(source='img/Frodo.webp', size_hint=(None, None), size=(350, 350), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(img)

        # Додамо текстовий елемент з відступом
        lbl = Label(text="Frodo from The Lord of the Rings", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        lbl.y -= 10  # Зміщення вниз на 10 пікселів
        layout.add_widget(lbl)


class FourthScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(name='fourth', **kwargs)
        layout = self.children[0]

        # Додамо фотографію
        img = Image(source='img/Sauron.webp', size_hint=(None, None), size=(230, 350), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(img)

        # Додамо текстовий елемент з відступом
        lbl = Label(text="Sauron Lord of the Rings,", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        lbl.y -= 10  # Зміщення вниз на 10 пікселів
        layout.add_widget(lbl)


class FifthScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(name='fifth', **kwargs)
        layout = self.children[0]

        # Додамо фотографію
        img = Image(source='img/gimli.jpg', size_hint=(None, None), size=(230, 350), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(img)

        # Додамо текстовий елемент з відступом
        lbl = Label(text="Gimli from The Lord of the Rings,", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        lbl.y -= 10  # Зміщення вниз на 10 пікселів
        layout.add_widget(lbl)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(FourthScreen())
        sm.add_widget(FifthScreen())
        return sm


MyApp().run()