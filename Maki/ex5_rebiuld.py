from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout


class FirstScreen(Screen):
    def __init__(self, name ='first'):
        super().__init__(name = name)
        layout = GridLayout(cols=2)
        for i in range(4):
            btn = Button(text=f"Button {i+1}")
            btn.on_press = self.next
            layout.add_widget(btn)
        self.add_widget(layout)

    def next(self, *args):
        self.manager.transition.direction = "up"
        self.manager.current = "second"


class SecondScreen(Screen):
    def __init__(self, name ='second'):
        super().__init__(name = name)
        btn = Button(text = "Second button!")
        btn.on_press = self.next 
        self.add_widget(btn)
    
    def next(self, *args):
        self.manager.transition.direction = "left"
        self.manager.current = "third"


class ThirdScreen(Screen):
    def __init__(self, name ='third'):
        super().__init__(name = name)
        btn = Button(text = "Third button!")
        btn.on_press = self.next 
        self.add_widget(btn)
        
    def next(self, *args):
        self.manager.transition.direction = "right"
        self.manager.current = "fourth"


class FourthScreen(Screen):
    def __init__(self, name ='fourth'):
        super().__init__(name = name)
        btn = Button(text = "Fourth button!")
        btn.on_press = self.next 
        self.add_widget(btn)
    
    def next(self, *args):
        self.manager.transition.direction = "down"
        self.manager.current = "fifth"


class FifthScreen(Screen):
    def __init__(self, name='fifth'):
        super().__init__(name=name)
        btn = Button(text="Fifth button!")
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self, *args):
        self.manager.transition.direction = "up"
        self.manager.current = "first"


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
