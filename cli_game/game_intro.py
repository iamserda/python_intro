def generate_greeting(filepath="./content/welcome.txt", option="r"):
    with open(filepath, option) as file:
        greeting = file.read()
    return greeting
