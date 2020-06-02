from board import SCL, SDA
import busio
import time
from adafruit_pca9685 import PCA9685


class Ingredient:
	def __init__(self, pin, dc, freq, sleep_time):
		self.pin        = pin                   # pump
		self.dc         = dc                    # duty cycle            \
		self.freq       = freq                  # frequency             -      amount
		self.sleep_time = sleep_time            # pumping time period   /


	def __start_pwm(self):
		GPIO.setup(self.pin, GPIO.OUT)
		self.pwm = GPIO.PWM(self.pin, self.freq)
		return self.pwm


	def __clean_pin(self):
		GPIO.cleanup(self.pin)





class Drink:
	def __init__(self, name, ingredients, pca):
		self.name = name
		self.ingredients = ingredients
		self.sleep_time = 3
		#self.pwms       = []
		self.pca = pca


	def __dc_percent2value(self, percent):
		x = percent*64*1024/100
		return x


	def make(self):
		# Run PWMs for each ingredient
		for i in range(len(self.ingredients)):
			pin = self.ingredients[i].pin
			dc 	= self.ingredients[i].dc
			self.pca.channels[pin].duty_cycle = self.__dc_percent2value(dc)


		# TODO: each alcohol should end in different time period
		time.sleep(self.sleep_time)


		# Clean pin for each ingredient
		for i in range(len(self.ingredients)):
			pin = self.ingredients[i].pin
			self.pca.channels[pin].duty_cycle = 0


class Menu:
	def __init__(self):
		# Create the I2C bus interface.
		self.i2c_bus = busio.I2C(SCL, SDA)
		# Create a simple PCA9685 class instance.
		self.pca = PCA9685(self.i2c_bus)
		self.pca.frequency = 100

		sleep_time = 5
		ingredients_dict = {"vodka": 0, "tonic":1, "a":2}

		self.drinks = {}

		# Drink1
		name = "Screwdriver" 
		ingredient0 = Ingredient(ingredients_dict["tonic"], 100, 100, sleep_time)
		ingredient1 = Ingredient(ingredients_dict["vodka"], 50,  100, sleep_time)
		ingredient2 = Ingredient(ingredients_dict["a"],     100, 100, sleep_time)
		ingredients = [ingredient0, ingredient1, ingredient2]
		self.drinks[name]= Drink(name, ingredients, self.pca)

		# Drink2
		name = "TurboCola" 
		ingredient0 = Ingredient(ingredients_dict["tonic"], 100, 100, sleep_time)
		ingredient1 = Ingredient(ingredients_dict["vodka"], 50,  100, sleep_time)
		ingredient2 = Ingredient(ingredients_dict["a"],     100, 100, sleep_time)
		ingredients = [ingredient0, ingredient1, ingredient2]
		self.drinks[name]= Drink(name, ingredients, self.pca)
		
		# Drink3
		name = "Drink1" 
		ingredient0 = Ingredient(ingredients_dict["tonic"], 100, 100, sleep_time)
		ingredient1 = Ingredient(ingredients_dict["vodka"], 50,  100, sleep_time)
		ingredient2 = Ingredient(ingredients_dict["a"],     100, 100, sleep_time)
		ingredients = [ingredient0, ingredient1, ingredient2]
		self.drinks[name]= Drink(name, ingredients, self.pca)
		
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