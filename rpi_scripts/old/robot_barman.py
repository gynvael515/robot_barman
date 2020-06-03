from board import SCL, SDA
import busio
import time
# Import the PCA9685 module.
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



if __name__ == "__main__":
	exit()
		
	menu = {"vodka": 21, "tonic":4, "a":13}

	sleep_time = 5
	ingredient0 = Ingredient(menu["tonic"], 100, 100, sleep_time)
	ingredient1 = Ingredient(menu["vodka"], 50,  100, sleep_time)
	ingredient2 = Ingredient(menu["a"],     100, 100, sleep_time)
        
	ingredients = [ingredient0,
                   ingredient1,
                   ingredient2]


	GPIO.setmode(GPIO.BCM)
	jonik = Drink("drink", ingredients)
	jonik.make()
	
	exit()
	#jonik = Drink_old([menu["tonic"], menu["vodka"], 13], [100, 50, 100], [100, 100, 100],10)
	#jonik.make()









