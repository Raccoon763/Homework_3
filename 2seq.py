mylist_true = []
user_input = str(input('Введите любые числа для заполнения списка через запятую, слэш, либо же точку с запятой:'))
if "," in user_input:
    razd = ","
elif "/" in user_input:
    razd = "/"
elif ";" in user_input:
    razd = ";"
mylist = user_input.split(razd)
for i in mylist:
    if mylist.count(i) == 1:
        mylist_true.append(i)
print(sorted(mylist_true, key=int))

