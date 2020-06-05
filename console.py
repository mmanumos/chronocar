import cmd


class CHRONOCARCommand(cmd.Cmd):
    """contains the methods to work into the commands line"""
    prompt = '(chronocar)'
    """custom prompt"""

    def do_quit(self, line):
        """quit - command to exit the console"""
        return True

    def do_EOF(self, line):
        """EOF - command to exit the console"""
        return True

    def do_empty_line(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    """executed the loop for promp by default"""
    CHRONOCARCommand().cmdloop()
