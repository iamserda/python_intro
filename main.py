from projects.cli_game import game, game_menu
import os


def start_game()->None:
    greeting = game.greet_user()
    print(greeting)


if __name__ == "__main__":
    os.system("clear")
    start_game()
    game_menu.read_command()
