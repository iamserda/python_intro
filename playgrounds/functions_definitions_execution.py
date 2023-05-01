greet = "Hello World!" # greet(scope: global)

# def function_name(param:data_type)->return data_type:
def greet_function(greet:str)->str:
    print(greet)  # uses "Global Hello" the received argument.

    # creates a local variable, greet. IT DOES NOT UPDATE or CHANGE outer greet variable.
    greet = "Local and " + greet
    print(greet)
    return greet  # "Local Hello"

def addition_with_default_args(a:int, b:int=3)->int:
    return a + b

# accepts 0 or more arguments
def with_one_or_more_args(*args:tuple) -> tuple:
    if not len(args):
        return args, tuple()
    doubled = tuple([x**2 for x in args])
    return args, doubled

# printing returned value from executing the function.
print(greet_function(greet))
print(greet)  # prints "Global Hello"

answ = addition_with_default_args(1,2) # 1 + 2 = 3
print(answ) # 3
answ = addition_with_default_args(2) # 2 + 3 = 5
print(answ) # 5

# receiving more than one value from a function execution.
# more than 1 arg. args are separated with a comma
sent, rcvd = with_one_or_more_args(1,2,3,4,5) 
print(f"sent: {sent} => received: {rcvd}")

sent, rcvd = with_one_or_more_args(1) # one arg
print(f"sent: {sent} => received: {rcvd}")

sent, rcvd = with_one_or_more_args() # no arg
print(f"sent: {sent} => received: {rcvd}")