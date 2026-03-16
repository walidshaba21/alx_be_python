import random
TRAP_ARTISTS = [
    'Rick Ross',
    'Future',
    'Desiigner',
    'Young Jeezy'
]

class TrapArtist:
    _hits = [
        'Dead presidents', 
        'Panda',
        'Money',
    ]

    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name not in TRAP_ARTISTS:
            raise ValueError(f"{name} is not a trap artist" )
        self._name = name

    @staticmethod
    def random_artist():
        return TrapArtist(random.choice(TRAP_ARTISTS))


    @classmethod
    def hits(cls):
        return cls._hits
    
