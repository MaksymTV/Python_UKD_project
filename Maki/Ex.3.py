from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        text = Label(text = "This is Text")
        btn = Button(text = "This is Button")
        layout = BoxLayout()
        layout.add_widget(text)
        layout.add_widget(btn)
        return layout
    
MyApp().run()