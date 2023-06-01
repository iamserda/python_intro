class Person:
    def __init__(self,f:str,l:str,m:str="") -> None:
        self.first_name = f
        self.middle_name = m
        self.last_name = l
    def __str__(self):
        return f"""Person:\n(First: {self.first_name},\nLast: {self.last_name}{f", Middle: {self.middle_name}" if self.middle_name else ""})"""

class Student(Person):
    def setGrade(self, grade):
        self.grade = grade
    def getGrade(self):
        return self.grade
    def __str__(self):
        """ converts an instance or object into string and return it. """
        grade = self.getGrade()
        student =  """\nStudent:\n
first: {f}
middle: {m}
last: {l}
gpa: {g}""".format(f=self.first_name, m=self.middle_name, l=self.last_name, g=grade)
        return student


class Citizen(Person):
    def __init__(self, f: str, l: str = str(None), m: str = "", age:int=0, id:str="", voter_id:str="") -> None:
        super().__init__(f, l, m)
        self.dob = {}
        self.age = age
        self.id = id
        self.voter_id = str(voter_id)
    
    def set_dob(self, year, month, day)->None:
        self.dob = {
            "year": year,
            "month": month,
            "day": day
        }
    def get_age(self)->int:
        from datetime import datetime as time
        return int(time.now().year - self.dob["year"])
    
    def set_age(self)->None:
        self.age = self.get_age()

    def can_vote(self)->bool:
        if self.age >= 18:
            return True
        return False
    
    def __str__(self)->str:
        return f"""\nCitizen:\n( 
    "first-name": {self.first_name}
    "last-name": {self.last_name}
    "midde-name": {self.middle_name}
    "age": {self.age}
    "can-vote?": {self.can_vote()}
    "state-id" {self.id}
    "voter-id": {self.voter_id}
)"""

_person1 = Person("Amie","La Vendre","")
print(_person1)

_student1 = Student("Angela", "Duckworth") 
_student1.setGrade(3.23)
print(_student1)

_citizen1 = Citizen("Serda", "Python", "Pirate", 0, "NY-202039023", "NY-202039023-VID-1023-1020")
print(_citizen1)






"""
MY NOTES:

- What is a Class-level Attributes?
+ Class-level attributes: state defined at the class level. These attributes are shared between all instances of a given classes. If the value is change in 1 instance, it affects all other instances.


- What is an Instance Attribute?
+

- How does Class attributes differ from Instance attributes
+

# What is an "Instance Method?"
# What is a "Class Method?"
# What is the difference between "Instance" vs "Class" Methodss

"""

