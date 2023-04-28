print("Hello World")
greeting = "Hi, welcome to"
brand_name = "HealthFit"
print(greeting, brand_name)
print(bool(""))  # False
print(bool("1"))  # True
print(bool(1))  # True
print(bool(str(1)))  # True
print(bool(0))  # False
print(bool(str(0)))  # True
a = 1
b = 2
c = a > b
d = b > a
print("c is", c)  # False
print("d is", d)  # True

greet = "Global Hello!"


def greet_function(greet):
    print(greet)  # uses "Global Hello" the received argument.

    # creates a local variable, greet. IT DOES NOT UPDATE or CHANGE outer greet variable.
    greet = "Local and " + greet
    print(greet)
    return greet  # "Local Hello"


# printing returned value from executing the function.
print(greet_function(greet))
print(greet)  # prints "Global Hello"



