# Брюс Уиллис = 19.03.1955
# Арнольд Шварцнеггер = 30.07.1947
# Сильвестр Сталлоне = 06.07.1946
# Чак Норрис = 10.03.1940
# Жан-Клод Ван Дамм = 18.10.1960
# Гарт Эннис = 16.01.1970
# Марк Миллар = 24.12.1969
# Джон Ромита-младший = 17.08.1956
# Фрэнк Миллер = 27.01.1957
# Скотт Снайдер = 01.01.1976

import random
brain = 0
stupid = 0
desire = 'yes'
people_dates = dict()
people_word_dates = dict()
people = ['Брюс Уиллис', 'Арнольд Шварцнеггер', 'Сильвестр Сталлоне', 'Чак Норрис', 'Жан-Клод Ван Дамм',
          'Гарт Эннис', 'Марк Миллар', 'Джон Ромита-младший', 'Фрэнк Миллер', 'Скотт Снайдер']
people_dates ['Брюс Уиллис'] = '19.03.1955'
people_dates ['Арнольд Шварцнеггер'] = '30.07.1947'
people_dates ['Сильвестр Сталлоне'] = '06.07.1946'
people_dates ['Чак Норрис'] = '10.03.1940'
people_dates ['Жан-Клод Ван Дамм'] = '18.10.1960'
people_dates ['Гарт Эннис'] = '16.01.1970'
people_dates ['Марк Миллар'] = '24.12.1969'
people_dates ['Джон Ромита-младший'] = '17.08.1956'
people_dates ['Фрэнк Миллер'] = '27.01.1957'
people_dates ['Скотт Снайдер'] = '01.01.1976'
people_word_dates['Брюс Уиллис'] = 'девятнадцатое марта 1955'
people_word_dates['Арнольд Шварцнеггер'] = 'тридцатое июля 1947'
people_word_dates['Сильвестр Сталлоне'] = 'шестое июля 1946'
people_word_dates['Чак Норрис'] = 'десятое марта 1940'
people_word_dates['Жан-Клод Ван Дамм'] = 'восемнадцатое октября 1960'
people_word_dates['Гарт Эннис'] = 'шестнадцатое января 1970'
people_word_dates['Марк Миллар'] = 'двадцать четвёртое декабря 1969'
people_word_dates['Джон Ромита-младший'] = 'семнадцатое августа 1956'
people_word_dates['Фрэнк Миллер'] = 'двадцать седьмое января 1957'
people_word_dates['Скотт Снайдер'] = 'первое января 1976'
result = random.sample(people, 5)
while desire == 'yes':
    print('Введите дату рождения в формате дд.мм.гг следующих известных людей: ')
    for man in result:
        question = str(input(f'{man}:'))
        if question == people_dates[man]:
            print(f'Правильно')
            brain += 1
        else:
            print(f'Неправильно, правильная дата рождения: {people_word_dates[man]}')
            stupid += 1
    print('Количество правильных ответов:', brain)
    print('Количество неправильных ответов:', stupid)
    desire = str(input('Хотите начать заново? yes/no:'))