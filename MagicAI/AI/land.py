from spell import Spell

class Land(Spell):

    def __init__(self, name, color):
        Spell.__init__(self, name, None)
        self.color = color

    def copy(self):
        return Land(self.name, self.color)

    
