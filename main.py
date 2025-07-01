from typing import List

import PySimpleGUI as sg
from PySimpleGUI import Element

import constants.base_stats as BASE_STATS


class Stats:
    health: int
    shield: int
    armor: int
    energy: int

    def __init__(self):
        self.health = BASE_STATS.HEALTH
        self.shield = BASE_STATS.SHIELD
        self.armor = BASE_STATS.ARMOR
        self.energy = BASE_STATS.ENERGY


def render_stats(stats: Stats, header: str) -> List[List[Element]]:
    return [
        [sg.Text(header)],
        [sg.Text("Health: "), sg.Text(stats.health)],
        [sg.Text("Shield: "), sg.Text(stats.shield)],
        [sg.Text("Armor: "), sg.Text(stats.armor)],
        [sg.Text("Energy: "), sg.Text(stats.energy)],
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base_stats = Stats()
    modified_stats = Stats()
    modified_stats.energy += 41
    layout = [
        [
            sg.Column(render_stats(base_stats, "Base statistics"), background_color="green"),
            sg.Column(render_stats(modified_stats, "Modified statistics"), background_color="green"),
            sg.VSeparator()
        ]
    ]
    window = sg.Window("Verns are best", layout, size=(800, 600))
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

    window.close()
