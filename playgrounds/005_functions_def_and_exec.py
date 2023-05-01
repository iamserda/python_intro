greet = "Global Greet Variable."
def greet_function(greet: str) -> str:
    """A function with some parameters, and type hinting...returns a string."""
    greet = "Local Greet Variable"
    print("Here 'greet' is:", greet)
    return greet

# printing returned value from executing the function.
print(greet)  # prints "Global..."
greet = greet_function(greet)
print(greet) # updated Global greet variable. 

