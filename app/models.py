from dataclasses import dataclass
from typing import Optional

import constants.base_stats as BASE_STATS

@dataclass
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

@dataclass
class Modifiers:
    health: Optional[float] = None
    shield: Optional[float] = None
    armor: Optional[float] = None
    energy: Optional[float] = None

@dataclass
class Equipment:
    name:str
    bonuses: Modifiers
    is_equipped: bool = False
