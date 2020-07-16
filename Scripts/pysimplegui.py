# Import
import PySimpleGUI as sg

# Layout
layout = [
    [sg.Text("My layout", key="-TEXT-")],
    [sg.Input(key="-INPUT-"), sg.Button("Update Input")],
    [
        sg.Combo(("blue", "red", "brown", "yellow"), key="-COLOR-"),
        sg.Button("Update Color"),
    ],
    [sg.Button("OK"), sg.Button("Cancel")],
]

# Window
window = sg.Window("Persistant Window", layout)

# Event loop
if __name__ == "__main__":
    while True:
        event, values = window.read()
        print(event, values)  # CLI debug
        if event in (None, "Cancel"):
            break
        if event in ("Update Input"):
            window["-TEXT-"].update(values["-INPUT-"])
        if event in ("Update Color"):
            window["-TEXT-"].update(text_color=values["-COLOR-"])
        if event in ("OK"):
            window["-TEXT-"].update(values["-INPUT-"])
            window["-TEXT-"].update(text_color=values["-COLOR-"])

    # Make sure always to close the window
    window.close()
