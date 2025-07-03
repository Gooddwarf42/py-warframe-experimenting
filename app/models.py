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