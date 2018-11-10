## Distance example
import pyb
from lib.sonar import *

sonar = Sonar(True)

while True:
    sonar.get_distance()
    pyb.delay(500)

## end distance example