from pyb import Pin, ADC

adc = ADC(Pin('X19'))	#использование 19 пина
value = adc.read() 				#читаем значение, АЦП 12 бит (диапазон значний от 0 до 4095)
print(value)