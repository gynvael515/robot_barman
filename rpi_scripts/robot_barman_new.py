import RPi.GPIO as GPIO
import time


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
	def __init__(self, name, ingredients):
		self.name = name
		self.ingredients = ingredients
		self.sleep_time = 3
		self.pwms       = []



	def make(self):
		# Setup pins and PWMs for each ingredient and store reference to PWMs in list
		for i in range(len(self.ingredients)):
			GPIO.setup(self.ingredients[i].pin, GPIO.OUT)
			self.pwms.append(GPIO.PWM(self.ingredients[i].pin, self.ingredients[i].freq))
				
				
		# Run PWMs for each ingredient
		for i in range(len(self.ingredients)):
			self.pwms[i].start(self.ingredients[i].dc)


		# TODO: each alcohol should end in different time period
		time.sleep(self.sleep_time)


		# Clean pin for each ingredient
		for i in range(len(self.ingredients)):
			GPIO.cleanup(self.ingredients[i].pin)
			
			
		# Clean list of references to PWMs
		self.pwms = []




if __name__ == "__main__":
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









