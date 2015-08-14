from deck import Deck
from colors import *
from land import Land
from creature import Creature
import random
from utils import *

"""
1. Initialize population
2. Calculate fitness
3. Create breeding pool
4. Crossover
5. Mutate
6. Repeat from 2 until bored?
"""

#calc fitness: colored mana counts for two, colorless counts for 1. Go
#divide sum of mana by # lands

#crossover

pop = []
nextGen = []

def initPop(rootCards):
    global pop

    for j in xrange(64):
        d = randDeck(rootCards)
        pop.append(d)

def setFitness():
    global pop
    
    for deck in pop:
        deck.getFitness()
        
def saveBestDecks(parents):
    global nextGen
    
    for i in xrange(LAST):
        for deck in parents:
            if deck.colors == i:
                nextGen.append(deck)
                break
    return parents
        
def chooseParents():
    global pop, nextGen
    
    parents = []
    nextGen = []
    
    pop.sort()
    pop.reverse()
        
    total = sum([deck.fitness for deck in pop])
    #temp = [total / deck.fitness for deck in pop]
    temp = [deck.fitness for deck in pop]
    total = sum(temp) * 1.0
    percents = [val / total for val in temp]
    for i in xrange(1, len(percents)):
        percents[i] = percents[i] + percents[i - 1]
        
    for i in pop:
        rand = random.random()
        for j in xrange(len(percents)):
            if rand < percents[j]:
                parents.append(pop[j])
                break
                
    parents.sort()
    parents.reverse()
    
    parents = saveBestDecks(parents)
    return parents
    
def crossover(parents):
    global nextGen
    
    while len(nextGen) < len(parents):
        p1 = parents[random.randint(0, len(parents) - 1)]
        p2 = parents[random.randint(0, len(parents) - 1)]
        
        c1, c2 = p1.cross(p2)
        nextGen.append(c1)
        if len(nextGen) < len(parents):
            nextGen.append(c2)
    #print nextGen
        
def mutate():
    global nextGen
    
    for deck in nextGen:
        for i in xrange(len(deck.cards)):
            if random.random() < .0005:
                card = deck.randomCard()
                card = deck.randomCard()
                deck.cards[i] = card

def runGA():
    global pop
    
    setCards()
    
    initPop(rootCards)
    setFitness()
    
    print [deck.fitness for deck in pop]
    
    parents = chooseParents()
    
    crossover(parents)
    mutate()
    
    
    pop = nextGen

if __name__ == "__main__":
    runGA()
