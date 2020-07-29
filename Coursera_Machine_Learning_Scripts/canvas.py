import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

"""
    Simultaneous PySimpleGUI Window AND a Matplotlib Interactive Window
    A number of people have requested the ability to run a normal PySimpleGUI window that
    launches a MatplotLib window that is interactive with the usual Matplotlib controls.
    It turns out to be a rather simple thing to do.  The secret is to add parameter block=False to plt.show()
"""


def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg


def draw_plot():
    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, 0.01)
    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
    fig_photo = draw_figure(window["-CANVAS-"].TKCanvas, fig)


layout = [
    [sg.Button("Plot"), sg.Cancel(), sg.Button("Popup")],
    [sg.Canvas(key="-CANVAS-", size=(500, 400))],
]

window = sg.Window("Have some Matplotlib....", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Cancel"):
        break
    elif event == "Plot":
        draw_plot()

    elif event == "Popup":
        sg.popup("Yes, your application is still running")
window.close()
