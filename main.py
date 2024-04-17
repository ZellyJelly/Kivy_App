from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty, BooleanProperty
from kivy.metrics import dp
from kivy.uix.switch import Switch


class WidgetsExample(GridLayout):
    number = 1
    c_state = BooleanProperty(False)
    my_text = StringProperty(str(number))

    def change_text(self):
        if self.c_state == True:
            self.number = self.number + 1
            self.my_text = (str(self.number))
        else:
            pass
        
    def toggle_counter(self, value):
        if value.state == "down":
            self.c_state = True
        else:
            self.c_state = False

    def light_switch(self, value):
        self.god_switch(self, value)
        print(value.active)
    
    def god_switch(self, self_self, state):
            if state.active == True:
                new_button = Button(text="hi")
                self.add_widget(new_button)
                
    
            else:

                self.remove_widget()
            

        

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
