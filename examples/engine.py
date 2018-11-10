from lib.engine import Engine
import pyb

pyb.delay(3000)

engine = Engine()

while True:
    engine.step_right()
    # pyb.delay(10)

# count = 100

# for i in range(0, count):
#     engine.step_right()

# for i in range(0, count):
#     engine.step_left()