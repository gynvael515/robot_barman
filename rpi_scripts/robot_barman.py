import RPi.GPIO as GPIO
import time


class Ingredient:
        def __init__(self, pin, dc, freq, sleep_time):
                self.pin                = pin                           # pump
                self.dc                 = dc                            # duty cycle                    \
                self.freq               = freq                          # frequency                             -      amount
                self.sleep_time = sleep_time            # pumping time period   /



        def start_pwm(self):
                GPIO.setup(self.pin, self.freq)
                GPIO.PWM(self.pin, self.freq)



        def clean_pin(self):
                GPIO.cleanup(self.pin)





class Drink:
        def __init__(self, ingredients):
                self.ingredients = ingredients
                self.sleep_time = 10



        def make(self):
                for i in range(len(self.ingredients)):
                        self.ingredients[i].start_pwm()


                # TODO: each alcohol should end in different time period
                time.sleep(self.sleep_time)


                for i in range(len(self.ingredients)):
                        self.ingredients[i].clear_pin()




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

        ingredient0 = Ingredient(menu["tonic"], 100, 100, 10)
        ingredient1 = Ingredient(menu["vodka"], 50,  100, 10)
        ingredient2 = Ingredient(menu["a"],     100, 100, 10)
        ingredients = [ingredient0,
                                        ingredient1,
                                        ingredient2]



        GPIO.setmode(GPIO.BCM)
        jonik = Drink(ingredients)
        jonik.make()

        exit()
        jonik = Drink_old([menu["tonic"], menu["vodka"], 13], [100, 50, 100], [100, 100, 100],10)
        jonik.make()









