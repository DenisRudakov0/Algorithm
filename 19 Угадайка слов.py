from random import *

word_list = ['корабль', 'карандаш', 'медуза', 'грабитель', 'моряк', 'абонемент', 'авиасалон', 'бессонница',
             'вакуум', 'велосипед', 'викторина', 'дрессировщик', 'жужелица', 'иероглиф', 'коктейль', 'крокодил']

def get_word(word_list):
    return choice(word_list)

def display_hangman(tries):
    stages = ['''
                ------
                |    |
                |    0
                |   /|\\
                |   / \\
                |
                |                    
              ''',
              '''
                ------
                |    |
                |    0
                |    |\\
                |   / \\
                |
                |                    
              ''',
              '''
                ------
                |    |
                |    0
                |    |
                |   / \\
                |
                |                    
              ''',
              '''
                ------
                |    |
                |    0
                |    |
                |     \\
                |
                |                    
              ''',
              '''
                ------
                |    |
                |    0
                |    |
                |
                |
                |                    
              ''',
              '''
                ------
                |    |
                |    0
                |
                |
                |
                |                    
              ''',
              '''
                ------
                |    |
                | 
                |
                |
                |
                |
              '''        
    ]
    return stages[tries]

def play(word):
    print('Давайте начнем игру!')
    word_completion = '_ ' * len(word) # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    word1 = word
    
    while tries != 0:
        print('Количество допустимых промахов: ', tries)
        print(display_hangman(tries), 'Загаданное слово: ', word_completion)
        s = input('Введите букву или слово: ').lower()
        if s.isalpha() == True:
            if len(s) == 1: # если 1 символ
                if s not in guessed_letters:
                    guessed_letters.append(s)
                    if s in word:
                        for i in range(word.count(s)):            
                            word_completion = word_completion[:word.index(s) * 2] + s + word_completion[word.index(s) * 2 + 1:]
                            word = word.replace(s, '1', 1)
                        if '_' not in word_completion:
                            return 'Поздравляем, вы угадали слово! Вы победили!'
                    else:
                        tries -= 1
                        print('К сожалению такой буквы нету. Попробуйте еще раз.')
                else:
                    print('Вы уже вводили данный символ', guessed_letters)
                    continue
            elif len(s) == len(word): # если слово целиком
                if s not in guessed_words:
                    guessed_words.append(s)
                    if s == word1:
                        return 'Поздравляем, вы угадали слово! Вы победили!'
                    else:
                        tries -= 1
                        print('Вы не угадали =)')
                else:
                    print('Вы уже вводили данное слово')
                    continue
        else:
            print('Вы ввели некоректные данные! Попробуйте еще раз.')
            continue
    print(display_hangman(tries))
    return 'У вас не осталось больше попыток. К сожадению вы проиграли!'

while input('Начать новую игру? (y/n) ') == 'y':
    word = get_word(word_list)
    print(play(word))
    print('Загаданное слово было: ', word)
print('Спасибо за игру. До встречи.')


















    
