'''
Строка содержит пять временных значений. Они записаны через запятую:
'1h 45m,360s,25m,30m 120s,2h 60s'.
Напиши цикл, который посчитает общее количество минут. Результат сохрани в переменную и выведи на экран. 
Используй в решении методы split(), replace() и оператор in.
Обрати внимание: временное значение может состоять из одного, двух или трёх единиц времени. 

Значения расшифровываются так:

    часы — любое положительное целое число и символ h;
    минуты — любое положительное целое число и символ m;
    секунды — положительное целое число кратное 60 и символ s.


Ответ :  60+45+6+25+30+2+120+1 = 289.
'''

def str_to_minutes(timestring):
    measure = timestring[-1]
    value = timestring.replace('h', '').replace('m','').replace('s','')
    if (measure == 'h'):
        return int(value)*60
    elif (measure == 'm' ):
        return int(value)
    elif (measure == 's'):
        return int(value)//60   
    else: 
        return -9999999

s = '1h 45m,360s,25m,30m 120s,2h 60s'


total_minutes = 0

for chunk in s.split(','):
    parts = chunk.split()
    for item in parts:
        total_minutes += str_to_minutes(item)
        
print (total_minutes)




