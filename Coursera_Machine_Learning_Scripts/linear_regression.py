from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import matplotlib


sg.theme("DarkGreen")
plt.style.use("seaborn-darkgrid")


class Gui:
    def __init__(self):
        self.UI_col = [
            [sg.Button("Generate points")],
            [sg.Button("Draw baseline")],
            [sg.Button("Plot exp")],
            [sg.Text("c0"), sg.Input("N/A", readonly=True, key="-c0-")],
            [sg.Text("c1"), sg.Input("N/A", readonly=True, key="-c1-")],
        ]

        self.gradient_desc_col = [[sg.Canvas(key="-GRAD_DESC-", size=(500, 400))]]

        self.lin_plot_col = [[sg.Canvas(key="-LINE_PLOT-", size=(500, 400))]]

        self.layout = [
            [
                sg.Col(self.UI_col),
                sg.VerticalSeparator(),
                sg.Col(self.gradient_desc_col),
                sg.VerticalSeparator(),
                sg.Col(self.lin_plot_col),
            ]
        ]

        self.window = sg.Window("Linear Regression", self.layout, finalize=True)

    def draw_figure(canvas, figure, loc=(0, 0)):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
        return figure_canvas_agg


class Linear:
    def __init__(self):
        self.generate_points()

    def calculate_loss(self):
        self.y_pred = np.array([self.c0 + i * self.c1 for i in self.x])
        self.y_diff = self.y_pred - np.array(self.y)
        loss = sum([i ** 2 for i in self.y_diff])
        print(self.y)
        print(self.y_pred)
        print(self.y_diff)
        print(loss)
        return loss

    def generate_points(self):

        self.x = [point * 10 for point in np.random.rand(10)]
        self.y = [point * 10 for point in np.random.rand(10)]
        self.df = pd.DataFrame({"x": self.x, "y": self.y})

        self.fig, self.ax = plt.subplots(1, 1)
        self.df.plot(kind="scatter", x="x", y="y", ax=self.ax)
        self.ax.set_xlabel("x", size=20)
        self.ax.set_ylabel("y", size=20, rotation="horizontal")
        self.ax.set_xticks(np.arange(0, 11, 1))
        self.ax.set_yticks(np.arange(0, 11, 1))
        self.ax.autoscale(False)
        self.c0 = np.mean(self.y)
        self.c1 = 0
        df = self.generate_line(self.c0, self.c1)
        df.plot(x="t", y="y", ax=self.ax)

        loss = self.calculate_loss()
        y_ref = list(zip(self.y, self.y_pred))
        self.ax.plot(
            (self.x, self.x), ([i for i, j in y_ref], [j for i, j in y_ref]), color="r",
        )
        print(self.ax.lines)

        return self.fig, loss

    def generate_line(self, c0, c1):
        t = np.linspace(0, 10, 1000)
        y = [c0 + i * c1 for i in t]
        df = pd.DataFrame({"t": t, "y": y})
        return df

    def show_loss(self, fig):
        self.ax.lines = []
        print(self.ax.lines)
        return fig


def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg


def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close("all")


def main():
    g = Gui()
    lin = Linear()
    # lin.generate
    figure_canvas_agg_lp = None
    figure_canvas_agg_gd = None

    fig, loss = lin.generate_points()
    if figure_canvas_agg_lp:
        delete_figure_agg(figure_canvas_agg_lp)
    figure_canvas_agg_lp = draw_figure(g.window["-LINE_PLOT-"].TKCanvas, fig)

    while True:
        event, values = g.window.read()
        print(event, values)
        if event is None:
            break
        if event in ("Generate points"):
            fig, loss = lin.generate_points()
            if figure_canvas_agg_lp:
                delete_figure_agg(figure_canvas_agg_lp)
            figure_canvas_agg_lp = draw_figure(g.window["-LINE_PLOT-"].TKCanvas, fig)
        if event in ("Plot exp"):
            fig = lin.show_loss(lin.fig)
            if figure_canvas_agg_lp:
                delete_figure_agg(figure_canvas_agg_lp)
            figure_canvas_agg_lp = draw_figure(g.window["-LINE_PLOT-"].TKCanvas, fig)
            # fig = lin.plot_exp()
            # if figure_canvas_agg_gd:
            #     delete_figure_agg(figure_canvas_agg_gd)
            # figure_canvas_agg_gd = draw_figure(g.window["-GRAD_DESC-"].TKCanvas, fig)
        if event in ("Draw baseline"):
            fig, loss = lin.plot_baseline()
            if figure_canvas_agg_lp:
                delete_figure_agg(figure_canvas_agg_lp)
            figure_canvas_agg_lp = draw_figure(g.window["-LINE_PLOT-"].TKCanvas, fig)


if __name__ == "__main__":
    main()
