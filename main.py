from typing import List

import PySimpleGUI as sg

from app.elements import render_stats
from app.models import Stats


def run_app():
    base_stats = Stats()
    modified_stats = Stats()
    modified_stats.energy += 41
    layout = [
        [
            sg.Column(render_stats(base_stats, "Base statistics")),
            sg.Column(render_stats(modified_stats, "Modified statistics")),
            sg.VSeparator()
        ]
    ]
    window = sg.Window("Verns are best", layout, size=(800, 600))
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_app()
