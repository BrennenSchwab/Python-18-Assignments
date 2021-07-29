"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """ 

        >>> wf = WordFinder("words.txt")
        3 words read

        >>> wf.random()
        'cat'

        >>> wf.random()
        'cat'

        >>> wf.random()
        'porcupine'

        >>> wf.random()
        'dog'
    """

    def __init__(self, words_file):
        """ initiates file, opens the file then displays teh amount of words read in file """
        file = open(words_file)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, file):
        """ Parse of the 'file' creates a list of the words """
        return [x.strip() for x in file]
    def random(self):
        """ chooses a random word from words_file and returns it"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
     """ this wordfinder excludes blank lines and comment lines
    example:

    cat.txt = [Cat, , Dog, Mouse, , #comment] # -> 6 items here, but swf should remove blank 
    and comments starting with #

    >>> swf = SpecialWordFinder("cat.txt")
        3 words read

    >>> swf.random()
    'Cat'

    ...  
    """
    def parse(self, file):
        """ Parse of the 'file' creates a list of the words, excluding blank lines """

        
        return [x.strip() for x in file if x.strip() and not x.startswith("#")]
  


