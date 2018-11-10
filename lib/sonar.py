from pyb import Pin, ADC

class Sonar:
    """Sonar library"""

    LOW_ACCURACY = 3072
    HIGH_ACCURACY = 1024

    def __init__(self, low_accuracy = True, range_pin = 'X10', out_pin = 'X11'):
        self.low_accuracy = low_accuracy
        self.range_pin    = Pin(range_pin, Pin.IN, Pin.PULL_UP)
        self.out_pin      = ADC(Pin(out_pin))

        if False == low_accuracy:
            self.range_pin.low()
        else:
            self.range_pin.high() 

    def get_accuracy(self):
        return self.HIGH_ACCURACY if 0 == self.range_pin.value() else self.LOW_ACCURACY

    def get_distance(self):
        value = self.out_pin.read()
    
        return self.get_accuracy() * value / 3300