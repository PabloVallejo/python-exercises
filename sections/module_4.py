#
# Section 4: Somehow harder exercises
#
# This section covers regular expressions, input and output, the use of higher-
# order-functions and a little more advanced loops.
#
from collections import defaultdict
import random, re


# 42. Sentence Splitter
# Given a text file, this program separates its sentences based
# on a set of rules and then, returns the result.
def split_sentences( filename = 'data/text-42.md' ):

    file = open( filename )
    text = file.read()

    # Find and add a newline after every occurrence of a dot not preceded by ( `Mrs.`, `Mr.` or `Dr.` )
    # and do followed by a space and an uppercase letter.
    text = re.sub( r'\.(?<!Mrs.)(?<!Mr.)(?<!Dr.)(\s[A-Z])', r'.\n\1', text )

    # Find and add a newline after every `?`
    text = re.sub( r'\?', '?\n', text )

    # Find and add a newline after every `!`
    text = re.sub( r'\!', '!\n', text )

    return text


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
#
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


# 45 Helper:
# Checks whether the list has a word ending with
# a specific letter and return its position,
# returns false if there are no words that match
# the criteria.
def has_word_starting_with( letter, iterable ):

    for i, w in enumerate( iterable ):
        if w.startswith( letter ):
            return i

    return False


# 45. This function will generate a sequence with the
# highest possible list of pokemons in which the final letter
# of the name of the preceding one is the first letter of the
# following one
# Example:
#
#   banette -> emboar -> relicant -> tirtuga -> audino ...
#
def words_domino( filename = 'data/pokemons-list.md' ):

    file = open( filename )
    words = re.findall( '\w+', file.read() )
    words_set = words[:]
    best_fit, series = [], []

    # Loop through all the elements in the word list
    # looking for series starting from each one
    for w in words:
        current_word = w
        words_set = words[:]
        i = has_word_starting_with( current_word[ -1 ], words_set )

        # Do the lookut for words starting with the final letter of `current_word`
        while i is not False:
            series.append( current_word )
            current_word = words_set[ i ]
            words_set.pop( i )
            i = has_word_starting_with( current_word[ -1 ], words_set )


        # If the current series has more items than the actual `best_fit`,
        # set `best_fit` to the current series
        if len( series ) > len( best_fit ):
            best_fit = series[:]

        # Empty the series in order to lookup again
        series = []

    return best_fit


# 46. Anternade
# Given a word list, this function takes each word and tries to make two
# smaller words  using all the letters of that word.
# Example:
#
#   'board': makes 'bad' and 'or'
#   'waists': makes: 'wit' and 'ass'
#
def alternade( filename = 'data/words-43.md' ):

    file = open( filename )
    words = re.findall( '\w+', file.read() )
    alternades = {}

    for w in words:
        words_subset = words[:]
        words_subset.remove( w )

        # Skip the look if the current word has less than two characters
        if len( w ) < 2: continue

        first = has_word_starting_with( w[ 0 ], words_subset )
        second = has_word_starting_with( w[ 1 ], words_subset )

        word_set, fit = list( w ), True
        fit = True

        # Enter if both words found
        if first is not False and second is not False:

            if len( words_subset[ first ] ) < len( w ) and len( words_subset[ second ] ) < len( w ):

                # First word
                for l in words_subset[ first ]:
                    if l in word_set:
                        i = word_set.index( l )
                        word_set.pop( i )

                    else: fit = False

                # Second word
                for letter in words_subset[ second ]:
                    if letter in word_set:
                        k = word_set.index( letter )
                        word_set.pop( k )

                    else: fit = False

                if len( word_set ) is 0:
                    alternades[ w ] = [ words_subset[ first ], words_subset[ second ], ]

    return alternades
