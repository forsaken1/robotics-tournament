from pyb import Pin, Timer
from utime import sleep_ms

p_out = Pin('X3', Pin.OUT_PP) 				#настройка пина на выход
p = Pin('X1') 								#использование таймера 2 на канале 1
tim = Timer(2, freq=1000)					#задание частоты таймера			
ch = tim.channel(1, Timer.PWM, pin=p)		#использование таймера как PWM
					

p_out.high()								#устанавливаем высокий сигнал
ch.pulse_width_percent(50)					#формирование PWM сигнала, от 0 до 100 (значение в процентах)
sleep_ms(1000)								#вращаем в одну сторону

p_out.low()									#устанавливаем низкий сигнал
ch.pulse_width_percent(50)					#формирование PWM сигнала, от 0 до 100 (значение в процентах)
sleep_ms(1000)								#вращаем в другую сторону