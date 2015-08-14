from spell import Spell
from creature import Creature
from land import Land
from colors import *
import copy, random
from utils import *

class Deck():

    def __init__(self, colors):
        self.cards = []
        self.colors = colors
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def printDeck(self, ):
        for card in self.cards:
            print card

    def add(self, card):
        self.cards.append(card)

    def fourOf(self, card):
        if self.cards.count(card) > 4:
            return True
        return False

    def countLands(self):
        return len([card for card in self.cards if card.manaCost == None])
       
    def scoreMana(self):
        ret = 0
        for card in self.cards:
            if card.manaCost != None:
                ret = ret + card.manaCost[0] * 2
                for color in card.manaCost[1:]:
                    ret = ret + color
        return ret
        
       
    def getFitness(self):
        landCount = self.countLands()
        if landCount == 0:
            return 0
        val = self.scoreMana() / landCount
        self.fitness = val
        return val
        
    #if it has a color element, it's a land?
    def randomCard(self):
        card = randomCard()
        if card.manaCost == None:
            return card
        while not self.fourOf(card):
            card = randomCard()
            if card.manaCost == None:
                return card
        return card
        
    def cross(self, deck2):
        c1 = Deck(self.colors)
        c2 = Deck(self.colors)
        
        tempSelf = copy.deepcopy(self.cards)
        tempOther = copy.deepcopy(deck2.cards)
        
        for j, card in zip(xrange(len(self.cards)), self.cards):
            for i in xrange(len(tempOther)):
                if card == tempOther[i]:
                    c1.add(card)
                    c2.add(card)
                    tempOther[i] = None
                    tempSelf[j] = None
                    break

        tempOther = [card for card in tempOther if card != None]
        tempSelf = [card for card in tempSelf if card != None]
        
        for i in xrange(len(tempOther)):
            #print "%d %d"%(len(c1.cards), len(c2.cards))
            card1 = tempSelf[i]
            card2 = tempOther[i]
            if random.random() < .5:
                card1 = tempOther[i]
                card2 = tempSelf[i]
                
            deck1Added = False
            deck2Added = False
            
            if not c1.fourOf(card1) and not c2.fourOf(card2):
                c1.add(card1)
                c2.add(card2)
            elif not c1.fourOf(card2) and not c2.fourOf(card1):
                c1.add(card2)
                c2.add(card1)
            else:
                if not c1.fourOf(card1):
                    c1.add(card1)
                    c2.add(c2.randomCard())
                elif not c1.fourOf(card2):
                    c1.add(card2)
                    c2.add(c2.randomCard())
                elif not c2.fourOf(card1):
                    c2.add(card1)
                    c1.add(c1.randomCard())
                elif not c2.fourOf(card2):
                    c2.add(card2)
                    c1.add(c1.randomCard())
                else:
                    c1.add(c1.randomCard())
                    c2.add(c2.randomCard())
                    
        #print "%d %d"%(len(c1.cards), len(c2.cards))
        return (c1, c2)
        
    def __lt__(self, other):
        if not isinstance(other, Deck):
            return False
            
        if self.fitness < other.fitness:
            return True
        return False
        
    def __gt__(self, other):
        if not isinstance(other, Deck):
            return False
            
        if self.fitness < other.fitness:
            return True
        return False
        

def main():
    pass

    
if __name__ == "__main__":
    main()
