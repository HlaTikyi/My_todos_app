from ctypes import alignment

import functions
import functions as fcn
import PySimpleGUI as sg

Label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip='Enter todo', key='inputToAdd')
list_box = sg.Listbox(values=fcn.get_todo(),key='listSelect',enable_events= True,size=[45,10])
edit_button = sg.Button('Edit',disabled=True)
add_button = sg.Button('Add',size=[10,1])
del_button = sg.Button('Delete',disabled=True)

Layout = [[Label],[input_box, add_button],[list_box,edit_button,del_button]]

window = sg.Window("My To - Do APP", layout = Layout, font=('Helvetica', 24))

while True:
    event, value = window.read()


    match event:
        case'Add':
            todos = functions.get_todo()
            new_todo = value['inputToAdd'] +'\n'
            todos.append(new_todo)
            functions.write_todo(todos)
            window['listSelect'].update(values=todos)
            window['inputToAdd'].update(value='')
        case'listSelect':
            val = value['listSelect'][0]
            str(val)
            window['inputToAdd'].update(value=val)
            edit_button(disabled=False)
            del_button(disabled=False)

        case 'Edit':
             try:
                 todo_to_edit = value['listSelect'][0]
                 new_todo = value['inputToAdd']
                 todos = functions.edit_todo(todo_to_edit,new_todo)
                 window['listSelect'].update(values=todos)
                 window['inputToAdd'].update(value='')
                 edit_button(disabled=False)
             except:
                 sg.popup('Please Select a todos')
        case 'Delete':
            try:
                    todo_to_del = value['listSelect'][0]

                    todos = functions.get_todo()
                    todos.pop(todos.index(todo_to_del))
                    window['listSelect'].update(values=todos)
                    window['inputToAdd'].update(value='')
                    del_button(disabled=False)
            except:
                sg.popup("Please Select A todo")







        case sg.WIN_CLOSED:
            break





window.close()
exit()