from pyb import Pin, ADC

detector_range = Pin('X10', Pin.IN, Pin.PULL_UP)
detector_out = ADC(Pin('X11'))

detector_range.low()

LOW_ACCURACY = 3072
HIGH_ACCURACY = 1024

def get_accuracy():
    return HIGH_ACCURACY if 0 == detector_range.value() else LOW_ACCURACY

def get_distance():
    value = detector_out.read()
    
    return get_accuracy() * value / 3300