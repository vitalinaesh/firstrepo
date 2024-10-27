class NS:
    def __init__(self, name, surname):
        self.name= name
        self.surname = surname
class Student:
    studentam = 0
    def __init__(self,name,surname,age,height=160):
        self.height = height
        self.ns = NS(name, surname)
        self.age = age
        Student.studentam += 1



    def printst(self):
        print(f'Height : {self.height}')
        print(f'Name : {self.ns.name}')
        print(f'SurName : {self.ns.surname}')
        print(f'Age : {self.age}')

    def agebrth(self):
        self.age += 1
        print(f"happy b-day tj {self.ns.name}. Now you {self.age}!")

print(f'before creating Student object {Student.studentam}')
frstudent = Student('Vitalina', 'Dunets', 13)
frstudent.printst()
print(Student.studentam)
print(f'after creating student object {Student.studentam}')

print(f'before one year  {Student.agebrth}')


frstudent.agebrth()