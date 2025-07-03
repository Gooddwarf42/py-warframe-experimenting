import json
from pathlib import Path
from typing import List

import PySimpleGUI as sg

from app.elements import render_stats, render_equipments
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
            sg.VSeparator(),
            sg.Column(render_equipments(equipments), scrollable=True, vertical_scroll_only=True, size=(600, 300)),
        ]
    ]
    window = sg.Window('Verns are best', layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        # React to checkbox toggles
        if isinstance(event, str) and event.startswith("-TOGGLE-EQUIP-"):
            try:
                index_of_equipment_to_toggle = int(event.split("-")[3])#boy this is ugly///
                equipments[index_of_equipment_to_toggle].is_equipped = values[event]
                print(f"{equipments[index_of_equipment_to_toggle].name} is_equipped = {equipments[index_of_equipment_to_toggle].is_equipped}")
            except (IndexError, ValueError):
                pass  # Just in case the key is malformed

    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_app()
