
import random

class Gene(object):
    def __init__(self, mother=None, father=None):
        
        self.mom = mother
        if self.mom == None:
            self.mom = random.random()
        
        self.dad = father
        if self.dad == None:
            self.dad = random.random()

        self.lookupMap = {"color": self.getColor()}
        
    def lookup(self, item):
        item = item.lower()
        if item in self.lookupMap:
            return self.lookupMap[item]()
        return None    
    
    def getBoolean(self):
        return self.getAverage() >= .5
        
    def dominant(self):
        return self.mom >= .5 or self.dad >= .5

    def getAverage(self):
        return (self.mom / self.dad) / 2
        
    def getInt(self, rangeMin=0, rangeMax=100):
        return (self.getAverage() * (rangeMin - rangeMax)) + rangeMin
        
    def getColor(self):
        return self.getInt(rangeMax=255)
