
from gene import Gene
import constants
import random
import uuid

class Person(object):
    def __init__(self, genome, genes=False):
        self.id = str(uuid.uuid4())
        self.dead = False
        if genes:
            self.genes = genes
            self.age = 0
        else:
            self.genes = [Gene() for i in xrange(constants.GENOME_LENGTH)]
            self.age = random.randint(0, 80 * 365)
            
        self.calories = 2000
        self.status = constants.ALIVE
            
        if random.random() < .5:
            self.sex = constants.MALE
        else:
            self.sex = constants.FEMALE
            
        self.genome = genome
        self.genome.process(self)
        
        self.relations = []
        for i in xrange(5):
            self.relations.append([])
        
    def __eq__(self, other):
        if isinstance(self, other):
            return self.id == other.id
        else:
            return False
            
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def getAge(self):
        return round(self.age / 365)
        
    def isMature(self):
        return self.getAge() >= 16
        
    def burnCalories(self):
        self.calories -= 1200
        
    def forage(self):
        self.calories += random.randint(500, 2000)
        
    def die(self, cause):
        self.dead = True
        self.status = cause
        
    def addRelationship(self, other, degree):
        self.relations[degree].append(other)
        
    def reproduce(self, other):
        if self == other:
            return
            
        childGenes = [Gene(myGene.choose(), otherGene.choose())
                        for myGene, otherGene 
                        in zip(self.genes, other.genes)]
            
        return Person(self, self.genome, childGenes) 

    def step(self):
        self.forage()
        self.burnCalories()
        self.age += 1
        
        if self.calories <= 0 and random.random() < .1:
            self.die(constants.DEATH_HUNGER)
        
        if self.doomed:
            if random.random() < (self.age / 5000000.0):
                self.die(constants.DEATH_DOOM)
                
                
                
                
