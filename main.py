## Distance example

from distance import *

print(get_distance())

## end distance example


## Color example

from sensors.color import *
import pyb

color = Color(debug=True)
while True:
  print(color.is_path())
  pyb.delay(1000)

## End color example
