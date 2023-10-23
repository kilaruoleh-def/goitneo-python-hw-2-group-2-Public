import re
from typing import Optional

from error_decorator import input_error


class AssistantBot:
    def __init__(self) -> None:
        """Initialize the bot with an empty contacts dictionary."""
        self.contacts = {}

    def execute_command(self, command: str) -> str:
        """Execute a given command and return the bot's response."""
        command_pattern = re.compile(r'(\w+)(?:\s+(.*))?')
        match = command_pattern.match(command)

        if not match:
            return "Invalid command."

        cmd, args = match.groups()
        cmd = cmd.lower()

        command_function = {
            "hello": self.hello,
            "add": self.add_contact,
            "change": self.change_contact,
            "phone": self.show_phone,
            "all": self.show_all,
        }.get(cmd)

        if command_function:
            return command_function(args)

        if cmd in ["close", "exit"]:
            raise SystemExit("Good bye!")

        return "Invalid command."

    def hello(self, _: Optional[str]) -> str:
        """Handle the 'hello' command."""
        return "How can I help you?"

    @input_error
    def add_contact(self, args: Optional[str]) -> str:
        """Add a contact to the contacts' dictionary."""
        if not args or len(args.split()) != 2:
            raise ValueError
        name, phone = map(str.strip, args.split(None, 1))
        self.contacts[name] = phone
        return "Contact added."

    @input_error
    def change_contact(self, args: Optional[str]) -> str:
        """Change the phone number of an existing contact."""
        if not args or len(args.split()) != 2:
            raise ValueError
        name, new_phone = map(str.strip, args.split())
        if name not in self.contacts:
            raise KeyError
        self.contacts[name] = new_phone
        return "Contact updated."

    @input_error
    def show_phone(self, args: Optional[str]) -> str:
        """Show the phone number for a given contact name."""
        if not args:
            raise ValueError
        name = args.strip()
        if name not in self.contacts:
            raise KeyError
        return self.contacts[name]

    @input_error
    def show_all(self, _: Optional[str]) -> str:
        """Show all saved contacts and their phone numbers."""
        if not self.contacts:
            raise IndexError
        return '\n'.join([f"{name}: {phone}" for name, phone in self.contacts.items()])
