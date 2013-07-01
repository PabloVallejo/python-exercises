#
# Module 3. Simple exercises including I/O ( Input/Output )
#
# Simple exercises to use I/O functins and the `re` module.
# Documentation for input and output in python can be found in the following link.
# http://docs.python.org/2/tutorial/inputoutput.html
#
import re, time, random
from module_1 import is_palindrome_advanced, char_freq


# 32. Find palidromes.
# Scans a file line by line findind palidromes in it
# and return an array with the palindromes found.
def find_palidromes( filename = 'data/palidromes-32.md' ):

    palindromes = []
    file = open( filename, 'r' )

    for line, content in enumerate( file ):
        if is_palindrome_advanced( content ):
            palindromes.append( content )

    return palindromes


# 33. Semordnilap.
# A semordnilap is a word that when spelled backwards, produces other word.
# E.G.
#
#   strssed -> desserts
#
# This function, gets all the words in a file and finds all the words
# that when spelled backwards, are equal to other words in the file.
#
def find_semordnilaps( filename = 'data/words-33.md' ):

    semordnilaps = []
    file = open( filename, 'r' )
    words = re.findall( '\w+', file.read() )


    for word in words:

        for w in words:
            if word[ ::-1 ].lower() == w.lower():
                semordnilaps.append( w )


    return semordnilaps


# 34. Character frequency table.
# Prints a table showing how many characters of each
# charachter there are in a text file
def char_freq_table( filename = 'data/the-dream.md' ):

    file = open( filename )
    letters = re.findall( '[a-zA-Z]', file.read() )
    letters = ''.join( letters )

    result = char_freq( letters )

    # Print table
    print 'The character frequency of the file {} is as follows:'.format( filename )
    for k in result:
        print '{}: {}'.format( k, result[ k ] )



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

    import pyttsx
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


# 37. Add line numbers.
# Given a text file, this function will create a new text file
# in which all the lines from the original file are numbered
# from 1 to n.
def copy_file_count_lines( filename = 'data/text.txt' ):

    original = open( filename, 'r' )

    # Create new file
    new_file = open( 'data/output-37.md', 'w+' )

    # Read file line by line
    for line, content in enumerate( original ):
        new_file.write( '%s %s' % ( line + 1, content ) )


# 38. Average_word_length.
# Calculates the average word length in a text file
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
    return average


# 39. Guess the number game.
# Command line game that will randomly select a number from 1 to 20
# and will ask the user to guess it.
def guess_the_number_game():

    number, guesses = random.randint( 1, 20 ), 1

    user_name = raw_input( 'Hello! what is your name? \n' )
    print 'Well, {}, I am thinking of a number betweet 1 and 20.'.format( user_name )
    print 'Take a guess.'

    guess = input()
    while guess != number:

        if guess < number:
            print 'Your guess is too low.'
            print 'Take a guess.'
            guesses += 1
            guess = input()

        else:
            print 'Your guess is to high.'
            print 'Take a guess.'
            guesses += 1
            guess = input()

    if guess == number:
        print 'Good job {} you guessed my number in {} guesses!'.format( user_name, guesses )


# 40. Anagram
# Command line game that given a list of colours will pick one,
# make an Anagram with it and ask the user to decript it.
def anagram_game( words ):

    w, anagram = words[ random.randint( 0, len( words ) - 1 ) ], ''
    letters, guess = [], ''

    for letter in w:
        letters.append( letter )

    length = len( letters )

    for n in range( 0, length ):
        i = random.randint( 0, len( letters ) )
        anagram += letters[ i - 1 ]
        letters.pop( i - 1 )


    # Interactive game
    print 'Colour word anagram: {}'.format( anagram )
    guess = raw_input( 'Guess the colour word! \n' )
    while guess.lower() != w.lower():
        guess = raw_input( 'Guess the colour word! \n' )

    print 'Correct'


# 41. Lingo function
# Given two words, this function will compare them and show
# clues on the second one, that may lead to guess the first one.
def lingo( word, guess ):

    feedback, length = guess, len( word )

    # Lambdas which given a word return it enclosed in brackets or parenthesis
    add_par, add_bra = lambda s: '(' + s + ')', lambda s: '[' + s + ']'


    for i, letter in enumerate( guess ):
        if letter.lower() in word.lower():

            if i < length:
                clue = add_bra( letter ) if letter.lower() == word[ i ].lower() else add_par( letter )

            else:
                clue = add_par( letter )

            feedback = re.sub( letter, clue, feedback )


    return feedback


# 41 Lingo Game
# Lingo is a game for guessing a hidden 5 characters word.
# Users enter a word and it is compared with the one to guess
# and clues are show for the user to finally guess the word.
def lingo_game():

    words = [ 'tiger', 'house', 'cigar', 'opera', 'modem', 'horse', 'plane', 'white' ]
    word = words[ random.randint( 0, len( words ) -1 ) ]

    guess = raw_input( 'Enter your guess for the five characters long word. \n' )
    while guess.lower() != word.lower():
        print lingo( word, guess )
        guess = raw_input( 'Oop. Try again \n' )

    if guess.lower() == word.lower():
        print 'You guessed the word.'