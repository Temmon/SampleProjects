Just run this with python lyrics.py. This is based off a puzzle I played a bit online and wished there were more examples of. It takes some corpus of text--I used song lyrics, hence the title and terminology--replaces all alphabetic characters with underscores and then makes for a bit of a game where you try to guess the precise lyrics of the song. It grabs up all files in the lyrics folder as possible corpuses. Obviously, this means that a non-text file can and probably would crash it. This also makes use of Levenstein distance so that you don't have to guess a word perfectly correctly in order to match (handy for typos, or just being unsure). But it only accepts matches where the edit distance is 1 or less, to keep it from being too easy. It's punctuation insensitive.

Since the command line I came up with interprets all literal strings as guesses, the commands for controlling the program are:

"exit()" (also "exit_game", or ctrl+d) to quit
"new()" to load a new song
"show()" to complete the lyrics in the current song.

I like the way that I arranged my classes, for example the "Word" class doesn't represent just a raw word, it also handles testing the string for correctness (including making it punctuation insensitive), and displaying either underscores or the correct word.

It's not designed to be super efficient, because it doesn't need to be. It runs without any user-noticeable delay with a text about the length of your typical lyrics. Some possible enhancements might be to not store each word distinctly even when they're the same word, but to instead have a reference to a base word so that you don't have to keep recalculating the edit distance, since all words with the same base text are treated exactly the same.