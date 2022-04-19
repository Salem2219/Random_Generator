import random

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

kivy.require('1.9.0')  # Possible Bug

Builder.load_file("IsabelleRandom.kv")




class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))





class IsabelleRandom(App):

    def build(self):
        return MyRoot()


isabelleRandom = IsabelleRandom()
isabelleRandom.run()
