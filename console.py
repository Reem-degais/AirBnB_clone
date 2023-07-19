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
from models.base_model import BaseModel
import shlex
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB program."""
    prompt = "(hbnb) "

    __classes = {
        "BaseModel", "User", "State",
        "City", "Place", "Amenity",
        "Review"}

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

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id.

        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance.

        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        instances = storage.all()
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id.

        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        instances = storage.all()
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances.

        Usage: all [class name]
        """
        args = arg.split()
        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] in HBNBCommand.__classes:
            class_instances = [str(
                obj
                ) for obj in storage.all().values() if type(
                obj).__name__ == args[0]]
            print(class_instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            obj = storage.all()[key]
            setattr(obj, args[2], args[3].strip('"'))
            storage.save()
        else:
            print("** no instance found **")

    def default(self, arg):
        """to handel using: <class name>.fun()"""
        args = arg.split('.', 1)
        if args[0] in HBNBCommand.__classes:
            if args[1].strip('()') == 'count':
                self.do_count(args[0])
            elif args[1].strip('()') == 'all':
                self.do_all(args[0])
            elif args[1].split('(')[0] == 'show':
                self.do_show(args[0])+' '+args[1].split('(')[1].strip(')'))
            elif args[1].split('(')[0] == 'destroy':
                self.do_destroy(args[0])

    
    def do_count(self, arg):
        """to retrieve the number of instances of a class"""
        count = 0
        for obj in storage.all().values():
            if arg == obj.__class__.__name__:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
