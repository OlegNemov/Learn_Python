
#Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит их к строке 
# и отдает объединенными через разделитель delimiter
#Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение на экран
#Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_summ(one, two, delimiter='&'):
    string = one + delimiter + two
    return string

fin_result = get_summ('Learn ', ' python')
print(fin_result)
print(f'{fin_result.upper()}')


#Создайте функцию format_price, которая принимает один аргумент price
#Приведите price к целому числу (тип int)
#Верните строку "Цена: ЧИСЛО руб."
#Вызовите функцию, передав на вход 56.24 и положите результат в переменную
#Выведите значение переменной с результатом на экран

def format_price(price):    
    int_price = 'Цена: ' + str(int(price)) + ' руб.'
    return int_price

integer_price = (format_price(56.24))
print(integer_price)