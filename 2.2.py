import math

amount_mes_string = input('Введите количество равновероятных сообщений: ')
amount_value_string = input('Введите количество возможных значений разряда: ')
try:
    amount_mes = int(amount_mes_string)
    amount_value = int(amount_value_string)
    if amount_mes > 0 and amount_value > 0:
        h_m = 0
        h_s = 0
        for i in range(amount_mes):
            h_m -= (1/amount_mes)*math.log2(1/amount_mes)
        for i in range(amount_value):
            h_s -= (1/amount_value)*math.log2(1/amount_value)
        print('\nЭнтропия сообщения: {0}\nЭнтропия источника: {1}'.format(h_m,h_s))
    else:
         print('Проверьте правильность ввода! Требуется в обоих случаях задать положительное целое число .') 
except ValueError:
    print('Проверьте правильность ввода! Требуется в обоих случаях задать положительное целое число.')

input('\nНажмите ENTER для выхода из программы')