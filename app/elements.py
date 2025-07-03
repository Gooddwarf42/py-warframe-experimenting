from typing import List
import PySimpleGUI as sg
from PySimpleGUI import Element

from app.models import Stats


def render_stats(stats: Stats, header: str) -> List[List[Element]]:
    return [
        [sg.Text(header)],
        [sg.Text("Health: "), sg.Text(stats.health)],
        [sg.Text("Shield: "), sg.Text(stats.shield)],
        [sg.Text("Armor: "), sg.Text(stats.armor)],
        [sg.Text("Energy: "), sg.Text(stats.energy)],
    ]
