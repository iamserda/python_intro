import os
def using_exceptions():
    os.system("clear") # clear screen at each run
    flag = True
    while flag:
        os.system("clear")
        try:
            username = input("Username: ")
            if username.isdigit():
                raise TypeError(f"Expected type: str, received type: {type(username)}.")
            return f"Hello {username}, Welcome to Python World!"
        except Exception as err:
            print(f"Error: {err}")
            if "y" == input("Would you like to continue? Enter 'y' for yes: ").lower():
                continue
            break


print(using_exceptions())