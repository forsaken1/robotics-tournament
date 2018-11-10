from pyb import Pin

p_in = Pin('X2', Pin.IN, Pin.PULL_UP)
p_in.value()