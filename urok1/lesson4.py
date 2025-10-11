# class Parent:
#     classmethods and attrs
# class Child(Parent):
#     classmethods and attrs

# class Human:
#     height = 170
# class Student(Human):
#     pass 
# class Worker(Human):
#     pass
# nick = Student()
# ann = Worker()
# print(nick.height)
# print(ann.height)    


# class Woww:
#     def __wow(self):
#         print("Wow")
    
#     def __hello(self):
#         print("hello")
# wow = Wow()
# wow.hello_hello()
# wow.__Wow__wow()


class Class1:
    var = 30
    def __init__(self):
        self.var = 15
class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)

obj = Class2()
