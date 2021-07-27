def print_upper_words(words):
    '''Converts each string in [] and prints them on a separate line uppercased
        >>> print_upper_words(["hi", "hello", "bye"])
        HI
        HELLO
        BYE
    '''
    for word in words:
        print(word.upper())
    
def print_upper_wordse(words):
    """ Will convert input words into uppercase only if i starts with the letter e or E
    
     >>> print_upper_words_e(["okay", "dokay", "easy", "Equator"])
        EASY
        EQUATOR
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words_selective(words, must_start_with):
    '''Prints each word on separate line if the word starts with the given letter
    but it is case sensitive
        >>>  print_upper_words_selective(["okay", "dokay", "Do", "Pluto"],{"d", "P"})
        DOKAY
        PLUTO
    '''
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

