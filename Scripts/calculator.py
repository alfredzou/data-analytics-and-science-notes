import PySimpleGUI as sg

layout = [
    [sg.Text("My layout", enable_events=True, key="-TEXT-")],
    [sg.Input(key="-INPUT-")],
    [sg.Combo(("blue", "red", "brown", "yellow"), key="-COLOR-")],
    [sg.Button("OK"), sg.Button("Cancel")],
]

window = sg.Window("Design pattern 3- Persistant Window", layout)

while True:
    event, values = window.read()
    sg.Print(event, values)
    if event in (None, "Cancel"):
        break

window.close()
