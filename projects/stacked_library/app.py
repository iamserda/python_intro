# stacks -> LIFO data structure -> list() is good for this.
def using_list_as_stacks():
    try:
        books_bin1 = []
        user_borrowed = []
        print("Welcome to 'Stacked Library': where you can only pick the most recently returned books!")
        menu = """Menu: 
            1.- Drop off a book? Enter '1'
            2.- Pick up a book? Enter '2'
            3.- exit app. Enter 'x'
            4.- show my_account 'account'
            5.- show lib-books 'available'
            """
        print(menu)

        _continue_flag = True
        
        while _continue_flag:
            choice = input(f"Enter your selection from the menu: '1' to drop-off, '2' to borrow, or 'x' to exit:\n$-: ").lower()
            if choice == "x":
                    break
            if choice == "0":
                print(menu)
                continue
            if choice == "1":
                choice = input("$-: Enter book's title: ").lower()
                if choice == "x":
                    break
                else: 
                    books_bin1.append(choice.title())
                    continue
            elif choice == "2":
                if len(books_bin1):
                    user_borrowed.append(books_bin1.pop())
                    print("account: ", user_borrowed)
                    continue
                else:
                    print("We do not have any books on hand at the moment. Please try again later...")
                    continue
            elif choice == "account":
                print(f"Account:\nOutstanding: {len(user_borrowed)}\n List:{user_borrowed}")
            elif choice == "available":
                print(f"Library:\n Available:{len(books_bin1)}\nOutstanding: {len(user_borrowed)}")
            else:
                raise ValueError(f"{choice} is not a valid option. Terminating the app... entered is not on the list of options.")
        print("Terminating at user's request...")
        return -1
    except Exception as err:
        print(f"Error: {err}")
        print("Terminating...")
        return -1    

using_list_as_stacks()