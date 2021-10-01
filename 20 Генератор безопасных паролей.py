from random import *

def create_password(chars, lengths, password):
    for i in range(lengths - len(password)):
        password += choice(chars)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
password = ''
print('Добро пожаловать в программу для генерации паролей')
lengths = int(input('Укажите длинну пароля: '))
for i in range(int(input('Укажите количество паролей: '))):
    if input('Включать ли цифры 0123456789? (y/n): ') == 'y':
        chars += digits
        password += choice(digits)
    if input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ') == 'y':
        chars += uppercase_letters
        password += choice(uppercase_letters)
    if input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ') == 'y':
        chars += lowercase_letters
        password += choice(lowercase_letters)
    if input('Включать ли символы !#$%&*+-=?@^_? (y/n): ') == 'y':
        chars += punctuation
        password += choice(punctuation)
    if input('Исключать ли неоднозначные символы il1Lo0O? (y/n): ') == 'y':
        for symbol in 'il1Lo0O': 
            chars = chars.replace(symbol, '')
    print(create_password(chars, lengths, password))
    
    
