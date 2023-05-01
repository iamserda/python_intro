

def to_fizz_buzz_form(fizz:str="Fizz", buzz:str="Buzz", rg:int=100):
    fizz_buzz = str(fizz) + str(buzz)
    for i in range(1,int(rg)):
        a = i % 3 == 0 # True or False
        b = i % 5 == 0 # True or False
        print( fizz_buzz.title() if a and b else fizz.title() if a else buzz.title() if b else i)
    print("(THE END)\n\n")

to_fizz_buzz_form() # fizz, buzz, fizz_buzz, i(1,100)
to_fizz_buzz_form("Adams", "Family", 15) # Adams, Family, AdamsFamily, i
to_fizz_buzz_form("super", "mario", 30) # Super, Mario, SuperMario, i