# import pyb
# import examples.sonar

## Color example

# from sensors.color import *

# color = Color(debug=True)
# while True:
#   print(color.is_path())
#   pyb.delay(1000)

## End color example


## Engines example

# from lib.engine import Engine

# engine = Engine()
# engine.move()

## End engine example


## Start tournament

from lib.tournament import Tournament

tournament = Tournament()
tournament.start()
