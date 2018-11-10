from pyb import Pin, ADC

class LineDetector:
    """detect black line"""

    def __init__(self, pin, debug = False):
        self.out = ADC(Pin(pin))
        self.debug = debug

    def raw(self):
        out = self.out.read()
        if self.debug:
            print(out)
        return out

    def is_path(self):
        out = self.raw()
        return out > 100
