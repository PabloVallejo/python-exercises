from collections import defaultdict
import random

# 43. Anagram
# Given a text file of words, this program will
# find the most anagrams in it.
def find_anagrams( filename = 'data/words-43.md' ):
    return ''
    # archive, anagrams = open( filename ), []
    # words = re.findall( '\w+', archive.read() )

    # for word in words:
    #     for w in words:

    #         if not word == w:
    #             if len( word ) == len( w ):
    #                 is_anagram = True
    #                 for letter in word:
    #                     if not letter in w:
    #                         is_anagram = False

    #                 if is_anagram:
    #                     anagrams.append( word )

    # return anagrams


# Helper: Load Words
# Returns an array of all the words in a file
def load_words( filename ):
    with open( filename ) as f:
        return [ word.rstrip() for word in f ]


# 43. Find Anagram
# Finds all the anagrams in a file and return a list
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


# 44. Checks backets
# This function generates a random string with `n` opening brackets ( '[' ) and `n`
# closing brackets ( ']' ) in a random order. After that, it checks to see whether
# the generated string is combrises for pairs of opening/closing brackets.
#
# Your task in this exercise is as follows:

# Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
# Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.
# Examples:

#    []        OK   ][        NOT OK
#    [][]      OK   ][][      NOT OK
#    [[][]]    OK   []][[]    NOT OK
#    [[[][]]]
#
def analyze_brackets():

    length, string = random.randint( 2, 10 ), ''
    brackets, openning, closing = '[]', 0, 0

    for i in range( 0, length ):
        rand_bracket = random.randint( 0, 1 )
        string += brackets[ rand_bracket ]

    # Analyze combination
    openning, closing = re.findall( '\[', string ), re.findall( '\]', string )
    if not openning == closing:
        return False

    # Deep checks
    # While have the same
    while openning == closing and openning != 0:
        string = re.sub( r'\[]', '', string )
        if len( string ) > 1:
            string = re.sub( r'\[]' )


    # [][] -> OK
    # []][[] -> Bad
    # [][][]
    # []][ -> Bad

    # print string
    # print openning
    # print closing

