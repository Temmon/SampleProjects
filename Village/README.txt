Run this with "python world.py" 

This plays with an idea I had for creating genes and genomes (in a more literal sense than a genetic algorithm; I actually want to simulate people in this case).

Each gene is a random double between 0 and 1 (initially derived from random.random()) that's interpreted according to context, so it can be viewed as a boolean, an integer, a color, or some arbitrary type that I hadn't come up with yet when I stopped development. I wanted this to kind of mimic the way a "gene" can serve multiple purposes in actual DNA, so that a given locus can be used for both hair color and "do they have a terrible disease".

The genome is the way that those things are actually interpreted. I only have two sample traits that they care about: the "doom" gene and an arbitrary color that currently doesn't have any purpose. The doom gene is a simple Mendelian trait that's on if you have a single copy, and off if you don't have any. It'll make the person die in some set time frame and was mostly just useful as a test case to make sure that inheritance was working properly. To determine if a person has a trait, you apply a genome to a person and run the genome's run method.

A person has a genome, some basic information about the person, and also a way of handling a step of the program. So you could extend the base person class's step method and make a warrior, for example, instead of the forager that I did by default. 

The world generates a genome for all the people, the initial set of people and handles stepping over each person each day. As well as user interface concerns. The UI could be separated out and certainly would be if it were made into a more complex program. It was just convenient for the pocket sized program that it currently is to all be in the same class. 
