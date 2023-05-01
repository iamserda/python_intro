
def greet_():
    """void function, function that returns nothing"""
    greet = "Hello, Welcome to Python World!"
    print(greet)
    # implicitly returns None.


print(greet_(), type(greet_()))  # None, <class 'NoneType'>


def greet_2() -> str:
    """
    Type hinting... predefined types accepted and/or return by the function
    A function that takes no argument, returns data of type string.
    format: def function_name(arg_1:type_1,..., arg_n:type_n): expected_data_type_returned
    Returns:
        str: this function returns 'Hello, Welcome to Python World' as a string
    """
    return "Hello World!"


greet = "Global " + greet_2()
print(greet)