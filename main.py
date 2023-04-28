from cli_game import game, game_menu


def start_game()->None:
    greeting = game.greet_user()
    print(greeting)


if __name__ == "__main__":
    start_game()
    game_menu.read_command()
