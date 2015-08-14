import bottle
import GameFunctions, argparse

parser = argparse.ArgumentParser(description='Run the JIRA game')
parser.add_argument('--verbose', '-v', action='store_true', help="Start server in verbose mode")
parser.add_argument('--server', '-s', default="127.0.0.1", help="Address to serve on")
parser.add_argument('--port', '-p', default=9200, help="Port to serve on")
parser.add_argument('--single', action="store_false", help="Only connect to JIRA server once at game start")

class GameServer(bottle.Bottle):
    def __init__(self, *args, **kwargs):
        singleConnect = kwargs["singleConnect"]
        del kwargs["singleConnect"]
        super(GameServer, self).__init__(*args, **kwargs)
        self.game = GameFunctions.GameFunctions(singleConnect)
        self.game.runGame()
        
        self.route('/show/:user', callback=self.showCharacter, method="GET")
        self.route('/show', callback=self.showAll, method="GET")
        self.route('/fight/:user1/:user2', callback=self.fight, method="GET")
        
    def showCharacter(self, user):
        desc = self.game.getCharacterHTML(user)
        if desc == None:
            return "Hero %s could not be found"%user
        return desc
    
    def showAll(self):
        desc = self.game.getAllHTML()
        if desc == None:
            return "There are no characters currently playing"
        return  desc
        
    def fight(self, user1, user2):
        return self.game.fightByUser(user1, user2)
        
    def shutdown(self):
        #Stub for when persistence is implemented to save off characters at the shutdown hook
        pass
        
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.game.shutdown()
        self.shutdown()
        
def main():
    opts = parser.parse_args()
    
    if opts.verbose:
        bottle.debug(True)
    with GameServer(singleConnect = opts.single) as app:
        bottle.run(app, host = opts.server, port = opts.port, reloader=True, server = bottle.CherryPyServer)
        
if __name__ == "__main__":
    main()