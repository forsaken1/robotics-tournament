from pyb import Pin
import pyb
from engine_wheel import EngineWheel
from engine_wheel_bunch import EngineWheelBunch

class Engine:
    STEP_DURATION = 10

    def __init__(self):
        self.right_wheel  = EngineWheel('X5',  'X6')
        self.left_wheel   = EngineWheel('X7',  'X8')
        
        self.bunch = EngineWheelBunch([self.right_wheel, self.left_wheel])

    def move(self):
        self.bunch.move()

    def stop(self):
        self.bunch.stop()

    def back(self):
        self.bunch.back()

    def left(self):
        self.right_wheel.move()
        self.left_wheel.back()

    def right(self):
        self.right_wheel.move()
        self.left_wheel.back()

    def step(self):
        self.move()
        self._end_step()

    def step_back(self):
        self.back()
        self._end_step()

    def step_left(self):
        self.left()
        self._end_step()

    def step_right(self):
        self.right()
        self._end_step()

    def _end_step(self):
        pyb.delay(self.STEP_DURATION)
        self.bunch.stop()
        # pyb.delay(self.STEP_DURATION)
