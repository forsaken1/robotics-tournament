from pyb import Pin

class Engine:
    STEP_DURATION = 50

    def __init__(self):
        self.rearLeft1 = Pin('X9', Pin.OUT_PP)
        self.rearLeft2 = Pin('X10', Pin.OUT_PP)

    def move(self):
        self.rearLeft1.high()
        self.rearLeft2.low()

    def stop(self):
        self.rearLeft1.high()
        self.rearLeft2.high()

        self.rearLeft1.low()
        self.rearLeft2.low()

    def left(self):
        pass

    def right(self):
        pass

    def step(self):
        pass

    def step_back(self):
        pass

    def step_left(self):
        pass

    def step_right(self):
        pass
