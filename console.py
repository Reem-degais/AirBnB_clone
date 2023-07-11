#!/usr/bin/python3
"""
console.py

This module provides the command-line interpreter for the HBNB program.

It defines the `HBNBCommand` class, which inherits from `cmd.Cmd` and
implements the command interpreter functionality.

The command interpreter supports the following commands:
- quit: Exit the program.
- EOF: Exit the program with EOF (Ctrl+D).
- <empty line>: Do nothing when an empty line is entered.

Usage:
    ./console.py
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB program."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D).

        Usage: Ctrl+D
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

