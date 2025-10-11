import random

number = random.randint(1,10)
attempt = 3

while attempt:
    n = int(input("Вгадайте число "))
    if n == number:
        print('Правильно!')
        break
    elif n > number:
        print("менше")
    else:
        print("більше")
    attempt -= 1

if attempt == 0 and n!=number:
     print(f"Не вгадали, було загадано число {number}")
    