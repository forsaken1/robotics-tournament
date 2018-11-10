from pyb import Pin, ADC

class Sonar:
    """Sonar library"""

    LOW_ACCURACY = 3072
    HIGH_ACCURACY = 1024

    def __init__(self, debug = False, out_pin = 'X11'):
        self.out_pin = ADC(Pin(out_pin))
        self.debug   = debug

    def get_distance(self):
        value = self.out_pin.read()
        result = 1024 * value / 3300

        if True == self.debug:
            print('value', value)
            print('distance', result)
    
        return result