#from deck import Deck
import deck
from colors import *
from land import Land
from creature import Creature
import random

rootCards = []

ON_CAST = 0
TRIGGERED = 1
ENTER_BATTLEFIELD = 2
LEAVE_BATTLEFIELD = 3
STATE = 4
ACTIVATED = 4

def randomCard():
    return rootCards[random.randint(0, len(rootCards) - 1)]
    
def randDeck(rootCards):
    d = deck.Deck(RED)
    for i in xrange(60):
        isLand = random.randint(0, 2)
        if isLand == 0:
            d.add(rootCards[0].copy())
        else:
            hasFourOf = True
            while hasFourOf:
                chance = random.randint(1, len(rootCards) - 1)
                if not d.fourOf(rootCards[chance]):
                    d.add(rootCards[chance].copy())
                    hasFourOf = False
    return d

def setCards():
    global rootCards
    rootCards.append(Land("Mountain", RED))
    rootCards.append(Creature("Blood Ogre", [2, 1, 0, 0, 0, 0], 2, 2, "Ogre", "Warrior"))
    rootCards.append(Creature("Bonebreaker Giant", [4, 1, 0, 0, 0, 0], 4, 4, "Giant"))
    rootCards.append(Creature("Chandra's Phoenix", [1, 2, 0, 0, 0, 0], 2, 2, "Phoenix"))
    rootCards.append(Creature("Crimson Mage", [1, 1, 0, 0, 0, 0], 2, 1, "Human", "Shaman"))
    rootCards.append(Creature("Fiery Hellhound", [1, 2, 0, 0, 0, 0], 2, 2, "Elemental", "Hound"))
    rootCards.append(Creature("Flameblast Dragon", [4, 2, 0, 0, 0, 0], 5, 5, "Dragon"))
    rootCards.append(Creature("Furyborn Hellkite", [4, 3, 0, 0, 0, 0], 6, 6, "Dragon"))
    rootCards.append(Creature("Goblin Arsonist", [0, 1, 0, 0, 0, 0], 1, 1, "Goblin", "Shaman"))
    rootCards.append(Creature("Goblin Bangchuckers", [2, 2, 0, 0, 0, 0], 2, 2, "Goblin", "Warrior"))
    rootCards.append(Creature("Goblin Chieftain", [1, 2, 0, 0, 0, 0], 2, 2, "Goblin"))
    rootCards.append(Creature("Goblin Fireslinger", [0, 1, 0, 0, 0, 0], 1, 1, "Goblin", "Warrior"))
    rootCards.append(Creature("Goblin Piker", [1, 1, 0, 0, 0, 0], 2, 1, "Goblin", "Warrior"))
    rootCards.append(Creature("Goblin Tunneler", [1, 1, 0, 0, 0, 0], 1, 1, "Goblin", "Rogue"))
    rootCards.append(Creature("Gorehorn Minotaurs", [2, 2, 0, 0, 0, 0], 3, 3, "Minotaur", "Warrior"))
    rootCards.append(Creature("Grim Lavamancer", [0, 1, 0, 0, 0, 0], 1, 1, "Human", "Wizard"))
    rootCards.append(Creature("Inferno Titan", [4, 2, 0, 0, 0, 0], 6, 6, "Giant"))
    rootCards.append(Creature("Lightning Elemental", [3, 1, 0, 0, 0, 0], 4, 1, "Elemental"))
    rootCards.append(Creature("Manic Vandal", [2, 1, 0, 0, 0, 0], 2, 2, "Human", "Warrior"))
    rootCards.append(Creature("Stormblood Berserker", [1, 1, 0, 0, 0, 0], 1, 1, "Human", "Berserker"))
    rootCards.append(Creature("Volcanic Dragon", [4, 2, 0, 0, 0, 0], 4, 4, "Dragon"))
    rootCards.append(Creature("Wall of Torches", [1, 1, 0, 0, 0, 0], 4, 1, "Wall"))
