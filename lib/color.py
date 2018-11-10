import os.path
from lib.line_detector import LineDetector

if os.path.isfile('./colorSensor.py'):
    from colorSensor import TCS34725
else:
    from colorSensorMock import TCS34725

class Color:
    """Color detection library"""

    def __init__(self, debug = False, border = 15):
        self.debug = debug
        self.border = border
        self.white_border = border * 4
        self.blue_modifier = 1.3
        self.colorDetector = TCS34725()
        self.leftLineDetector = LineDetector('Y11')
        self.rightLineDetector = LineDetector('Y12')

    def raw(self):
        red, green, blue, c = self.colorDetector.get_raw_data()
        if self.debug:
            print(red, green, blue)
        return red, green, blue

    def is_path(self):
        red, green, blue = self.raw()
        return red < self.border and green < self.border and blue < self.border

    def is_white(self):
        red, green, blue = self.raw()
        return red > self.white_border and green > self.white_border and blue > self.white_border

    def is_red(self):
        red, green, blue = self.raw()
        return self._is_color(red, green, blue)

    def is_green(self):
        red, green, blue = self.raw()
        return self._is_color(green, red, blue)

    def is_blue(self):
        red, green, blue = self.raw()
        return self._is_color(blue * self.blue_modifier, red, green)

    def left_black(self):
        return self.leftLineDetector.is_path()

    def right_black(self):
        return self.rightLineDetector.is_path()

    def _middle(self, a, b):
        return abs((a + b) / 2)

    def _is_color(self, target, other1, other2):
        return target > self._middle(other1, other2) * 2
