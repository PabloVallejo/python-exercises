from collections import defaultdict
import random, re











# 42. Sentence Splitter
# Given a text file, this program write in another text file each sentence
# in a new line.
def split_sentences( filename = 'data/text-42.md' ):

    file = open( filename )

    # Find sentence # 1
    # Sentences boundaries
    #
    #   '.', '?' or '!'
    #
    # Find first dot

    # return file.read()
    #
    # 1. Find everything until a character
    # \[^.]*\

    # Get the position of the last occurrence  of a char in a string
    #
    # string = 'sample/string/here'
    # string.rfind( '/' ) # -> 13
    #
    # Get letter after that
    # Get position of first dot


# 43 Helper: Load Words
# Returns an array of all the words in a file
def load_words( filename ):
    with open( filename ) as f:
        return [ word.rstrip() for word in f ]


# 43. Find Anagram
# Finds all the anagrams in a text file and returns a list
# with all the group of anagrams
# Adapted from answer at
# http://stackoverflow.com/questions/8286554/find-anagrams-for-a-list-of-words
def find_anagrams( filename = 'data/words-43.md' ):

    d, anagrams = defaultdict( list ), []
    words = load_words( filename )

    for word in words:
        d[ ''.join( sorted( word ) ) ].append( word )

    for k, v in d.iteritems():
        if len( v ) > 1:
            anagrams.append( v )

    return anagrams


# 44 Helper: Checks whether a set pairs of squared brackets
# is sintactically correct. This means, whether every opening bracket ( '[' )
# is closed.
# Example:
#    []        True
#    [][]      True
#    []][[]    False
def validate_brackets( string ):

    string = re.sub( '\s+', '', string )

    # Keep looping while there are ocurrences of `[]`.
    while len( re.findall( r'\[]', string ) ) > 0:
        string = re.sub( r'\[]', '', string )

    if len( string ) == 0:
        return True

    return False


# 44. Analyze backets
# This function generates a random string with `n` opening brackets ( '[' ) and `n`
# closing brackets ( ']' ) in a random order. After that, it checks to see whether
# the generated string is combrises for pairs of opening/closing brackets.
# After that, it print the output to the console like in this example.
# Example:
#
#    []        OK   ][        NOT OK
#    [][]      OK   ][][      NOT OK
#    [[][]]    OK   []][[]    NOT OK
#
def analyze_rand_brackets():

    length, string, spaces = random.randint( 1, 5 ) * 2, '', ''
    brackets, openning, closing = '[]', 0, 0

    for i in range( 0, length ):
        rand_bracket = random.randint( 0, 1 )
        string += brackets[ rand_bracket ]

    for space in range( 1, 12 - len( string ) ):
        spaces += ' '

    feedback = 'OK' if validate_brackets( string ) else 'NOT OK'
    print '{}{}{}'.format( string, spaces, feedback )


