users = { "Маша" : "дитина", "Діма" : "дитина", "Кіра" : "підліток", "Андрій" : "підліток", "Микола" : "дорослий", "Вікторія" : "доросла",}

try:
    name = input("Введіть ім'я: ")
    if name not in users:
        raise NameError("Такого користувача не існує")
    print(name, "належить до групи:", users[name])

except NameError as e:
    print("помилка.", e)





