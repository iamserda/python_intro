class Student:
    def __init__(self,f:str, l:str, m:str="", gpa:float=0.0):
        self.firstname = str(f).capitalize()
        self.lastname = str(l).capitalize()
        self.middlename = m
        self.gpa = gpa
    
    def set_first(self, f_name):
        self.firstname = str(f_name)
    def set_last(self, l_name):
        self.lastname = str(l_name)
    def set_middle(self, m_name):
        self.middlename = str(m_name)
    def __str__(self):
        middle = f"\nMiddle: {self.middlename}" if self.middlename else ""
        return f"""First: {self.firstname}{middle}\nLast: {self.lastname}\n"""
    def __eq__(self, other) -> bool:
        return other.firstname == self.firstname and other.lastname == self.lastname and self.gpa == other.gpa and self.middlename == other.middlename

_student1 = Student("rogeR", "lamorT")
print(_student1)
_student2 = Student("sebastianna", "roSSi", m="Lisa", gpa=4.25)
print(_student2)
_student3 = Student("Roger", "Lamort")
_student4 = Student("Roger", "Lamort", "Anglade", 3.89)

print(_student1 == _student2) # False
print(_student1 == _student3) # True
print(_student3 == _student4) # False