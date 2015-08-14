import string
import sys
import os
import random

punc = tuple([p for p in string.punctuation]) + ("\n",)

class Word(object):
    def __init__(self, word):
        self.raw = word + " "
        
        self.stripped = self.raw.translate(string.maketrans("",""), string.punctuation).lower().strip().replace(chr(10), "")
        
        trans = ''.join('_' if chr(c).isupper() or chr(c).islower() else chr(c) for c in range(256))
        self.found = self.raw.translate(trans)
        self.correct = False
        self.guessed = False
        
    def __repr__(self):
        return self.found

    def __str__(self):
        return self.stripped
        
    def test(self, guess):
        if self.stripped == guess:
            self.correct = True
            self.guessed = True
            self.found = self.raw
        elif len(self.stripped) > 2 and self.levenshteinDistance(self.stripped, guess) == 1:
            self.found = self.raw
            self.correct = True
            
    def show(self):
        self.found = self.raw
        self.correct = True
        
    def levenshteinDistance(self, s1,s2):
        if len(s1) > len(s2):
            s1,s2 = s2,s1
        distances = range(len(s1) + 1)
        for index2,char2 in enumerate(s2):
            newDistances = [index2+1]
            for index1,char1 in enumerate(s1):
                if char1 == char2:
                    newDistances.append(distances[index1])
                else:
                    newDistances.append(1 + min((distances[index1],
                                                 distances[index1+1],
                                                 newDistances[-1])))
            distances = newDistances
        return distances[-1]
            
class Line(object):
    def __init__(self, line):
        self.words = [Word(word) for word in line.split(" ")]
        
    def test(self, guess):
        for word in self.words:
            word.test(guess)
            
    def printLine(self):
        return ''.join([word.found for word in self.words]).strip()
        
    def show(self):
        for word in self.words:
            word.show()
        
def printLyrics(lyrics):
    print '\n'.join([line.printLine() for line in lyrics])

def loadLyrics():
    songs = os.listdir("lyrics")
    choice = random.choice(songs)
    print choice
    
    with open(os.path.join("lyrics", choice)) as f:
        lines = f.readlines()
    return [Line(line) for line in lines]

def guessWord(guess, lyrics):
    for line in lyrics:
        line.test(guess)
        
def showSong(lyrics):
    for line in lyrics:
        line.show()

def gameLoop():
    lyrics = loadLyrics()

    while True:
        printLyrics(lyrics)
        
        print ""
        command = raw_input("Command: ").lower().strip()
        if command == "exit_game":
            sys.exit(0)
        elif command == '\x04':
            sys.exit(0)
        elif command == "exit()":
            sys.exit(0)
        elif command == "new()":
            lyrics = loadLyrics()
        elif command == "show()":
            showSong(lyrics)
        else:
            print ""
            guessWord(command, lyrics)


def main():
    gameLoop()

if __name__ == "__main__":
    main()

