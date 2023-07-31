#import functions
import PySimpleGUI as sg

Label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip='Enter todo')
add_button = sg.Button("Add")

window = sg.Window("My To - Do APP", layout=[[Label],[input_box, add_button]])
window.read()
window.close()
