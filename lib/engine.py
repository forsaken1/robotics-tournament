from pyb import Pin
from engine_wheel import EngineWheel
from engine_wheel_bunch import EngineWheelBunch

class Engine:
    STEP_DURATION = 50

    def __init__(self):
        self.frontRightWheel = EngineWheel('X5',  'X6')
        self.frontLeftWheel  = EngineWheel('X7',  'X8')
        self.rearRightWheel  = EngineWheel('X19', 'X20')
        self.rearLeftWheel   = EngineWheel('X21', 'X22')

        self.all = EngineWheelBunch([self.frontLeftWheel, self.rearLeftWheel, self.frontRightWheel, self.rearRightWheel])
        
        self.lefts  = EngineWheelBunch([self.frontLeftWheel, self.rearLeftWheel])
        self.rights = EngineWheelBunch([self.frontRightWheel, self.rearRightWheel])
        
        self.fronts = EngineWheelBunch([self.frontLeftWheel, self.frontRightWheel])
        self.rears  = EngineWheelBunch([self.rearLeftWheel, self.rearRightWheel])

    def move(self):
        self.all.move()       

    def stop(self):
        self.all.stop()

    def back(self):
        self.all.back()

    def left(self):
        self.lefts.move()
        self.rights.back()

    def right(self):
        self.rights.move()
        self.lefts.back()

    def step(self):
        self.move()
        pyb.delay(self.STEP_DURATION)
        self.all.stop()

    def step_back(self):
        self.back()
        pyb.delay(self.STEP_DURATION)
        self.all.stop()

    def step_left(self):
        self.left()
        pyb.delay(self.STEP_DURATION)
        self.all.stop()

    def step_right(self):
        self.right()
        pyb.delay(self.STEP_DURATION)
        self.all.stop()