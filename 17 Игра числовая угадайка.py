from random import *

def is_valid(vvod):
    return True if 1 <= vvod <= 100 else False

print('Добро пожаловать в числовую угадайку')
while input('Начать новую игру? (y/n): ') == 'y':
    num, count, vvod = randint(1, int(input('Укажите max число для границы угадывания: '))), 1, 1
    while vvod > 0:
        vvod = int(input('Введите число: '))
        if is_valid(vvod) == True:
            if vvod < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif vvod > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif vvod == num:
                print('Поздравляем! Вы угадали число. Вам понадобилось', count, 'попыток.')
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?') 
        count += 1
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
