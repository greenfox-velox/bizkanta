import sys
import csv

class Todo(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.action_handler = {
            '-l': self.print_action,
            '-a': self.add_action,
            '-r': self.remove_action,
        }

    def main(self):
        try:
            file = open(self.file_name, 'r')
            file.close()
            if len(sys.argv) == 1:
                print(self.menu())
            elif len(sys.argv) > 1:
                command = sys.argv[1]
                if command in self.action_handler:
                    action = self.action_handler[command]
                    action(sys.argv)
                    # self.action_handler[command](sys.argv)
                else:
                    print('Error: Unsupported argument')
        except FileNotFoundError:
            print('file not found')
            new_file = open(self.file_name, 'a')
            new_file.close()
            print(self.file_name + ' file created')

    def menu(self):
        return(
'Python Todo application\n\
=======================\n\n\
Command line arguments:\n\
-l   Lists all the tasks\n\
-a   Adds a new task\n\
-r   Removes an task\n\
-c   Completes an task')

    def print_action(self, arg):
        print(self.get_todo_list())

    def get_todo_list(self):
        f = open(self.file_name, 'r')
        lines = f.readlines()
        f.close()
        if lines == []:
            return 'No todos for today! :)'
        lines_with_nums = ''
        for i in range(len(lines)):
            lines_with_nums += str(i + 1) + ' - ' + '[ ] ' + lines[i]
        return lines_with_nums

    def add_action(self, arg):
        if len(arg) == 3:
            self.add_new_todo(arg[2])
        else:
            print('Unable to add: No task is provided')

    def add_new_todo(self, new_todo):
        f = open(self.file_name, 'a')
        list_with_new_todo = f.write(new_todo + '\n')
        f.close()
        return list_with_new_todo

    def remove_action(self, arg):
        try:
            if len(arg) == 3:
                self.remove_nth_element(int(arg[2]))
            else:
                print('Unable to remove: No index is provided')
        except ValueError:
            print('Unable to remove: Index is not a number')
        except IndexError:
            print('Unable to remove: Index is out of bound')


    def remove_nth_element(self, num):
        f = open(self.file_name, 'r')
        lines = f.readlines()
        f.close()
        if num > len(lines):
            raise IndexError

        f = open(self.file_name, 'w')
        index = num - 1
        new_list = lines[:index] + lines[index + 1:]
        new_todos = ('').join(new_list)
        f.write(new_todos)
        f.close()
        return new_todos


        # elif len(sys.argv) == 2 and sys.argv[1] == '-l':
        #     print(self.get_todo_list())
        # elif len(sys.argv) == 2 and sys.argv[1] == '-a':
        #     print('Unable to add: No task is provided')
        # elif len(sys.argv) == 3 and sys.argv[1] == '-a':
        #     self.add_new_todo(sys.argv[2])
        # elif len(sys.argv) == 3 and sys.argv[1] == '-r':
        #     self.remove_nth_element(int(sys.argv[2]))
        #     print('successful deleted, your todo list is:')
        #     print(self.get_todo_list())
        # self.action_handler['-a']('lk;lkjl')
        # self.action_handler['-r'](1)


todo = Todo('todos.csv')
todo.main()
