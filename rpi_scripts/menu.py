import barman_classes
from board import SCL, SDA
import busio
import time
from adafruit_pca9685 import PCA9685


class Menu:
	def __init__(self):
		# Create the I2C bus interface.
		self.i2c_bus = busio.I2C(SCL, SDA)
		# Create a simple PCA9685 class instance.
		self.pca = PCA9685(self.i2c_bus)
		self.pca.frequency = 100

		sleep_time = 5
		menu = {"vodka": 0, "tonic":1, "a":2}

		self.drinks = {}

		# Drink1
		name = "Screwdriver" 
		ingredient0 = barman_classes.Ingredient(menu["tonic"], 100, 100, sleep_time)
		ingredient1 = barman_classes.Ingredient(menu["vodka"], 50,  100, sleep_time)
		ingredient2 = barman_classes.Ingredient(menu["a"],     100, 100, sleep_time)
		ingredients = [ingredient0, ingredient1, ingredient2]
		self.drinks[name]= barman_classes.Drink(name, ingredients, self.pca)

		# Drink2
		name = "TurboCola" 
		ingredient0 = barman_classes.Ingredient(menu["tonic"], 100, 100, sleep_time)
		ingredient1 = barman_classes.Ingredient(menu["vodka"], 50,  100, sleep_time)
		ingredient2 = barman_classes.Ingredient(menu["a"],     100, 100, sleep_time)
		ingredients = [ingredient0, ingredient1, ingredient2]
		self.drinks[name]= barman_classes.Drink(name, ingredients, self.pca)
		
		# Drink3
		name = "Drink1" 
		ingredient0 = barman_classes.Ingredient(menu["tonic"], 100, 100, sleep_time)
		ingredient1 = barman_classes.Ingredient(menu["vodka"], 50,  100, sleep_time)
		ingredient2 = barman_classes.Ingredient(menu["a"],     100, 100, sleep_time)
		ingredients = [ingredient0, ingredient1, ingredient2]
		self.drinks[name]= barman_classes.Drink(name, ingredients, self.pca)
		# Drink4
		# Drink5
		# Drink6
		# Drink7
		# Drink8
		# Drink9
		# Drink10
		# Drink11
		# Drink12
		# Drink13
		# Drink14
		# Drink15
		# Drink16
		# Drink17
		# Drink18
		# Drink19
		# Drink20


menu = Menu()

if __name__ == "__main__":
	menu.drinks["Srewdriver"].make()