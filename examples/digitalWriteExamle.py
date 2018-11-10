from pyb import Pin
from utime import sleep_ms

p_out = Pin('X1', Pin.OUT_PP)
p_out.high()
sleep_ms(500)
p_out.low()
sleep_ms(500)