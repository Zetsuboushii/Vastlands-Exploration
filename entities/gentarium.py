from entities import Entity


class Gentarium(Entity):
    def __init__(self, name: str, ageavg: int, domains: list[str]):
        self.name = name
        self.ageavg = ageavg
        self.domains = domains

    @staticmethod
    def from_json(data):
        return Gentarium(
            name=data.get('name', ''),
            ageavg=data.get('age_average', 0),
            domains=data.get('domains', [])
        )
