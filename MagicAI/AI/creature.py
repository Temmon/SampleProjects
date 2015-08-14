from spell import Spell

class Creature(Spell):

    def __init__(self, name, manaCost, power, tough, ctype, subtype=""):
        Spell.__init__(self, name, manaCost)
        self.power = power
        self.tough = tough
        self.ctype = ctype
        self.subtype = subtype
        self.summoningSickness = True
        self.attacking = False
        self.blocking = False

    def copy(self):
        return Creature(self.name, self.manaCost, self.power,
                        self.tough, self.ctype, self.subtype)

    def __str__(self):
        ret = Spell.__str__(self)
        sub = ""
        if self.subtype != "":
            sub = " " + self.subtype
        ret = ret + " | Creature - %s%s | %d/%d"%(self.ctype, sub, self.power, self.tough)
        return ret

    def getPower(self):
        return self.power
        
