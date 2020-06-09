#!/usr/bin/python3
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
<<<<<<< HEAD

class CHRONOCARCommand(cmd.Cmd):
    """ Contains the methods to work into the commands line """
    """ Custom prompt """
    prompt = '(chronocar)$ '
    list_class = ["BaseModel", "User"]
    list_err = ["** class name missing **", "** class doesn't exist **",
                "** instance id missing **", "** no instance found **",
                "** attribute name missing **", "** value missing **"]

    def do_quit(self, line):
        """ Quit - command to exit the console """
        return True

    def do_EOF(self, line):
        """ EOF - command to exit the console """
        return True

    def do_empty_line(self):
        """ Empty line + ENTER shouldn’t execute anything """
        pass

    def do_create(self, line):
        """ Create a new instance of BaseModel """
        my_list = list(line.split())
        if line == "":
            print(self.list_err[0])
        elif my_list[0] in self.list_class:
            obj = eval(my_list[0])()
            models.storage.insert(obj)
            print(obj.id)
            obj.save()
        else:
            print(self.list_err[1])

    def do_show(self, line):
        """ Show object by id """
        my_list = list(line.split())
        if line == "":
            print(self.list_err[0])
        elif my_list[0] not in self.list_class:
            print(self.list_err[1])
        elif len(my_list) == 1:
            print(self.list_err[2])
        else:
            mycls = eval(my_list[0])()
            my_obj = models.storage.getobject(mycls.__class__, my_list[1], my_list[2] )          
            if my_obj is not None:
                print(my_obj[0].name)
            else:
                print(self.list_err[3])

    def do_destroy(self, line):
        """ Delete object by id """
        my_list = list(line.split())
        if line == "":
            print(self.list_err[0])
        elif my_list[0] not in self.list_class:
            print(self.list_err[1])
        elif len(my_list) == 1:
            print(self.list_err[2])
        else:
            mycls = eval(my_list[0])()
            my_obj = models.storage.getobject(mycls.__class__, my_list[1], my_list[2] )
            print("my_obj ", my_obj)
            if my_obj is not None:  
                models.storage.delete(my_obj[0])
            else:
                print(self.list_err[3])

    def do_all(self, line):
        """ Function that displays all class instances of given argument or all
        if no argument given """
        dict_temp = models.storage.all()
        if line is "":
            list_obj = []
            for obj_id in dict_temp.keys():
                obj = dict_temp[obj_id]
                list_obj.append("{}".format(obj))
            print(list_obj)
        else:
            my_list = line.split()
            if my_list[0] not in self.list_class:
                print(self.list_err[1])
            else:
                list_obj = []
                for key, value in dict_temp.items():
                    if value.__class__.__name__ == my_list[0]:
                        list_obj.append("{}".format(value))
                print(list_obj)

    def do_update(self, line):
        """ Update an object by className and id, with attribute and value """
        my_list = self.splitter(line)
        my_dic = models.storage.all()
        if line == "":
            print(self.list_err[0])
        elif my_list[0] not in self.list_class:
            print(self.list_err[1])
        elif len(my_list) < 2:
            print(self.list_err[2])
        else:
            if (my_list[0] + "." + my_list[1]) in my_dic.keys():
                if len(my_list) < 3:
                    print(self.list_err[4])
                elif len(my_list) < 4:
                    print(self.list_err[5])
                else:
                    obj_dic = my_dic[my_list[0] + "." + my_list[1]]
                    setattr(obj_dic, my_list[2], my_list[3].replace("\"", ""))
                    models.storage.save()
            else:
                print(self.list_err[3])

    def splitter(self, line):
        """Function to split line into arguments using shlex"""
        lex = shlex.shlex(line)
        lex.quotes = '"'
        lex.whitespace_split = True
        lex.commenters = ''
        return list(lex)


if __name__ == '__main__':
    """ Executed the loop for promp by default """
    CHRONOCARCommand().cmdloop()
