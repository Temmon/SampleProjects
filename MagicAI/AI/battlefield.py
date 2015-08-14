class Battlefield():
    spells = []
    
    def __init__(self):
        pass
        
    def untapAll(self, player):
        for card in self.spells:
            if card.owner == player:
                card.untap()
        
    def add(self, card):
        self.spells.append(card)

    def printBattlefield(self, player):
        print "Theirs"
        for i, spell in zip(xrange(len(self.spells)), self.spells):
            if spell.controller != player:
                print "%d\t%s"%(i, spell)
        print "Yours"
        for i, spell in zip(xrange(len(self.spells)), self.spells):
            if spell.controller == player:
                print "%d\t%s"%(i, spell)

    def attack(self, index, player):
        spell = self.spells[index]
        if spell.controller == player and hasattr(spell, "power"):
            spell.attacking = True
            return True
        else:
            return False
            
    def block(self, index, player):
        spell = self.spells[index]
        if spell.controller != player and hasattr(spell, "power"):
            spell.blocking = True
            return True
        else:
            return False

    def declareBlock(self, attackIndex, blockIndex):
        blocker = self.spells[blockIndex]
        attacker = self.spells[attackIndex]
        
        if hasattr(blocker, "power") and hasattr(attacker, "power"):
            if attacker.attacking and blocker.blocking:
                blocker.blocking = attacker
                return True
        return False
        
    def spellInBattlefield(self, spell):
        if spell in self.spells:
            return True
        return False
        
    def removeSpell(self, spell):
        if self.spellInBattlefield(spell):
            self.spells.remove(self.index(spell))

    def getCreatures(self):
        return [spell for spell in self.spells if hasattr(spell, "power")]

battlefield = Battlefield()
