import json
from pathlib import Path
from typing import List

import PySimpleGUI as sg

from app.elements import render_stats
from app.models import Stats, Equipment, Modifiers


def load_equipments(filename: str) -> List[Equipment]:
    path = Path(filename)
    with open(path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    equipments = []
    for item in raw_data:
        bonuses = Modifiers(**item.get('bonuses', {}))
        equipments.append(Equipment(name=item['name'], bonuses=bonuses))

    return equipments

def run_app():
    equipments: list[Equipment] = load_equipments('./data/equipment.json')
    base_stats: Stats = Stats()
    modified_stats: Stats = Stats()
    modified_stats.energy += 41
    layout = [
        [
            sg.Column(render_stats(base_stats, 'Base statistics')),
            sg.Column(render_stats(modified_stats, 'Modified statistics')),
            sg.VSeparator()
        ]
    ]
    window = sg.Window('Verns are best', layout, size=(800, 600))
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_app()
