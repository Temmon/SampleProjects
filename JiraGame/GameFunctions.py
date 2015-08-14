import threading
from Hero import Hero
from Monster import Monster
from jira.client import JIRA

class GameFunctions(object):
    def __init__(self, singleConnect):
        self.singleConnect = singleConnect
        self.connect()
        self.heroes = {}
        
    def connect(self, patched = False):
        if patched:
        #Patched is for deprecated requests API
            self.jira = patchedJira.connectToJira()
        else:
            options = {'server': 'https://jira.secondlife.com'}
            self.jira = JIRA(options)
        
    def runGame(self):
        self.connectAndLevelUp()
        [self.fight(self.heroes[name], Monster()) for name in self.heroes]
        
        if not self.singleConnect:
            self.gameTimer = threading.Timer(60 * 6, self.runGame)
            self.gameTimer.start()
        
    def fightByUser(self, user1, user2):
        ret = ""
        notPlayTempl = "Hero %s does not exist"
        if user1 not in self.heroes:
            ret += notPlayTempl%user1
        if user2 not in self.heroes:
            ret += notPlayTempl%user2
        if ret != "":
            return ret
            
        ret = self.fight(self.heroes[user1], self.heroes[user2])
        
        ret += "%s\n%s"%(self.getCharacterHTML(user1), self.getCharacterHTML(user2))
        
        return ret
        
    def getCharacterHTML(self, user):
        return self.heroes[user].html() if user in self.heroes else None
        
    def getAllHTML(self):
        ret = ""
        for name in self.heroes:
            ret = "%s <p>%s</p>"%(ret, self.heroes[name].html())
        return ret
        
    def fight(self, char1, char2):
        ret = ""
        if char1.isDead() or char2.isDead():
            return "A hero is knocked out and can't fight"
        
        while not char1.isDead() and not char2.isDead():
            char2.takeDamage(char1.attack())
            char1.takeDamage(char2.attack())
        
        if char1.isDead() and char2.isDead():
            #Can't loot if they're both KO
            return "Both players knocked each other out"
        
        if char2.isDead():
            ret = ret + self.manageWinner(char1, char2)
        elif char1.isDead():
            ret = ret + self.manageWinner(char2, char1)
        
        return ret
        
    def manageWinner(self, victor, loser):
        ret = ""
        if hasattr(victor, 'name'):
            ret += "%s won! "%victor.name
        if hasattr(loser, 'name'):
            ret += "%s lost. :( "%loser.name
            
        #TODO: Can go fractional
        victor.gold += loser.gold / 2
        loser.gold /= 2
        return ret
                
    def connectAndLevelUp(self):
    #TODO: Figure out how to actually get back the number of issues that match a filter
    #The API claims it's possible
        issues = self.jira.search_issues('project = OPEN AND issuetype = "New Feature"', maxResults = 500)
        for issue in issues:
            if issue.fields.assignee != None:
                name = issue.fields.assignee.name
                #TODO: Defaultdict of some sort?
                if name not in self.heroes:
                    h = Hero(name)
                    self.heroes[name] = h
                hero = self.heroes[name]
                self.processIssue(hero, issue)
                    
    def processIssue(self, hero, issue):
        status = issue.fields.status.name.lower()
        xpGains = {"closed": 20, "resolved": 15, "in progress": 5}
        if status in xpGains:
            hero.gainXP(xpGains[status])
        
    def shutdown(self):
        if hasattr(self, "gameTimer"):
            self.gameTimer.cancel()
        
            
            