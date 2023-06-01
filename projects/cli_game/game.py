from projects.cli_game import game_intro

def greet_user() -> str:
    user_name = input("Enter your name:")
    if not user_name:
        user_name = "Guest"
    greeting = game_intro.generate_greeting(
    ) + f"Hello {user_name}, and welcome to the main event! Enjoy!:\n"
    return greeting
