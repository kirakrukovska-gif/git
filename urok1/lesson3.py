class Human:
    def __init__ (self,name="Human"):
        self.name = name

# class Auto:
#     def __init__ (self,brand):
#         self.brand = brand
#         self.passengers = []
#     def add_passenger(self,*args):
#         for passenger in args:
#             self.passengers.append(passenge)
#     def print_passengers_names(self):
#         if self.passengers!= []:
#             print(f"Names of {self.brand} passengers:")
#             for passengers in self.passengers:
#                 print(passengers.name)
#         else:
#             print(f"There are no passengers in {self.brand}")


class School1:
    def __init__ (self,group):
        self.group = group
        self.students = []
    def add_student(self,*args):
        for student in args:
            self.students.append(student)

    def print_students_names(self):
        if self.students != []:
            print(f"Names of {self.group} students:")
            for student in self.students:
                print(student.name)
        else:
            print(f"There are no passengers in {self.group}")

class School2:
    def __init__ (self,group):
        self.group = group
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def print_students_names(self):
        if self.students != []:
            print(f"Names of {self.group} students:")
            for student in self.students:
                print(student.name)
        else:
            print(f"There are no passengers in {self.group}")

        
nick = Human("Nick")
kate = Human("Kate")
kira= Human("Kira")
jane = Human("Jane")
andrew = Human("Andrew")
school1 = School1("Group1")
school2 = School2("Group2")
school1.add_student(nick,kate,kira,jane,andrew)

for student in [nick,kate,kira,jane,andrew]:
    school2.add_student(student)



school1.print_students_names()
school2.print_students_names()


# car.add_passengers(nick,kate,kira,jane,andrew)
# car.print_passengers_names()
        