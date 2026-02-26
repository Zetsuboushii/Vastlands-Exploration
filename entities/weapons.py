from entities import Entity


class Weapon(Entity):
    def __init__(self, name: str, type: str, prerequisites: list[tuple[int, str]], range: int, range_far: int,
                 damage: list[tuple[str, str]], abilities: list[str]
                 ):
        self.name = name
        self.weapon_type = type
        self.prerequisites = prerequisites  # e.g. [(15, "Str"), (13, "Dex")]
        self.range_ = range  # short range
        self.range_far = range_far  # long range
        self.damage = damage  # e.g. [("1d4", "piercing"), ("1d8", "psychic")]
        self.abilities = abilities

    @staticmethod
    def from_json(data):
        return Weapon(
            name=data.get("name", ""),
            type=data.get("type", ""),
            prerequisites=data.get("prerequisites", []),
            range=data.get("range", 0),
            range_far=data.get("range_far", 0),
            damage=data.get("damage", []),
            abilities=data.get("abilities", [])
        )
