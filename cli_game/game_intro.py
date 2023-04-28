def generate_greeting(filepath:str="./content/welcome.txt", option:str="r")->str:
    with open(filepath, option) as file:
        greeting = file.read()
    return greeting
