from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.metrics import dp


class NewLayout(StackLayout):
    def __init__ (self, **kwargs):
    
        super().__init__(**kwargs)
        for button in range(1, 100):
            b_button = Button(text=str(button), size_hint = (None, None), size = (dp(100), dp(100)))
            self.add_widget(b_button)
        


class MyApp(App):
    pass


MyApp().run()
