import logging
logging.basicConfig(level=logging.INFO,
                    filename='logs.log',
                    filemode='w',
                    format='%(levelname)s%(asctime)s - %(message)s')

logging.info("program start")

class NS:
    def __init__(self, name: str, surname: str):
        if type(name) != str:
            raise TypeError('Name is not a string')
        if type(surname) != str:
            raise TypeError('Surname is not a string')
        self.name = name
        self.surname = surname

class Student:
    studentam = 0

    def __init__(self, name: str, surname: str, age: int, height: int = 160):
        if age <= 0:
            raise TypeError('Age must be greater than 0') 
        self.height = height
        self.ns = NS(name, surname)
        self.age = age
        Student.studentam += 1
        logging.info(f"Зроблен  Student: {self.ns.name} {self.ns.surname}")

    def printst(self):

        print(f'Height: {self.height}')
        print(f'Name: {self.ns.name}')
        print(f'Surname: {self.ns.surname}')
        print(f'Age: {self.age}')

    def agebrth(self):
        self.age += 1
        print(f"Happy birthday to {self.ns.name}! Now you are {self.age} years old!")

try:
    logging.debug("performance program (In progress...)")
    frstudent = Student('Vitalina', 'Dunets', 13)
    secondstudent = Student("Elya", "Pystovit", 65)
    frstudent.printst()
    secondstudent.printst()
except Exception as error:
    print(f"Error: {error}")
    logging.error("Exception")

logging.info("end of program")


print("Next code")
print(f'Number of students: {Student.studentam}')

