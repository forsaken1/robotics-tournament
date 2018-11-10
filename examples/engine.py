from lib.engine import Engine
import pyb

engine = Engine()

while True:
    engine.move()
    pyb.delay(5000)

    engine.stop()
    pyb.delay(2000)

    engine.back();
    pyb.delay(5000)