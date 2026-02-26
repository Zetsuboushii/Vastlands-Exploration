from entities import Entity


class WeaponAbility(Entity):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @staticmethod
    def from_json(data):
        return WeaponAbility(
            name=data.get("name", ""),
            description=data.get("desc", ""),
        )
