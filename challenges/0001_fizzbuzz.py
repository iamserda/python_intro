def fb(f:str="Fizz", b:str="Buzz", r:int=16)->None:
    for i in range(1,r): print(f+b if (i % 3 == 0) and (i % 5 == 0) else f if (i % 3 == 0) else b if (i % 5 == 0) else i)

fb()