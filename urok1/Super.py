class Zoo:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Тварина видає звук")

class Dog(Zoo):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"{self.name} каже гав гав")


class Cat(Zoo):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"{self.name} каже мяу мяу")


dog = Dog("Грета")
cat = Cat("Найс")

dog.sound()
cat.sound()
