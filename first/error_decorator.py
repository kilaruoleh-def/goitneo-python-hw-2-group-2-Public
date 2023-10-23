def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No contact found for this name."
        except ValueError:
            return "Invalid format for action. Use '[name] [phone]' after action."
        except IndexError:
            return "No contacts saved."
        except Exception as error:
            return f"An unexpected error occurred: {error}"
    return inner
