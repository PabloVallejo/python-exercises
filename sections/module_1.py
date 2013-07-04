# Section 1. Very simple exercises
#
# This selection of exercises is intended for developers
# to get a basic understanding of logical operators and loops in Python
#

import re

# 1. Max of two numbers.
def max_num( a, b ):

    if a > b:
        return a

    return b


# 2. Max of three numbers.
def max_of_three( a, b, c ):
    return max_num( a, max_num( b, c ) )


# 3. Calculates the length of a string.
def str_len( string ):

    count = 0
    for letter in string:
        count += 1

    return count


# 4. Returns whether the passed letter is a vowel.
def is_vowel( letter ):
    vowels = 'aeiou'
    return letter in vowels


# 5. Translates an English frase into `Robbers language`.
# Sample:
#
#   This is fun
#   Tothohisos isos fofunon
#
def translate( string ):

    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    translated = ''

    for letter in string:

        if letter in consonants:
            parsed = '%so%s' % ( letter, letter.lower() )
            translated = translated + parsed

        else:
            translated = translated + letter

    return translated


# 6. Sum.
# Sums all the numbers in a list.
def sum( items ):

    total = 0

    for a in items:
        total += a

    return total


# 6.1. Multiply.
# Multiplies all the items in a list.
def multiply( items ):

    total = items[ 0 ]

    for x in items:
        total *= x

    return total


# 7. Reverse.
# Reverses a string.
# 'I am testing' -> 'gnitset ma I'
def reverse( string ):

    truncated = ''
    index = len( string )

    # Loop over the string inversively
    while index > 0:

        truncated += string[ index - 1 ]
        index = index - 1

    return truncated


# 8. Is palindrome.
# Checks whether a string is palindrome.
# 'radar' > reversed : 'radar'
def is_palindrome( string ):

    if string == reverse( string ):
        return True

    return False


# 9. Is member.
# Checks whether a value x is contained in a group of values.
#   1 -> [ 2, 1, 0 ] : True
def is_member( x, group ):

    for value in group:
        if x == value:
            return True

    return False


# 10. Overlapping.
# Checks whether two lists have at least one number in common
def overlapping( a, b ):

    # Using `is_member()` method
    for x in a:
        if is_member( x, b ):
            return True

    return False

    # Nested loop way of doing it
    # for x in a:

    #     for y in b:
    #         if x == y:
    #             return True

    # return False


# 11. Generate n chars.
# Generates `n` number of characters of the given one.
#
#   generate_n_chars( 5, 'n' )
#   -> nnnnn
#
def generate_n_chars( times, char ):

    output = ''

    while( times > 0 ):
        output += char
        times = times - 1

    return output


# 12. Historigram.
# Takes a list of integers and prints a historigram of it.
#   historigram( [ 1, 2, 3 ] ) ->
#       *
#       **
#       ***
#
def historigram( items ):

    for x in items:
        chars = generate_n_chars( x, '*' )
        print( chars )


# 13. Max in list.
# Gets the larges number in a list of numbers.
def max_in_list( list ):

    max = list[ 0 ]

    for x in list:
        if x > max:
            max = x

    return max


# 14. Map words to numbers.
# Gets a list of words and returns a list of integers
# representing the length of each word.
#
#   [ 'one', 'two', 'three' ] -> [ 3, 3, 5 ]
#
def map_words( words ):
    result = []

    for word in words:
        result.append( str_len( word ) )

    return result


# 15. Find longest wors.
# Receives a list of words and returns the length
# of the longest one.
#
#   [ 'one', 'two', 'three', 'four' ] -> 5
#
def longest_word( words ):

    # Asume the first word is the longest one
    longest = str_len( words[ 0 ] )

    for word in words:
        if str_len( word ) > longest:
            longest = str_len( word )

    return longest


# 16. Filter long words.
# Receives a list of words and an integer `n` and returns
# a list of the words that are longer than n.
def filter_long_words( words, x ):

    result = []

    for word in words:
        if str_len( word ) >= x:
            result.append( word )

    return result


# 17. Version of palindrome that ignores punctuation, capitalization and
# spaces, so that a larger range of frases can be clasified as palindromes.
#
#   ( "Dammit, I'm mad!" ) -> is palindrome
#
def is_palindrome_advanced( string ):

    stripped = re.sub( r'[^a-zA-z]+', '', string )
    reversed = reverse( stripped )

    if stripped.lower() == reversed.lower():
        return True

    return False


# 18. Is pangram.
# Checks whether a phrase is pangram, that is, if
# it contains all the letters of the alphabet.
def is_pangram( phrase ):

    abec = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

    for a in phrase:
        if a in abec:
            i = abec.index( a )
            abec.pop( i )

    if len( abec ) == 0:
        return True

    return False


# 19. 99 Bottles of beer.
# 99 Bottles of beer is a traditional song in the United States and Canada.
# It has a very repetitive lyrics and it is popular to sing it in very long trips.
# The lyrics of the song are as follows.
#
#   99 bottles of beer in the wall, 99 bottles of beer.
#   Take one down, pass it arrown, 98 bottles of beer.
#
# The song is repeated having one less bottle each time until there are no more
# bottles to count.
#
def sing_99_bottles_of_beer():

    for i in reversed( range( 1, 100 ) ):

        print '{} bottle{} of beer in the wall, {} bottle{} of beer.'.format(
                i, 's' if i != 1 else '', i, 's' if i != 1 else '' )

        print 'Take one down, pass it around, {} bottle{} of beer on the wall.'.format(
            i - 1, 's' if i - 1 != 1 else '' )


# 20. Note: exercise number 20 is the same as exercise # 30


# 21. Character frequency.
# Counts how many characters of the same letter there are in
# a string.
#
#   ( 'aabbccddddd' ) -> { 'a': 2, 'b': 2, 'c': 2, d: 5 }
#
def char_freq( string ):

    dict = {}

    for a in string:
        keys = dict.keys()

        if a in keys:
            dict[ a ] += 1

        else:
            dict[ a ] = 1

    return dict


# 22. ROT-13: Encrypt.
# Encrypts a string in ROT-13.
#
#   rot_13_encrypt( 'Caesar cipher? I much prefer Caesar salad!' ) ->
#   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
#
def rot_13_encrypt( string ):

    # Magnitud of rotation and dictionary
    rotate_by, dictionary = 13, {}
    abec = 'abcdefghijklmnopqrstuvwxyz'


    i = 0
    while i < len( abec ):

        index = i + rotate_by
        if index > 25:
            index = index - 26

        dictionary[ abec[ i ] ] = abec[ index ]
        i += 1


    # Build phrase
    # Pass any character that is not in abec
    encrypted = ''
    for char in string:

        is_upper = char.istitle()
        char = char.lower()

        if not char in abec:
            encrypted = encrypted + char

        else:
            char = dictionary[ char ]
            char = char if not is_upper else char.upper()
            encrypted = encrypted + char

    return encrypted;


# 22.1 ROT-13: Decrypt.
#
#   rot_13_decrypt( 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!' ) ->
#   Caesar cipher? I much prefer Caesar salad!
#
# Since we're dealing with offset 13 it means that decrypting a string
# can be accomplished with the encrypt function given that the alphabet contains
# 26 letters.
def rot_13_decrypt( string ):
    return rot_13_encrypt( string )


# 23. Correct.
# Takes a string and sees that 1) two or more occurences of a space
# are compressed into one. 2) Adds a space betweet a letter and a period
# if they have not space.
#
#   correct( 'This   is  very funny  and    cool.Indeed!' )
#   -> This is very funny and cool. Indeed!
#
def correct( string ):

    # Replace multiple whitespaces with one only
    string = re.sub( r'\s{2,}', ' ', string )

    # Add space after dots followed inmediatelly by a word
    string = re.sub( r'(?<=\.)(?=[a-zA-Z])', ' ', string )

    return string


# 24. Make third Form.
# Takes a singular verb and makes it third person.
#
#   ( 'run' ) -> 'runs'
#   ( 'Brush' ) -> 'brushes'
#
def make_3d_form( verb ):

    add_es_suffix, third_form = [ 'o', 'ch', 's', 'sh', 'x', 'z' ], False

    if verb.endswith( 'y' ):
        third_form = verb[ 0:-1 ] + 'ies'

    for suffix in add_es_suffix:
        if verb.endswith( suffix ):
            third_form = verb + 'es'

    if not third_form:
        third_form = verb + 's'

    return third_form


# 25. Make `ing` form.
# Given an infinite verb this function returns the
# present participle of it.
#
#   ( 'go' ) -> 'going'
#   ( 'sleep' ) -> 'sleep'
#
def make_ing_form( verb ):

    pp = False

    if verb.endswith( 'e' ):
        pp = verb[ 0:-1 ] + 'ing'

    if verb.endswith( 'ie' ):
        pp = verb[ 0:-2 ] + 'ying'

    # Consonant-vowel-consonant
    if not is_vowel( verb[ -1 ] ):

        if is_vowel( verb[ -2 ] ):
            if not is_vowel( verb[ -3 ] ):
                pp = verb + verb[ -1 ] + 'ing'

    if not pp:
        pp = verb + 'ing'

    return pp