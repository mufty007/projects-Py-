import PySimpleGUI as sg

layout = [
    [sg.Text("This is layout and buttons sample")],
    [sg.Button("OK")]
]

#creating the window
window = sg.Window("Sample Two", layout)

#creating a while loop

while True:
    event, values = window.read()
    #end program if user closes the window
    #or press OK
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()