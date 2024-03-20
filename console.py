#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """program was terminated by user"""
        return True

    def do_quit(self, line):
        """Quits the program"""
        return True

    def help_quit(self):
        """Quit comand help page"""
        print("Quit command to exit the program")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()