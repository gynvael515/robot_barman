from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.relativelayout import RelativeLayout 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.image import Image

  
class Barman_gui(RelativeLayout): 
    def __init__(self, **var_args): 
          
        super(Barman_gui, self).__init__(**var_args) 
        
        Buttony = []
        Obrazki = []
 
        Buttony.append(Button(text='Drin 1' ,size_hint=(.15,.1) ,pos_hint={"center_x":.2,"center_y":.2})) #on_press=self.clearText --> KRZYCHOWA FUNKCJA
        Buttony.append(Button(text='Drin 2' ,size_hint=(.15,.1) ,pos_hint={"center_x":.5,"center_y":.2})) #on_press=self.clearText --> KRZYCHOWA FUNKCJA
        Buttony.append(Button(text='Drin 3' ,size_hint=(.15,.1) ,pos_hint={"center_x":.8,"center_y":.2})) #on_press=self.clearText --> KRZYCHOWA FUNKCJA
        
        Obrazki.append(Image(source='1.png'), size_hint=(.1,.2))
        Obrazki.append(Image(source='2.png'), size_hint=(.1,.2))
        Obrazki.append(Image(source='3.png'), size_hint=(.1,.2))
 
        for i in range(len(Buttony)):
                self.add_widget(Buttony[i])
                self.add_widget(Obrazki[i])
 
  
 
class Bar(App):  
    def build(self): 
        # return a Barman_gui() as a root widget 
        return Barman_gui() 
  
  
if __name__ == '__main__': 
<<<<<<< HEAD
    Bar().run() 
=======
    Bar().run() 
>>>>>>> a2af71e8102e924e8d10d13d977d9c6f8fe9b16c
