from lib.engine import Engine
import pyb

engine = Engine()
engine.move()

pyb.delay(2000)

engine.stop()