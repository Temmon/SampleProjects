from colors import *

class Spell:
    def __init__(self, name, manaCost):
        self.name = name
        self.manaCost = manaCost
        self.tapped = False
        self.controller = None
        self.owner = None
        self.abilities = []
        self.tempAbilities = []

    def getManaCost(self):
        return self.manaCost
        
    def getConvertedManaCost(self):
        return sum(self.manaCost)

    def printMana(self):
        ret = ""
        for i in xrange(len(self.manaCost)):
            if self.manaCost[i] > 0:
                if i == 0:
                    ret = ret + "%d"%self.manaCost[i]
                else:
                    s = spellMappings[i] * self.manaCost[i]
                    ret = ret + "%s"%s
        return ret

    def __str__(self):
        if self.manaCost == None:
            return self.name
        ret = "%s | %s"%(self.name, self.printMana())
        return ret

    def __eq__(self, other):
        if isinstance(other, Spell):
            if other.name == self.name:
                return True
        return False
        
    def tap(self):
        self.tapped = True
        
    def untap(self):
        self.untapped = False
        
    def isTapped(self):
        return self.tapped
    
    def isLand(self):
        return self.manaCost == None
        
def main():
    pass

if __name__ == "__main__":
    main()

