
import PySimpleGUI as sg


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [ [sg.Text('Specify the path to the folder with photos'), sg.InputText()],
            [sg.Text('Specify the path to the file with coordinates'), sg.InputText()],
            [sg.Text('Specify the path to the file classes'), sg.InputText()],
            [sg.Text('Specify the path to the file that contains the name of the image and the name of the class to '
                     'which this image belongs'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Converter', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()