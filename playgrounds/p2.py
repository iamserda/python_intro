class Person():
    def __init__(self,f:str,l:str,m:str="") -> None:
        self.first_name = f
        self.middle_name = m
        self.last_name = l

class Student(Person):
    
    def setGrade(self, grade):
        self.grade = grade

    def honk(self):
        print("Beep Beep")
        

student1 = Student("joe", "don", "mo")
student1.setGrade(3.98)
print(student1.first_name, student1.last_name, student1.middle_name, student1.grade)
