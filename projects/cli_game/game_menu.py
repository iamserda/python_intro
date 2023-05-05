def read_command():
    print("""
          Menu:
          0 - Type 'h' or 'help' to get some help.
          9a - Enter "q" to quit(cowardly).
          9b - Enter "x" to exit. Game status will be saved. You will be offered the option to continue.""")
    print("Enter commands from the menu:")

    while (True):
        command = input("$->: ")
        if command.lower() == 'x':
            print("saving progress...\n")
            break
        if command.lower() == 'q':
            print("Quitter... Quitter... Quit....ter....")
            print("Progress deleted...\n")
            print("Final Score:")
            break
        if command.lower() == 'h' or command.lower() == 'help':
            #show the help list or menu.
            continue
        print(command)
