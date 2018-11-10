from pyb import Pin, ADC

class Sonar:
    """Sonar library"""

    MIN_DISTANCE = 50
    MAX_DISTANCE = 600;

    def __init__(self, debug = False, out_pin = 'X11'):
        self.out_pin = ADC(Pin(out_pin))
        self.debug   = debug

    def get_distance(self):
        value = self.out_pin.read()
        result = round(1024 * value / 5000) - self.MIN_DISTANCE
        if (0 > result):
            result = 0

        if True == self.debug:
            print('value', value)
            print('distance', result)
    
        return result

    def get_distance_cm(self):
        return round(self.get_distance() / 10, 2)

    def is_see_board(self):
        return (self.MAX_DISTANCE > self.get_distance())