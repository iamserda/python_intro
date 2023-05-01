class Person():
    def __init__(self,f:str,l:str=str(None),m:str="") -> None:
        self.first_name = f
        self.middle_name = m
        self.last_name = l

class Student(Person):
    def setGrade(self, grade):
        self.grade = grade
    def getGrade(self):
        return self.grade
    def __str__(self):
        grade = self.getGrade()
        student =  """
student:
    first: {f}
    middle: {m}
    last: {l}
    gpa: {g}""".format(f=self.first_name, m=self.middle_name, l=self.last_name, g=grade)
        return student
student1 = Student("Serda", "Python", "Pirate")
student1.setGrade(3.23)
print(student1)
