class Student:
    #height=170
    def __init__(self):
        print(self.height)
        self.height = 230
    height = 200
    def printer(self):
        print(self.height)

Ira = Student()
Ira.printer()