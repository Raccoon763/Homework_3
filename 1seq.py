elem = int(input('Введите количество элементов:'))
spisok = []
for i in range(elem):
    s = input(f'Введите {i+1} элемент:')
    spisok.append(s)
print(sorted(spisok, key=int))