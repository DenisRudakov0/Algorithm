from random import *

answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай' \
           'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет' \
           'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', \
           'По моим данным - нет', 'Определённо да', 'Знаки говорят - да', \
           'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', \
           'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name, Yes = input('Как мне к тебе обращаться? '), 'y'
print('Приветствую ', name, ', я готов ответить на твой вопрос.', sep = '')
while Yes == 'y':
    print(input('Слушаю: '))
    print(choice(answers))
    y = input('У тебя еще есть вопросы? (y/n) ')
    if y != 'y':
        break    
print('Возвращайся если возникнут вопросы!')
