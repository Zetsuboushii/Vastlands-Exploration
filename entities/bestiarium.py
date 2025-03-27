from entities import Entity


class Bestiarium(Entity):
    def __init__(self, name: str, boss_title: str, type: str, hp: int, ac: int, movement: list[dict], abilities: dict,
                 weaknesses: list[str], resistances: list[str], immunities: list[str], actions: list[str]):
        self.name = name
        self.boss_title = boss_title
        self.type = type
        self.hp = hp
        self.ac = ac
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.immunities = immunities
        self.actions = actions

        # unpacking movement
        self.movement = {move["type"]: move["range"] for move in movement}

        # unpack abilities
        self.str = abilities.get("str", 0)
        self.dex = abilities.get("dex", 0)
        self.con = abilities.get("con", 0)
        self.int = abilities.get("int", 0)
        self.wis = abilities.get("wis", 0)
        self.cha = abilities.get("cha", 0)

    @staticmethod
    def from_json(data):
        return Bestiarium(
            name=data.get('name', ""),
            boss_title=data.get('boss_title', ""),
            type=data.get('type', ""),
            hp=data.get('hp', 0),
            ac=data.get('ac', 0),
            movement=data.get('movement', []),
            abilities=data.get('abilities', {}),
            weaknesses=data.get('weaknesses', []),
            resistances=data.get('resistances', []),
            immunities=data.get('immunities', []),
            actions=data.get('actions', []),
        )
