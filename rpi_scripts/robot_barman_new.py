import RPi.GPIO as GPIO
import time


class Ingredient:
	def __init__(self, pin, dc, freq, sleep_time):
		self.pin        = pin                   # pump
		self.dc         = dc                    # duty cycle            \
		self.freq       = freq                  # frequency             -      amount
		self.sleep_time = sleep_time            # pumping time period   /


	def __start_pwm(self):
		GPIO.setup(self.pin, self.freq)
		self.pwm = GPIO.PWM(self.pin, self.freq)
		return self.pwm


	def __clean_pin(self):
		GPIO.cleanup(self.pin)





class Drink:
	def __init__(self, ingredients):
		self.ingredients = ingredients
		self.sleep_time = 10
		self.pwms       = []



	def make(self):
		# Setup PWMs for each ingredient and store reference to PWMs in list
		for i in range(len(self.ingredients)):
			self.pwms.append(GPIO.PWM(self.self.ingredients[i].pin, self.self.ingredients[i].freq))
				
				
		# Run PWMs for each ingredient
		for i in range(len(self.ingredients)):
			self.pwms[i].start(self.self.ingredients[i].dc)


		# TODO: each alcohol should end in different time period
		time.sleep(self.sleep_time)


		# Clean pin for each ingredient
		for i in range(len(self.ingredients)):
			GPIO.cleanup(self.ingredients[i].pin)
			
			
		# Clean list of references to PWMs
		self.pwms = []




class Drink_old:
        def __init__(self, pins, dcs, freqs, sleep_time):
                self.ingredients = []


                self.pins               = pins
                self.dcs                = dcs
                self.freqs              = freqs
                self.sleep_time = sleep_time
                self.pwms               = []

                for i in range(len(self.pins)):
                        GPIO.setup(self.pins[i], GPIO.OUT)


                for i in range(len(self.pins)):
                        self.pwms.append(GPIO.PWM(self.pins[i], self.freqs[i]))


        def make(self):
                for i in range(len(self.pins)):
                        self.pwms[i].start(self.dcs[i])


                # TODO: each alcohol should end in different time period
                time.sleep(self.sleep_time)

                for i in range(len(self.pins)):
                        GPIO.cleanup(self.pins[i])



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
        jonik = Drink(ingredients)
        jonik.make()

        exit()
        jonik = Drink_old([menu["tonic"], menu["vodka"], 13], [100, 50, 100], [100, 100, 100],10)
        jonik.make()









