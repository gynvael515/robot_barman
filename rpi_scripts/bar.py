from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.relativelayout import RelativeLayout 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.image import Image
import menu


  
class Barman_gui(RelativeLayout): 
	def __init__(self, **var_args): 
		path = 'src/'
		super(Barman_gui, self).__init__(**var_args) 
		self.menu = menu.menu
		Buttony = []
		Obrazki = []
 
		Buttony.append(Button(text='Drin 1' ,size_hint=(.15,.1) ,pos_hint={"center_x":.2,"center_y":.2}))#, on_press= self.menu.drinks["Screwdriver"].make()))#--> KRZYCHOWA FUNKCJA
		Buttony[0].bind(on_press=self.menu.drinks["Screwdriver"].make)
		Buttony.append(Button(text='Drin 2' ,size_hint=(.15,.1) ,pos_hint={"center_x":.5,"center_y":.2})) #on_press=self.clearText --> KRZYCHOWA FUNKCJA
		Buttony.append(Button(text='Drin 3' ,size_hint=(.15,.1) ,pos_hint={"center_x":.8,"center_y":.2})) #on_press=self.clearText --> KRZYCHOWA FUNKCJA

		Obrazki.append(Image(source=path+'1.jpg', size_hint=(.1,.2)))
		Obrazki.append(Image(source=path+'2.png', size_hint=(.1,.2)))
		Obrazki.append(Image(source=path+'3.png', size_hint=(.1,.2)))


		#	Obrazki.append(Image(source=path+'2.png', size_hint=(.1,.2))
    	#   Obrazki.append(Image(source=path+'3.png', size_hint=(.1,.2))
 

		for i in range(len(Buttony)):
			self.add_widget(Buttony[i])
			self.add_widget(Obrazki[i])
 
  
 
class Bar(App):  
    def build(self): 
        # return a Barman_gui() as a root widget 
        return Barman_gui() 
  
  
if __name__ == '__main__': 
	Bar().run() 

