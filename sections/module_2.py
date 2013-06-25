
#
# Higher order functions and list comprehension
#
# According to Wikipedia, high-order-functions are functions that do at least one
# of the following:
#
#   Take one or more functions as input
#   Output a function
#
# In python, there are several examples of such functions, some of them are:
#
#   filter( function, iterable )
#   map( function, iterable )
#   reduce( function, iterable )
#   max( iterable )
#   sort(  )


# 26. Largest Number
# Given a list of numbers, this function returns the largest one
# it does it using `reduce` function.
def max_in_list_v1( numbers ):

    def compare( x, y ):

        if y > x:
            return y

        return x

    largest = reduce( compare, numbers )
    return largest


# 27. Map strings
# Maps a list of words into a list of integers representing each
# word length.
# It uses the `map` higher-order-function
def map_words_v1( words ):
    return map( len, words )


# 27.1 Map strings
# Does the same as #27 but uses `List comprehensions`
# See http://www.secnetix.de/olli/Python/list_comprehensions.hawk
def map_words_v2( words ):
    return [ len( word ) for word in words ]


# 28. Find longest word
# Using high-order-function, this function receives a list of words,
# and return the longest one.
def find_longest_word_advanced( words ):

    largest = max( words, key = len )
    return len( largest )


# 29. Filter Long Words
# Takes a list of words and an integer and then return
# an array with all the words that are longer in length that
# the integer passed
def filter_long_words_advanced( words, x ):

    validate = lambda word: len( word ) >= x
    filtered_words = filter( validate, words )

    return filtered_words
