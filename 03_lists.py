
# Создайте список из чисел 3, 5, 7, 9 и 10.5
# Выведите содержимое списка на экран
# Добавьте в конец списка строку "Python"
# Выведите длину списка на экран

lists = [3, 5, 7, 9, 10.5]
print(lists)

lists.append(["Python"])
print(lists)

# Выведите на экран начальный элемент списка
# Выведите на экран последний элемент списка
# Напечатайте элементы списка со второго по четвертый включительно
# Удалите из списка строку "Python"

print(lists[0])
print(lists[-1])
print(lists[1:3])

lists.remove(["Python"])
print(lists)

# Создайте словарь: {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь

citys = {"city": "Москва", 
         "temperature": 20}

print(citys['city'])

citys['temperature'] = citys['temperature'] - 5
print(citys)

#Проверьте, есть ли в словаре ключ country
#Выведите значение по-умолчанию "Россия" для ключа country
#Добавьте в словарь элемент date со значением "27.05.2019"
#Выведите на экран длину словаря

print(citys.get('country'))
print(citys.get('country', 'Россия'))
# ?? как теперь показать что это сработает на будущих примерах?
#print(citys) #ничего не изменилось
#print(citys.get('country')) #осталось none
#print(citys['country']) #keyerror

citys['date'] = '27.05.2019'
print(citys)

print(len(citys))