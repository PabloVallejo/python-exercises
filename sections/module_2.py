# This Python file uses the following encoding: utf-8

# Section 2. Higher order functions and list comprehension
#
# According to Wikipedia, high-order-functions are functions that do at least one
# of the following:
#
#   Take one or more functions as input.
#   Output a function.
#
# In python, there are several examples of such functions, some of them are:
#
#   filter( function, iterable )
#   map( function, iterable )
#   reduce( function, iterable )
#   max( iterable )
#   sort( iterable )


# 26. Largest Number.
# Given a list of numbers, this function returns the largest one,
# it does it using `reduce` function.
def max_in_list_v1( numbers ):

    def compare( x, y ):

        if y > x:
            return y

        return x

    largest = reduce_v1( compare, numbers )
    return largest


# 27. Map strings
# Maps a list of words into a list of integers representing each
# word length.
# It uses the `map()` higher-order-function.
def map_words_v1( words ):
    return map( len, words )


# 27.1 Map strings.
# Does the same as #27 but uses `List comprehensions`.
# See http://www.secnetix.de/olli/Python/list_comprehensions.hawk
def map_words_v2( words ):
    return [ len( word ) for word in words ]


# 28. Find longest word.
# Using high-order-functions, this function receives a list of words,
# and return the longest one.
def find_longest_word_advanced( words ):

    largest = max( words, key = len )
    return len( largest )


# 29. Filter Long Words.
# Takes a list of words and an integer and then return
# an array with all the words that are longer in length that
# the integer passed.
def filter_long_words_advanced( words, x ):

    validate = lambda word: len( word ) >= x
    filtered_words = filter( validate, words )

    return filtered_words


# 30. Translates a list of words from English into Swedish.
# There are a fixed amount of words available for translatation.
# Uses `map()`.
# Sample:
#
#   ( [ 'happy', 'new', 'year' ] ) -> [ 'happy', 'nya', 'år' ]
#
def translate_words( words ):

    d = { 'all': 'alla', 'and': 'och', 'best': 'bäst', 'birthday': 'födelsedag', 'cake': 'kaka', 'celebrate': 'fira', 'christmas': 'jul',
        'come': 'komma', 'dreams': 'drömmar', 'for': 'för', 'good': 'bra', 'happy': 'happy', 'hope': 'hopp', 'inviting': 'inbjudande', 'is': 'är',
        'merry': 'merry', 'new': 'nya',  'thanks': 'tack', 'the': 'den', 'to': 'till', 'true': 'sant', 'us': 'oss', 'we': 'vi',
        'wishes': 'önskemål', 'year': 'år', 'your': 'din' }

    to_swedish = lambda word: d[ word ]
    translated = map_v1( to_swedish, words )

    return translated


# 31. Map.
# `map()` is a python build-in function which receive a function `f`
# and a list as parameters, and calls the function `f` on every element
# from the list.
# The following function is an implementation of the functionality that
# `map()` accomplishes.
def map_v1( fn, iterable ):

    result = []
    for v in iterable:
        result.append( fn( v ) )

    return result


# 31.1 Filter.
# As well as `map()`, `filter()` is a python built-in higer-order function,
# which get passed a function `f` and a list, and applies `f` to each of the elementf
# in the list, and return a list with only the elements that when passed to `f`
# made `f` return true.
def filter_v1( fn, iterable ):

    result = []

    for v in iterable:
        if fn( v ):
            result.append( v )

    return result


# 31.2 Reduce.
# Reduce is also a built-in higer-priority function in python.
# It receives two parameters, the first, a function `f` which receives two
# arguments: `a`, `b`, and the second an iterable `iterable` which can ba a list.
# What `reduce()` does, is calling `f` passing it as parameters the first and the second
# elements in the list, after this, reduce captures the return value of the function
# and passes it to `f` as `a`, and as `b` passes the third element of the list,
# `reduce()` captures the return value and passes it to `f` as `a` and so on, until
# there are no more elements in the list.
#
#   nums = [ 1, 2, 3, 4, 5 ]
#   sum = lambda x, y: x + y
#   reduce_v1( sum, nums )
#  -> 15
#
def reduce_v1( fn, iterable ):

    result, l = '', iterable
    result = fn( l[ 0 ], l[ 1 ] )

    l.pop( 0 )
    l.pop( 0 )

    for x in l:
        result = fn( result, x )

    return result

