from typing import List
import PySimpleGUI as sg
from PySimpleGUI import Element

from app.models import Stats, Equipment


def render_stats(stats: Stats, header: str) -> List[List[Element]]:
    return [
        [sg.Text(header)],
        [sg.Text("Health: "), sg.Text(stats.health)],
        [sg.Text("Shield: "), sg.Text(stats.shield)],
        [sg.Text("Armor: "), sg.Text(stats.armor)],
        [sg.Text("Energy: "), sg.Text(stats.energy)],
    ]

def render_equipments(equipments: List[Equipment]) -> List[List[Element]]:
    header = [
        sg.Text("Equipped", size=(10, 1), pad=(5, 5)),
        sg.Text("Name", size=(20, 1), pad=(5, 5)),
        sg.Text("Health", size=(8, 1), pad=(5, 5)),
        sg.Text("Shield", size=(8, 1), pad=(5, 5)),
        sg.Text("Armor", size=(8, 1), pad=(5, 5)),
        sg.Text("Energy", size=(8, 1), pad=(5, 5))
    ]

    rows = []
    for i, eq in enumerate(equipments):
        row = [
            sg.Checkbox("", key=f"-TOGGLE-EQUIP-{i}-", default=eq.is_equipped, enable_events=True, pad=(5, 5)),
            sg.Text(eq.name, size=(20, 1), pad=(5, 5)),
            sg.Text(f"{eq.bonuses.health or 0:.2f}", size=(8, 1), pad=(5, 5)),
            sg.Text(f"{eq.bonuses.shield or 0:.2f}", size=(8, 1), pad=(5, 5)),
            sg.Text(f"{eq.bonuses.armor or 0:.2f}", size=(8, 1), pad=(5, 5)),
            sg.Text(f"{eq.bonuses.energy or 0:.2f}", size=(8, 1), pad=(5, 5))
        ]
        rows.append(row)

    return [header] + rows
