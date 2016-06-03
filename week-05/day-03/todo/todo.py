import sys
import csv

class Todo(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.action_handler = {
            '-l': self.print_action,
            '-a': self.add_action,
            '-r': self.remove_action,
            '-c': self.complete_action
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
                else:
                    print('Error: Unsupported argument')
        except FileNotFoundError:
            new_file = open(self.file_name, 'a')
            new_file.close()
            print('file not found')
            print(self.file_name + ' file created')

    def menu(self):
        return '\n'.join([
            'Python Todo application',
            '=======================',
            '',
            'Command line arguments:',
            '-l   Lists all the tasks',
            '-a   Adds a new task',
            '-r   Removes an task',
            '-c   Completes an task'
        ])

    def print_action(self, arg):
        print(self.get_todo_list())

    def get_todo_list(self):
        text_list = self.get_file_content()
        if text_list == []:
            return 'No todos for today! :)'
        lines_with_nums = ''
        num = 1
        todo_list = []
        for element in text_list:
            index = str(num)
            status_mark = self.get_status_mark(element[0])
            todo_item = element[1]
            todo_list += [index + ' - ' + status_mark + ' ' + todo_item]
            num += 1
        return '\n'.join(todo_list)

    def add_action(self, arg):
        if len(arg) == 3:
            self.add_new_todo(arg[2])
        else:
            print('Unable to add: No task is provided')

    def add_new_todo(self, new_todo):
        new_item = 'False,' + new_todo + '\n'
        f = open(self.file_name,'a')
        f.write(new_item)
        f.close()

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
        todo_items = self.get_file_content()
        if num > len(todo_items):
            raise IndexError
        index = num - 1
        new_list = todo_items[:index] + todo_items[index + 1:]
        self.write_file_content(new_list)

    def get_status_mark(self, element):
        if element == 'False':
            return '[ ]'
        else:
            return '[x]'

    def complete_action(self, arg):
        try:
            if len(arg) == 3:
                self.complete_nth_element(int(arg[2]))
            else:
                print('Unable to add: No index is provided')
        except ValueError:
            print('Unable to check: Index is not a number')
        except IndexError:
            print('Unable to check: Index is out of bound')

    def complete_nth_element(self, num):
        todo_items = self.get_file_content()

        item_to_complete = todo_items[num - 1]
        if item_to_complete[0] == 'False':
            item_to_complete[0] = 'True'
        else:
            item_to_complete[0] = 'False'

        self.write_file_content(todo_items)

    def get_file_content(self):
        f = open(self.file_name, 'r')
        content_list = list(csv.reader(f))
        f.close()
        return content_list

    def write_file_content(self, list):
        f = open(self.file_name, 'w', newline = '')
        writer = csv.writer(f)
        writer.writerows(list)
        f.close()

todo = Todo('todos.csv')
todo.main()
