import functions


def get_todo():
    file = open('todos.txt', 'r')
    todos = file.readlines()
    return todos

def write_todo(todos):
    file = open('todos.txt', 'w')
    file.writelines(todos)
    file.close()
def edit_todo(todo_to_edit,new_todo):
    todos = functions.get_todo()
    index = todos.index(todo_to_edit)
    todos[index] = new_todo+'\n'
    file = open('todos.txt', 'w')
    file.writelines(todos)
    file.close()
    return todos








