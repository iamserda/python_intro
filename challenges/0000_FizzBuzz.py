
def to_fizz_buzz_form(fizz:str="Fizz", buzz:str="Buzz", rg:int=100)-> None:
    """ A function to solve the fizz-buzz problem. 
    Allows users to replace the values to be shown, 
    for example "Super" for "Fizz", "Mario" for Buzz
    
    Args:
        fizz (str, optional): _description_. Defaults to "Fizz".
        buzz (str, optional): _description_. Defaults to "Buzz".
        rg (int, optional): _description_. Defaults to 100.

    Returns:
        None: a void function, it returns None by default.
    """
    try:
        fizz, buzz, rg = str(fizz).title(), str(buzz).title(), int(rg)
    except Exception as err:
        print(f"Error: {err}. Terminated prematurely...")
    
    #The actual puzzle-solver!
    # Could be a one-liner, but I hate 1-liners.
    # They are often ineficient, as in this case.
    fizz_buzz = fizz + buzz
    # for i in range(1,rg): fb if (i % 3 == 0) and (i % 5 == 0) else fz if (i % 3 == 0) else bz if (i % 5 == 0) else i
    # the option below reduces the number of calc, especially the compounded one(and) above.
    for i in range(1,rg):
        a = i % 3 == 0 # True or False
        b = i % 5 == 0 # True or False
        print( fizz_buzz if a and b else fizz if a else buzz if b else i)

to_fizz_buzz_form() # uses default values: "Fizz", "Buzz", 100
to_fizz_buzz_form(list(), dict(), "20") # "[]", "{}", "16", <- Weird Edge Case
to_fizz_buzz_form("super", "mario", 31) # Super, Mario, SuperMario, i <- Reg Test