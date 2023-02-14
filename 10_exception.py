
# Перепишите функцию hello_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, 
# писала пользователю "Пока!" и завершала работу при помощи оператора break

def hello_user(user_say):
    try:
        while True:
            user_say = input('Скажи что-нибудь: ')
            if user_say == 'Пока':
                print('Ну пока')
                break
            else:
                print('Сам ты {}'.format(user_say))
    except KeyboardInterrupt:
        print(' ') #Иначе при вводе ^С пишет "Пока" в строке "Скажи что-нибудь"
        print('Пока!')

hello_user("")

#Перепишите функцию discounted(price, discount, max_discount=20) из урока про функции так, 
# чтобы она перехватывала исключения, когда переданы некорректные аргументы. 
# Первые два нужно приводить к вещественному числу при помощи float(), 
# а третий - к целому при помощи int() и перехватывать исключения ValueError и TypeError, если приведение типов не сработало.


def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (ValueError, TypeError):
        print('Косяк ввода')


print(discounted(   input(f'Введи цену: '), 
                    input(f'Введи скидку: '), 
                    input(f'Введи макс.скидку: ')))
