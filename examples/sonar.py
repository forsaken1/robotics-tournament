## Distance example
import pyb
from lib.sonar import *

sonar = Sonar()

while True:
    print(sonar.get_distance(), 'mm')
    print(sonar.get_distance_cm(), 'cm')
    print('is see board?', sonar.is_see_board())
    print('================')
    pyb.delay(750)

## end distance example