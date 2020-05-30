import RPi.GPIO as GPIO
import time


class Ingredient:
        def __init__(self, pin, dc, freq, sleep_time):
                self.pin                = pin                           # pump
                self.dc                 = dc                            # duty cycle            \
                self.freq               = freq                          # frequency             -      amount
                self.sleep_time         = sleep_time                    # pumping time period   /

                GPIO.setup(self.pin, self.freq)



class Drink:
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
        menu = {"vodka": 21, "tonic":4}
        GPIO.setmode(GPIO.BCM)
        jonik = Drink([menu["tonic"], menu["vodka"], 26], [100, 50, 100], [100, 100, 100],10)
        jonik.make()