user_input_1 = str(input('Введите любые числа для заполнения первого списка через запятую:'))
user_input_2 = str(input('Введите любые числа для заполнения второго списка через запятую:'))
user_input_1 = user_input_1.split(',')
user_input_2 = user_input_2.split(',')
for i in user_input_2:
    user_input_1.remove(i)
print(sorted(user_input_1, key=int))