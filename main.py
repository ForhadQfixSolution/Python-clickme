from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout


class InterFace(FloatLayout):
    x = BooleanProperty(False)  # Define 'x' as a class variable
    def clicked(self):
        if self.x:  # Use 'self.x' to access the class variable
            self.ids.leb.text =  "[color=ff3333][b]Hello[/b] [/color]World"
            self.ids.btn.text = "Click Me"
        else:
            self.ids.leb.text =  " [b]Hello[/b] [/color][color=ff3333]World"
            self.ids.btn.text = "Clicked"
            # Toggle the value of x for the next click
        self.x = not self.x
class FirstApp(App):
    pass

FirstApp().run()
