from pyb import Pin

class EngineWheel:
    def __init__(self, pin1, pin2):
        self.pin1 = Pin(pin1, Pin.OUT_PP)
        self.pin2 = Pin(pin2, Pin.OUT_PP)

    def move(self):
        self.pin1.high()
        self.pin2.low()

    def stop(self):
        # self.pin1.high()
        # self.pin2.high()

        self.pin1.low()
        self.pin2.low()

    def back(self):
        self.pin1.low()
        self.pin2.high()