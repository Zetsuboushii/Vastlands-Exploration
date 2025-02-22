from entities import Entity


class Character(Entity):
    def __init__(self, name: str, surname: str, title: str, race: str, sex: str, birthday: str,
                 height: float, weight: int, bust: int, underbust: int, waist: int, hip: int, shoulder_width: int,
                 muscle_mass: int,
                 functions: list[str], character_class: str, subclasses: list[str],
                 masterclass: str, homes: list[str],
                 alignment: str, likes: list[str], dislikes: [str], status: str, relationships: list[tuple[str, str]],
                 lover: str):
        self.name = name
        self.surname = surname
        self.title = title
        self.race = race
        self.sex = sex
        self.birthday = birthday
        self.height = height
        self.weight = weight
        self.bust = bust
        self.underbust = underbust
        self.waist = waist
        self.hip = hip
        self.shoulder_width = shoulder_width
        self.muscle_mass = muscle_mass
        self.function = functions
        self.character_class = character_class
        self.subclasses = subclasses
        self.masterclass = masterclass
        self.homes = homes
        self.alignment = alignment
        self.likes = likes
        self.dislikes = dislikes
        self.status = status
        self.relationships = relationships
        self.lover = lover

    @staticmethod
    def from_json(data):
        return Character(
            name=data.get('name', ''),
            surname=data.get('surname', ''),
            title=data.get('title', ''),
            race=data.get('race', ''),
            sex=data.get('sex', ''),
            birthday=data.get('birthday', ''),
            height=data.get('height', 0),
            weight=data.get('weight', 0),
            bust=data.get('bust', 0),
            underbust=data.get('underbust', 0),
            waist=data.get('waist', 0),
            hip=data.get('hip', 0),
            shoulder_width=data.get('shoulder_width', 0),
            muscle_mass=data.get('muscle_mass', 0),
            functions=data.get('functions', []),
            character_class=data.get('class', ''),
            subclasses=data.get('subclasses', []),
            masterclass=data.get('masterclass', ''),
            homes=data.get('homes', []),
            alignment=data.get('alignment', ''),
            likes=data.get('likes', []),
            dislikes=data.get('dislikes', []),
            status="am Leben" if data.get('status', None) == "true" else "tot" if data.get('status',
                                                                                           None) == "false" else data.get(
                'status', None),
            relationships=data.get('relationships', []),
            lover=data.get('lover', '')
        )
