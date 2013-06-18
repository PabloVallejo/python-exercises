
# Unit test for exercises
#

import random
import unittest
import exercises


# Test
class TestSequenceFunctions( unittest.TestCase ):

    # Initialize
    def setUp( self ):
        self.seq = range( 10 )


    # max()
    def test_max( self ):
        a, b = 10, 20

        max = exercises.max( a, b )
        self.assertEqual( max, b )

        # 2
        c, d = 50, 100
        max = exercises.max( c, d )
        self.assertNotEqual( max, c )


    # max_of_three()
    def test_max_of_three( self ):
        a, b, c = 10, 20, 40

        max = exercises.max_of_three( a, b, c )
        self.assertEqual( max, c )

        # 2
        d, e, f = 54, 90, 10
        max = exercises.max_of_three( d, e, f )
        self.assertNotEqual( max, f )


    # str_len()
    def test_str_len( self ):
        string = 'Sample string'

        length = exercises.str_len( string )
        self.assertEqual( length, 13 )


    # is_vowel()
    def test_is_vowel( self ):
        a, b = 'a', 'z'

        is_vowel = exercises.is_vowel( a )
        self.assertTrue( is_vowel )

        is_vowel = exercises.is_vowel( b )
        self.assertFalse( is_vowel )


    # translate()
    def test_translate( self ):
        original, translated = 'This is fun', 'Tothohisos isos fofunon'

        translate = exercises.translate( original )
        self.assertEqual( translate, translated )

    # Sum: sum()
    def test_sum( self ):
        items = [ 1, 2, 3, 4, 5 ]
        total = exercises.sum( items )

        self.assertEqual( total, 15 )


    # Multiply
    def test_multiply( self ):
        items = [ 1, 2, 3, 4, 5 ]
        total = exercises.multiply( items )

        self.assertEqual( total, 120 )

    # Reverse
    def test_reverse( self ):
        string = 'I am testing'
        truncated = exercises.reverse( string )

        self.assertEqual( truncated, 'gnitset ma I' )

    # Is palidrome
    def test_is_palindrome( self ):
        string = 'radar'

        is_palindrome = exercises.is_palindrome( 'radar' )
        self.assertTrue( is_palindrome )

    # Is member
    def test_is_member( self ):
        val = 's'
        group = [ 'sample', 's', 1 ]

        is_member = exercises.is_member( val, group )
        self.assertTrue( is_member )


    # Overlaping
    def test_overlaping( self ):
        a, b, c = [ 1, 2, 3, 4 ], [ 7, 6, 5, 4 ], [ 9, 8 ]

        overlaping = exercises.overlaping( a, b )
        self.assertTrue( overlaping )

        overlaping = exercises.overlaping( a, c )
        self.assertFalse( overlaping )


    # Generate n chars
    def test_generate_n_chars( self ):
        char, times = 'x', 5

        new_string = exercises.generate_n_chars( times, char )
        self.assertEqual( new_string, 'xxxxx' )


    # Historygram
    def test_historygram( self ):

        description = [ 1, 2, 3, 4, 5 ]
        exercises.historigram( description )


    # ROT-13 encrypt
    def test_rot_13_encrypt( self ):
        string = 'Caesar cipher? I much prefer Caesar salad!'
        intended = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'

        encrypted = exercises.rot_13_encrypt( string )
        self.assertEqual( encrypted, intended )


    # ROT-13 decrypt
    def test_rot_13_decrypt( self ):
        intended = 'Caesar cipher? I much prefer Caesar salad!'
        string = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'

        decrypted = exercises.rot_13_decrypt( string )
        self.assertEqual( decrypted, intended )

    # Max in list
    def test_max_in_list( self ):

        list = [ 1, 2, 3, 4, 44, 6, 10, 7 ]
        max = exercises.max_in_list( list )

        self.assertEqual( max, 44 )

    # Map word list to length list
    def test_map_words( self ):

        words = [ 'one', 'two', 'three', 'four' ]
        result = exercises.map_words( words )

        self.assertEqual( result, [ 3, 3, 5, 4 ] )


    # Longest word
    def test_longest_word( self ):

        words = [ 'Sheena', 'leads', 'Shelia', 'needs' ]
        longest = exercises.longest_word( words )

        self.assertEqual( longest, 6 )


    # Filter words
    def test_filter_words( self ):

        words = [ 'How', 'can', 'a', 'clam', 'cram', 'in', 'a', 'clean', 'cream', 'can?' ]

        result = exercises.filter_long_words( words, 3 )
        self.assertEqual( [ 'How', 'can', 'clam', 'cram', 'clean', 'cream', 'can?' ], result )

    # Is pangram
    def test_is_pangram( self ):

        phrase = 'The quick brown fox jumps over the lazy dog'
        is_pangram = exercises.is_pangram( phrase )

        self.assertTrue( is_pangram )

    # 21. Character frequecy
    def test_char_freq( self ):

        string = 'aabbccdddeeeefffff'
        char_freq = exercises.char_freq( string )

        self.assertEqual( char_freq, { 'a': 2, 'c': 2, 'b': 2, 'e': 4, 'd': 3, 'f': 5 } )


    # 23. Correct
    def test_correct( self ):

        string = 'This is a.Bad  formatted string.It      is to be fixed.'
        corrected = exercises.correct( string )

        self.assertEqual( 'This is a. Bad formatted string. It is to be fixed.', corrected )


# Run
if __name__ == '__main__':
    unittest.main()