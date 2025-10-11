class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    

make = input("Введіть марку авто - ")
model = input("Введіть модель авто - ")
year= input("Введіть рік авто - ")

my_car = Car(make,model,year)
print(my_car.get_info())




class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimetera(self):
        return 2 * (self.width + self.height)
    
w = float(input("Введіть ширину - "))
h = float(input("Введіть висоту - "))

rect = Rectangle(w, h)

print ("Площа: ", rect.calculate_area() )
print ("Периметр: ", rect.calculate_perimetera() )
 
