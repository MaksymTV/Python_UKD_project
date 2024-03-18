from kivy.app import App 
from kivy.uix.button import Button

class myApp(App):
    def build(self):
        btn = Button(text='This is button!!!')
        return btn
    
myApp().run()
