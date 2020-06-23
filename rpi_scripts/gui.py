from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.settings import SettingsWithSidebar
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import ObjectProperty


import os
os.environ["KIVY_WINDOW"] = "sdl2"
os.environ["KIVY_TEXT"] = "sdl2"

class BarScreen(Screen):
    pass

class ScrollableButton(Button):
    pass

class Bar(App):
    """
    Class that is root node of entire application.
    """
    def build(self):
        """
        Method to build application. Calling this function open application window.
        """
        self.screenmanager = ScreenManager()
        self.bar_screen = BarScreen(name="Bar")
        for i in range(20):
            self.bar_screen.ids['button_nav'].add_widget(ScrollableButton())
        self.screenmanager.add_widget(self.bar_screen)
        return self.screenmanager

if __name__ == '__main__':
    Bar().run()