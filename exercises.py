
# Exercises Module
# Module for collecting the exercises
import re, pyttsx, time

#1. Max of two numbers
def max( a, b ):

    max = a

    if b > a:
        max = b

    return b


# 2. Max of three numbers
def max_of_three( a, b, c ):

    max = a

    if b > max:
        max = b

    if c > max:
        max = c

    return max


# 3. Calculates the length of a string
def str_len( string ):

    count = 0
    for letter in string:
        count = count + 1

    return count

# 4. Returns whether the passed letter is a vowel
def is_vowel( letter ):
    vowels = 'aeiou'

    if letter in vowels:
        return True

    return False

# 5. Translates an English word into `Robbers language`
# Sample:
#   This is fun
#   Tothohisos isos fofunon
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


# 6. Sum: sum()
# Sums all the numbers in a list
def sum( items ):

    total = 0

    for a in items:
        total = total + a

    return total


# 6.1. Multiply: multiply()
# Multiplies all the items in a list
def multiply( items ):

    total = items[ 0 ]

    for x in items:
        total = total * x

    return total


# 7. Reverse:
# Reverses a string
# 'I am testing' -> 'gnitset ma I'
def reverse( string ):

    truncated = ''
    index = len( string )

    # Loop over the string inversively
    while index > 0:

        truncated = truncated + string[ index - 1 ]
        index = index - 1

    return truncated


# 8. Is palindrome
# Checks whether a string is palindrome
# 'radar' > reversed : 'radar'
def is_palindrome( string ):

    if string == reverse( string ):
        return True

    return False


# 9. Is member
# Checks whether a value x is contained in a group of values
# 1 -> [ 2, 1, 0 ] : True
def is_member( x, group ):

    for value in group:
        if x == value:
            return True

    return False


# 10. Overlapping
# Checks whether two lists have at least one number in common
def overlaping( a, b ):

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

# 11. Generate n chars
# Generates `n` number of chars of the given one.
# ( 5, 'x' ) -> 'xxxxx'
def generate_n_chars( times, char ):

    output = ''

    while( times > 0 ):
        output = output + char
        times = times - 1

    return output


# 12. Historigram
# Takes a list of integers and prints a historigram of it
# historigram( [ 1, 2, 3 ] ) ->
#   *
#   **
#   ***
def historigram( items ):

    for x in items:
        chars = generate_n_chars( x, '*' )
        print( chars )


# 13. Max in list
# Gets the larges number in a list of numbers
def max_in_list( list ):

    max = list[ 0 ]
    for x in list:
        if x > max:
            max = x

    return max


# 14. Map words to numbers
# Gets a list of words and returns a list of integers
# representing the length of each word
# [ 'one', 'two', 'three' ] -> [ 3, 3, 5 ]
def map_words( words ):
    result = []

    for word in words:
        result.append( str_len( word ) )

    return result


# 15. Find longest wors
# Receives a list of words and returns the length
# of the longest one
# [ 'one', 'two', 'three', 'four' ] -> 5
def longest_word( words ):

    # Asume the first word as the longest one
    longest = str_len( words[ 0 ] )

    for word in words:
        if str_len( word ) > longest:
            longest = str_len( word )

    return longest


# 16. Filter long words
# Receives a list of words and an integer n and returns
# a list of the words that are longer than n
def filter_long_words( words, x ):

    result = []

    for word in words:
        if str_len( word ) >= x:
            result.append( word )

    return result


# 17. Version of palindrome that ignores punctuation, capitalization and
# spaces, so that a larger range of palidromes can be accepted.
# ( "Dammit, I'm mad!" ) -> is palindrome
def is_palindrome_advanced( string ):

    stripped = re.sub( r'[^a-zA-z]+', '', string )
    reversed = reverse( stripped )

    if stripped.lower() == reversed.lower():
        return True

    return False


# 18. Is pangram
# Checks whether a phrase is pangram, that is, if
# it contains all the letters of the alphabet
def is_pangram( phrase ):

    abec = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

    for a in phrase:
        if a in abec:
            i = abec.index( a )
            abec.pop( i )

    if len( abec ) == 0:
        return True

    return False


# 21. Character frequency
# Counts how many characters of the same letter are there in
# a string
# -> ( 'aabbccddddd' ) -> { 'a': 2, 'b': 2, 'c': 2, d: 5 }
def char_freq( string ):

    dict = {}

    for a in string:
        keys = dict.keys()

        if a in keys:
            dict[ a ] = dict[ a ] + 1

        else:
            dict[ a ] = 1

    return dict


# 22. ROT-13: Encrypt
#
# Encrypts a string in ROT-13
# rot_13_encrypt( 'Caesar cipher? I much prefer Caesar salad!' ) ->
#   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
#
def rot_13_encrypt( string ):

    # Magnitud of rotation and dictionary
    rotate_by, dictionary = 13, {}
    abec = 'abcdefghijklmnopqrstuvwxyz'


    i = 0
    while i < len( abec ):

        # dictionary[ 'a' ] = 'n'
        index = i + rotate_by
        if index > 25:
            index = index - 26

        dictionary[ abec[ i ] ] = abec[ index ]
        i = i + 1


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



# 23.1 ROT-13: Decrypts
#
# rot_13_decrypt( 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!' ) ->
#   Caesar cipher? I much prefer Caesar salad!
#
# Since we're dealing with offset 13 it means that decrypting a string
# can be accomplished with the encrypt function since the alphabet contains
# 26 letters
def rot_13_decrypt( string ):
    return rot_13_encrypt( string )


# 23. Correct
# Takes a string and sees that 1) two or more occurences of a space
# are compressed into one. 2) Adds a space betweet a letter and a period
# if they have not space.
#
# correct( 'This   is  very funny  and    cool.Indeed!' )
#  -> This is very funny and cool. Indeed!
def correct( string ):

    # Replace multiple whitespaces with one only
    string = re.sub( r'\s{2,}', ' ', string )

    # Add space after dots followed inmediatelly by a word
    string = re.sub( r'(?<=\.)(?=[a-zA-Z])', ' ', string )

    return string


# 32. Find palidromes
# Scans a file line by line findind palidromes in it
# and return an array with the palindrome lines.
def find_palidromes( filename = 'data/palidromes-32.md' ):

    file = open( filename, 'r' )

    for line, content in enumerate( file ):
        print( content )


# 33. Semordnilap
def find_semordnilaps( filename = 'data/words-33.md' ):

    semordnilaps = []
    file = open( filename, 'r' )
    words = re.findall( '\w+', file.read() )


    for word in words:

        for w in words:
            if word[ ::-1 ].lower() == w.lower():
                semordnilaps.append( w )


    return semordnilaps



# 35. Speak ICAO
#
# Given a string, this function will translate it to ICAO
# giving a speach of each letter's corresponding tranlation according ICAO dictionary.
# The pause betweet each spoken translated letter and each word can be set.
#
#  ( 'Hello', 0, 1 ) -> Will speach -> 'hotel' `wait 0 seconds`,  'echo' `wait 0 seconds`, 'lima' `wait 0 seconds`,
#      'lima' `wait 0 seconds`, 'oscar' `wait 0 seconds` `and then wait 1 second`
#
# Note: In order for this function to work you should have available `pyttsx` package
# instructions and download can be found in the following link
# https://github.com/parente/pyttsx
#
def speak_ICAO( string, letter_pause, word_pause ):

    words = re.findall( '\w+', string )
    engine = pyttsx.init()
    engine.setProperty( 'rate', 130 )

    # ICAO dictionary
    d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
     'x':'x-ray', 'y':'yankee', 'z':'zulu' }

    for word in words:

        for letter in word:
            engine.say( d[ letter.lower() ] )
            engine.runAndWait()
            time.sleep( letter_pause )

        time.sleep( word_pause )



# 36. Hapax legomenon
# Finds words that happen to be used only once in a text.
def find_hapax_legomenons( filename = 'data/the-dream.md' ):

    dict, hapax_legomenons = {}, []

    # Get words in the file
    file = open( filename, 'r' )
    words = re.findall( '\w+', file.read() )

    for word in words:
        keys = dict.keys()

        word = word.lower()
        if word in keys:
            dict[ word ] += 1

        else:
            dict[ word ] = 1

    for word in dict:
        if dict[ word ] == 1:
            hapax_legomenons.append( word )

    return hapax_legomenons
    # print( hapax_legomenons )


# 37. Write a program that given a text file will create
# a new text file in which all the lines from the original file are numbered
# from 1 to n.
# http://docs.python.org/2/tutorial/inputoutput.html
def copy_file_count_lines( filename = 'data/text.txt' ):

    original = open( filename, 'r' )

    # Create new file
    new_file = open( 'data/output-37.md', 'w+' )

    # Read file line by line
    for line, content in enumerate( original ):
        new_file.write( '%s %s' % ( line + 1, content ) )


# 38. Average_word_length
# Calculates the average word length in a file
# passed by the user.
def average_word_length( filename = 'data/the-dream.md' ):

    file = open( filename, 'r' )

    # Count words
    words = re.findall( '\w+', file.read() )

    total_length = 0
    for word in words:
        total_length += len( word )

    # Calculate average word length
    average = total_length / len( words )
    return average;

