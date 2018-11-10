from lib.engine import Engine
import pyb

pyb.delay(3000)

engine = Engine()

count = 24

for i in range(0, count):
    engine.step()

for i in range(0, count):
    engine.step_back()

for i in range(0, count):
    engine.step_right()

for i in range(0, count):
    engine.step_left()