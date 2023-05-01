print("(START)\n")
#   COMMENTS:
#   course: An Intro to Python: Python from multiple-sources... Books, Tutorials, Challenges, Etc...

# VARIABLES:
# "Warren E. Buffett" is store in memory. 'person_name' is directly bound to that memory_location. This allows the programmer to quickly find and used the data store in that memory location.

username = "iamserda"
# PRIMITIVE TYPES:
# stings: characters between two quotation marks like this: "..."
person_name = "Serda" + ","
greet_p1 = "Hello"
greet_p2 = "Welcome to"
brand_name = "HealthFit.app"
print("username" + ": " + username)
print(greet_p1, person_name, greet_p2, brand_name+"!")
print() # creates an empty space.

# Primitive - Types : Integers or counting numbers or int
person_age = 2023 - 1990
print("Age:", person_age)
completed_sets = 4
print("Completed Sets:", completed_sets)
reps_per_set = 12
print("Total Number of Reps:", completed_sets * reps_per_set)

# floats or real numbers 32bit
body_mass_index = 32.9  # float
print("Body Mass Index:", body_mass_index)
account_balance = completed_sets * reps_per_set * 0.25  # float
print("Points Earned:", account_balance)

# boolean
is_active = True  # bool
print("Account Acitve:", is_active)
checked_in_today = False  # bool
print("Points Earned:", account_balance)
print()

# Built-in Methods: print(): a method/command in python used to display characters on the console/interpreter.
# execution_format: print(variable_or_literal)
# print does not return anything, effectively print(...) returns None.
# concatenation: combining strings together.
greeting = greet_p1 + " " + person_name + " " + greet_p2 + " " + brand_name + "!"
print("Brand:", brand_name)
print(greeting)
print("name:", person_name, "type:", type(person_name))
print("age:", person_age, "type:", type(person_age))
print("Points Earned:", account_balance, "type:", type(account_balance))
print("Account Active:", is_active, "type", type(is_active))
print("Checked-in:", checked_in_today, "type:", type(checked_in_today))

print("Primitive - Types : Real Number or floating point numbers or float\n")
print("bool(''): ", bool(""))    # False
print("bool('a'): ", bool('a'))   # True
print("bool('1'): ", bool('1'))   # True
print("bool(0): ", bool(0))     # True
print("bool(1): ", bool(1))     # True
print()
print("(END)\n")