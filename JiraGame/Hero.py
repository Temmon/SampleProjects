import random, Character

class Hero(Character.Character):
    def __init__(self, name):
        super(Hero, self).__init__()
        self.name = name
        
    def startingStrength(self):
        return 10
        
    def startingHP(self):
        return 200
        
    def attack(self):
        missChance = random.randint(0, 10)
        if missChance == 0:
            return 0
        return random.randint(self.strength / 2, self.strength)
        
    def html(self):
        return "<h3>%s</h3>%s"%(self.name, super(Hero, self).html())
        
    def __str(self):
        return "%s\n%s"%(self.name, super(Hero, self).__str__())
    