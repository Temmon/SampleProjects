
import constants
import random

class Genome(object):
    def __init__(self):
        length = constants.GENOME_LENGTH - 1
        self.traits = []
        self.traits.append(Color(length))
        self.traits.append(Doom(length))
        
    def process(self, person):
        for trait in self.traits:
            trait.process(person)
            
class Doom(object):
    def __init__(self, size):
        self.locus = random.randint(0, size)
        
    def process(self, person):
        if person.genes[self.locus].dominant():
            person.doomed = True
        else:
            person.doomed = False


class Color(object):
    def __init__(self, size):
        self.red = random.randint(0, size)
        self.green = random.randint(0, size)
        self.blue = random.randint(0, size)
        
        self.geneType = "color"
        
    def process(self, person):
        person.hair = [person.genes[self.red].getColor(), 
                        person.genes[self.green].getColor(), 
                        person.genes[self.blue].getColor()]
