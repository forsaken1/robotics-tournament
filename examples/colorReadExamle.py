from colorSensor import TCS34725    #вызов библиотеки
tc = TCS34725()                     #создаем объект класса для датчика    
r, g, b, c = tc.get_raw_data()      #получаем значения от датчика цвета
print(r, g, b, c)                   #выводим значения цвета