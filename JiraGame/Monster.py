import random, Character

class Monster(Character.Character):
    def __init__(self):
        super(Monster, self).__init__()
        self.gold = 10
        
    def levelUp(self):
        super(Monster, self).levelUp()
        self.gold += 10

    def startingStrength(self):
        return 5
        
    def startingHP(self):
        return 10
        
    def attack(self):
        return random.randint(0, self.strength)