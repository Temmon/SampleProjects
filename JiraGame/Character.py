import random

"""Abstract class used for representing a generic character type"""
class Character(object):

    def __init__(self):
        self.strength = self.startingStrength()
        self.maxHP = self.startingHP()
        self.currentHP = self.maxHP
        self.xp = 0
        self.level = 1
        self.gold = 0
        
    def levelUp(self):
        self.xp = self.xpToNextLevel() * -1
        self.level += 1
        self.maxHP += 20
        self.currentHP = self.maxHP
        self.strength += 3
        
    def xpToNextLevel(self):
        nextLevel = self.level * 100
        return nextLevel - self.xp
        
    def gainXP(self, xp):
        self.xp += xp
        if self.xpToNextLevel <= 0:
            self.levelUp()
            
    def isDead(self):
        return self.currentHP <= 0
    
    def attack(self):
        raise NotImplementedError
        
    def startingStrength(self):
        raise NotImplementedError
        
    def startingHP(self):
        raise NotImplementedError
        
    def takeDamage(self, damage):
        self.currentHP -= damage
        
    def html(self):
        return "<p>Max HP: %s</p><p>Current HP: %s</p>" \
                "<p>Strength: %s</p><p>XP: %s</p>" \
                "<p>Level: %s</p>"%(self.maxHP, self.currentHP,
                self.strength, self.xp, self.level)
        
    def __str__(self):
        return "Max HP: %s\nCurrent HP: %s\n" \
                "Strength: %s\nXP: %s\n" \
                "Level: %s"%(self.maxHP, self.currentHP,
                self.strength, self.xp, self.level)
                