from pyb import Pin
import pyb
from engine_wheel import EngineWheel
from engine_wheel_bunch import EngineWheelBunch

class Engine:
    STEP_DURATION = 10

    def __init__(self):
        self.frontRightWheel  = EngineWheel('X19', 'X20')
        self.frontLeftWheel   = EngineWheel('X21', 'X22')

        self.rearLeftWheel   = EngineWheel('X5',  'X6')
        self.rearRightWheel  = EngineWheel('X7',  'X8')
        
        self.all = EngineWheelBunch([self.frontLeftWheel, self.rearLeftWheel, self.frontRightWheel, self.rearRightWheel])
        
        self.lefts  = EngineWheelBunch([self.frontLeftWheel, self.rearLeftWheel])
        self.rights = EngineWheelBunch([self.frontRightWheel, self.rearRightWheel])
        
        self.fronts = EngineWheelBunch([self.frontLeftWheel, self.frontRightWheel])
        self.rears  = EngineWheelBunch([self.rearLeftWheel, self.rearRightWheel])

        self.trip_right = EngineWheelBunch([self.frontLeftWheel, self.rearRightWheel])
        self.trip_left = EngineWheelBunch([self.frontRightWheel, self.rearLeftWheel])

    def move(self):
        self.all.move()

    def stop(self):
        self.all.stop()

    def back(self):
        self.all.back()

    def left(self):
        self.trip_left.move()
        # self.trip_right.back()

    def right(self):
        self.lefts.move()
        self.rights.back()

    def step(self):
        self._run_step('move')

    def step_back(self):
        self._run_step('back')

    def step_left(self):
        self._run_step('left')

    def step_right(self):
        self._run_step('right')

    def _run_step(self, method_name):
        getattr(self, method_name)()
        pyb.delay(self.STEP_DURATION)
        self.all.stop()
        # pyb.delay(self.STEP_DURATION)
