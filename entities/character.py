from entities import Entity


# todo check if it dicts should be converted to tuple for easier analysis as it now look like this in the df column [{'place': 'Tempel der Zeit', 'attachment': 'Hauptsitz'}]
class Character(Entity):
    def __init__(self, name: str, surname: str, title: str, race: str, sex: str, birthday: str,
                 aliases: list[dict],
                 measurements: dict,
                 functions: list[str],
                 classes: dict,
                 nationality: str,
                 homes: list[dict],
                 alignment: str,
                 affiliations: list[str],
                 likes: list[str],
                 dislikes: list[str],
                 status: str,
                 relationships: list[dict],
                 alt_images: list[str],
                 content: dict):
        self.name = name
        self.surname = surname
        self.title = title
        self.race = race
        self.sex = sex
        self.birthday = birthday
        self.aliases = aliases

        # Unpack measurements
        self.height = measurements.get('height', 0)
        self.weight = measurements.get('weight', 0)
        self.bust = measurements.get('bust', 0)
        self.underbust = measurements.get('underbust', 0)
        self.waist = measurements.get('waist', 0)
        self.hip = measurements.get('hip', 0)
        self.shoulder_width = measurements.get('shoulder_width', 0)
        self.muscle_mass = measurements.get('muscle_mass', 0)

        self.functions = functions

        # Unpack class details
        self.baseclass = classes.get('baseclass', '')
        self.subclasses = classes.get('subclasses', [])
        self.masterclass = classes.get('masterclass', '')
        self.nationality = nationality
        self.homes = homes
        self.alignment = alignment
        self.affiliations = affiliations
        self.likes = likes
        self.dislikes = dislikes
        self.status = status
        self.relationships = relationships
        self.alt_images = alt_images
        self.content = content

    @staticmethod
    def from_json(data):
        return Character(
            name=data.get('name', ''),
            surname=data.get('surname', ''),
            title=data.get('title', ''),
            race=data.get('race', ''),
            sex=data.get('sex', ''),
            birthday=data.get('birthday', ''),
            aliases=data.get('aliases', []),
            measurements=data.get('measurements', {}),
            functions=data.get('functions', []),
            classes=data.get('classes', {}),
            nationality=data.get('nationality', ''),
            homes=data.get('homes', []),
            alignment=data.get('alignment', ''),
            affiliations=data.get('affiliations', []),
            likes=data.get('likes', []),
            dislikes=data.get('dislikes', []),
            status=data.get('status', ''),
            relationships=data.get('relationships', []),
            alt_images=data.get('alt_images', []),
            content=data.get('content', {})
        )