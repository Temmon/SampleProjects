from person import Person
from genome import Genome
import constants
import random
import sys
import time

class World(object):
    def __init__(self):
        self.genome = Genome()
        self.people = [Person(self.genome) for i in xrange(constants.STARTING_POPULATION)]
        self.exitCommand = {"q": self.exit, "quit": self.exit}
        self.lookups = self.makeLookup({"s": self.step, "step": self.step, "r": self.fastTime, "run": self.fastTime, "h": self.showHelp, "help": self.showHelp})
        self.dead = []
                        
        self.stop = "STOP"
        self.year = 1
        self.day = 1
        
        self.pause = True
        
    def run(self):
        self.prompt(self.lookups)
        
    def fastTime(self):
        print "Running for a year"
        self.pause = False
        self.printInfo()
        while not self.pause:
            self.step(False)
            #time.sleep(.1)
        
        self.printInfo()
            
            
    def prompt(self, commands):
        while True:
            command = raw_input("What do you do? (h for help) ").lower()
            if command in commands:
                ret = commands[command]()
                if ret == self.stop:
                    return
            
    def exit(self):
        sys.exit(0)
        
    def makeLookup(self, newDict):
        return dict(newDict.items() + self.exitCommand.items())
        
    def step(self, shouldPrint=True):
        #examines = makeLookup({})
        for person in self.people:
            person.step()
        
        self.dead = self.dead + [person for person in self.people if person.dead]
        self.people = [person for person in self.people if not person.dead]
        
        self.day += 1
        
        if shouldPrint:
            self.printInfo()
            
        if self.day == 366:
            self.day = 1
            self.year += 1
            self.pause = True
            
    def printInfo(self):
        print "Year %d. Day %d."%(self.year, self.day)
        print "%s people still alive"%len(self.people)        
        
        doomedPeople = [person for person in self.people if person.doomed]
        print "%d people are doomed"%len(doomedPeople)
        
        hungerDead = [person for person in self.dead if person.status == constants.DEATH_HUNGER]
        doomDead = [person for person in self.dead if person.status == constants.DEATH_DOOM]
        
        print "%d people died from hunger"%len(hungerDead)
        print "%d people died from doom"%len(doomDead)
        
    def showHelp(self):
        print "(S)tep to step forward one tick"
        print "(R)un to run for a year"
        

def main(debug):
    if debug:
        random.seed(5)

    World().run()
    

if __name__ == "__main__":
    main(False)
