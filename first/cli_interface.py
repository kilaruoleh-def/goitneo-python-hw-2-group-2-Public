from bot_core import AssistantBot


def bot_cli() -> None:
    """Command Line Interface for the AssistantBot."""
    bot = AssistantBot()
    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("> ")
            response = bot.execute_command(user_input)
            print(response)
        except SystemExit as e:
            print(e)
            break
