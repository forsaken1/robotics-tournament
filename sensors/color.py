from colorSensor import TCS34725

class Color:
    """Color detection library"""

    def __init__(self, debug = False, border = 15):
        self.debug = debug
        self.border = border
        self.tc = TCS34725()

    def raw(self):
        return self.tc.get_raw_data()

    def is_path(self):
        red, green, blue, c = self.raw()
        if self.debug:
            print(red, green, blue, c)
        return red < self.border and green < self.border and blue < self.border
