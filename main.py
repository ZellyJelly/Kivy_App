from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.metrics import dp


class WidgetsExample(GridLayout):
    number = 1
    state = "normal"
    my_text = StringProperty(str(number))

    def change_text(self):
        if self.state == "down":
            self.number = self.number + 1
            self.my_text = (str(self.number))
        else:
            pass
        
    def toggle_counter(self, value):
        self.state = value.state
        

class NewLayout(StackLayout):
    def __init__ (self, **kwargs):
        self.orientation = "lr-tb"
        super().__init__(**kwargs)
        for button in range(1, 100):
            b_button = Button(text=str(button), size_hint = (None, None), size = (dp(100), dp(100)))
            self.add_widget(b_button)
            self
        


class MyApp(App):
    pass


MyApp().run()
