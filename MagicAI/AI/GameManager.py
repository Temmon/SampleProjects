
from deck import Deck
from player import Player
from utils import *
from battlefield import Battlefield
import AIBase

class GameManager():    
    def __init__(self, interactive):
        self.interactive = interactive
        self.selection = ""
        self.currPlayer = None
        self.otherPlayer = None
        setCards()
        self.p1 = Player(randDeck(rootCards))
        self.p2 = Player(randDeck(rootCards))
        self.p1.drawStartingHand()
        self.p2.drawStartingHand()
        self.p1.printHand()
        print ""
        self.p2.printHand()

        self.currPlayer = self.p1
        self.otherPlayer = self.p2
        
    def waitForInput(self, prompt):
        selection = ""
        selection = raw_input(prompt + " ")
        if selection == "q":
            exit()
        if selection == "h":
            self.currPlayer.printHand()
        elif selection == "b":
            self.currPlayer.printBattlefield()
        elif selection == "g":
            self.currPlayer.printGraveyard()
        elif selection == "o":
            self.otherPlayer.printBattlefield()
        return selection

    def untap(self):
        self.waitForInput("Untap")
        self.currPlayer.untapAll()
        
    def upkeep(self):
        self.waitForInput("Upkeep")
        
    def draw(self):
        self.waitForInput("Draw")
        self.currPlayer.draw()

    def main(self, isFirst):
        toPrint = "2"
        if isFirst:
            toPrint = "1"
        selection = self.waitForInput("Main %s"%toPrint)
        
        self.currPlayer.mainPhase(isFirst)
        while selection != "":
            if selection.isdigit():
                self.currPlayer.cast(int(selection))
            selection = self.waitForInput("Main %s"%toPrint)
            

    def beginningCombat(self):
        self.waitForInput("Begin combat")
        
    def declareAttackers(self):
        #attackers = self.currPlayer.declareAttackers()
        selection = self.waitForInput("Declare attackers")
        while selection != "":
            if selection.isdigit():
                attacking = self.currPlayer.attack(int(selection))
            selection = self.waitForInput("Declare attackers")
        
        return attackers
        
    def declareBlockers(self, attackers):
        defender = self.waitForInput("Declare blockers")
        while defender != "":
            if defender.isdigit():
                if not self.currPlayer.block(int(defender)):
                    defender = self.waitForInput("Declare blockers")
                    continue
            selection = self.waitForInput("Declare creature to defend against: %s"%attackers)
            while not selection.isdigit():
                selection = self.waitForInput("Declare creature to defend against: %s"%attackers)
            print "selection: %s. Defender: %s"%(selection, defender)
            self.currPlayer.declareBlock(int(selection), int(defender))
            defender = self.waitForInput("Declare blockers")
        return False
        
    def combatDamage(self, attackers, defenders):
        self.waitForInput("combatDamage")
        for attacker in attackers:
            self.otherPlayer.dealDamage(attacker.getPower())
        
    def endCombat(self):
        self.waitForInput("endCombat")
        
    def combat(self):
        self.beginningCombat()
        attackers = self.declareAttackers()
        if attackers:
            defenders = self.declareBlockers(attackers)
            self.combatDamage(attackers, defenders)
            self.endCombat()
        
    def end(self):
        self.waitForInput("End phase")
        
    def cleanup(self):
        pass

    def runGame(self):            
        while True:
            self.untap()
            self.upkeep()
            self.draw()
            self.main(True)
            self.combat()
            self.main(False)
            self.end()
            self.cleanup()
            temp = self.currPlayer
            self.currPlayer = self.otherPlayer
            self.otherPlayer = temp
    
if __name__ == "__main__":
    interactive = True
    g = GameManager(True)
    g.runGame()
