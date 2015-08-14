import copy
import random
from battlefield import battlefield

class Player():
    
    def __init__(self, deck):
        self.deck = deck
        self.library = copy.copy(self.deck.cards)
        for card in self.library:
            card.owner = self
            card.controller = self
        self.graveyard = []
        self.exile = []
        self.hand = []
        self.life = 20
        self.landPlayed = False
        self.lands = []
        self.manaPool = [0, 0, 0, 0, 0, 0]
                
    def cast(self, index):
        if self.canPlayCard(index):
            self.playCardFromHand(index)
    
    def canPlayCard(self, index):
        #card = self.hand[index]
        #opts = self.hasLandFor(card)
        return True
        
    def playCardFromHand(self, index):
        #enter the battlefield effects occur
        card = self.hand.pop(index)
        battlefield.add(card)
        
    def shuffleLibrary(self):
        random.shuffle(self.library)

    def draw(self):
        card = self.library.pop()
        self.hand.append(card)
        
    def drawStartingHand(self):
        for i in xrange(7):
            self.draw()
            
    def printHand(self):
        for i, card in zip(xrange(len(self.hand)), self.hand):
            print "%d\t%s"%(i, str(card))
        if len(self.hand) == 0:
            print "No cards in hand"
    
    def printBattlefield(self):
        print "Life: %d"%self.life
        battlefield.printBattlefield(self)
            
    def printGraveyard(self):
        for i, card in zip(xrange(len(self.graveyard)), self.graveyard):
            print "%d\t%s"%(i, str(card))
            
        if len(self.graveyard) == 0:
            print "No cards in graveyard"
            
    def untapAll(self):
        battlefield.untapAll(self)
        
    def addMana(self, color, count = 1):
        self.manapool[color] += count
        
    def declareAttackers(self):
        return [card for card in battlefield.getCreatures() if card.controller == self]
        
    def attack(self, index):
        return battlefield.attack(index, self)
        
    def block(self, index):
        return battlefield.block(index, self)
        
    def declareBlock(self, attackIndex, blockIndex):
        return battlefield.declareBlock(attackIndex, blockIndex)
        
    def battleFieldToGraveyard(self, spell):
        if self.fromBattlefield(spell):
            toGraveyard(spell)
            
    def toGraveyard(self, spell):
        self.graveyard.append(spell)
        
    def toExile(self, spell):
        self.exile.append(spell)
            
    def fromBattlefield(self, spell):
        if battlefield.spellInBattlefield(spell):
            battlefield.removeSpell(spell)
            return True
        return False
    
    def fromGraveyard(self, spell):
        if spell in self.graveyard:
            self.graveyard.remove(self.graveyard.index(spell))
            return True
        return False
        
    def fromExile(self, spell):
        if spell in self.exile:
            self.exile.remove(self.exile.index(spell))
            return True
        return False
        
    def dealDamage(self, amt):
        self.life = self.life - amt

    def mainPhase(self, isFirst):
        pass
