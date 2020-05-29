import RPi.GPIO as GPIO, time


class Drink:
    def __init__(self, pins, dcs, freqs):
        self.pins  = pins
        self.dcs   = dcs
        self.freqs = freqs
        self.times = 10
        self.pwms = []

        for i in range(len(self.pins)):
            GPIO.setup(self.pins[i], GPIO.OUT)


        for i in range(len(self.pins)):
            self.pwms.append(GPIO.PWM(self.pins[i], self.freqs[i]))


    def make(self):
        #for i in range(len(self.pins)):
        #       GPIO.setup(self.pins[i], GPIO.OUT)

        for i in range(len(self.pins)):
            #pwm = GPIO.PWM(self.pins[i], self.freqs[i])
            self.pwms[i].start(self.dcs[i])


        # TODO: each alcohol should end in different time period
        time.sleep(self.times)

        for i in range(len(self.pins)):
            GPIO.cleanup(self.pins[i])


if __name__ == "__main__":
    menu = {"vodka": 21, "tonic":4}
    GPIO.setmode(GPIO.BCM)
    jonik = Drink([menu["tonic"], menu["vodka"]], [100, 50], [100, 100])
    jonik.make()



    exit()
    pin  = 4
    pin2 = 21
    time_period = 20

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin2,GPIO.OUT)

    dc = 100
    freq = 10

    pwm  = GPIO.PWM(pin, freq)
    pwm2 = GPIO.PWM(pin2, freq)
    pwm.start(dc)
    pwm2.start(dc/2)

    time.sleep(time_period)

    # pwm.ChangeFrequence(freq)
    # time.sleep()
    # pwm.ChangeDutyCycle(dc)
    # time.sleep(5)
    # pwm.stop()

    GPIO.cleanup(pin)
    GPIO.cleanup(pin2)