from pyb import Pin
from engineWheel import EngineWheel

class Engine:
    STEP_DURATION = 50

    def __init__(self):
        self.frontRightWheel = EngineWheel('X5',  'X6')
        self.frontLeftWheel  = EngineWheel('X7',  'X8')
        self.rearRightWheel  = EngineWheel('X19', 'X20')
        self.rearLeftWheel   = EngineWheel('X21', 'X22')

    def move(self):
        self.frontRightWheel.move()
        self.frontLeftWheel.move()
        self.rearRightWheel.move()
        self.rearLeftWheel.move()
        

    def stop(self):
        self.frontRightWheel.stop()
        self.frontLeftWheel.stop()
        self.rearRightWheel.stop()
        self.rearLeftWheel.stop()

    def back(self):
        self.frontRightWheel.back()
        self.frontLeftWheel.back()
        self.rearRightWheel.back()
        self.rearLeftWheel.back()

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