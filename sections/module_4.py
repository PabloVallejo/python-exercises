from collections import defaultdict

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

