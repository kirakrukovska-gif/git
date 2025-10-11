a = int(input("Введіть перше число - "))
b = int(input("Введіть друге число - "))
act = input("Введіть дію (+, -, *, /)")

if act == "+":
   print(a + b) 
elif act == "-":
   print(a - b) 
elif act == "*":
   print(a * b) 
elif act == "/":
   if b == 0:
        print("Ділення на нуль")
   else:
        print(a / b) 
else:
    print("Невідома дія")
