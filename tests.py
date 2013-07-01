
# Unit tests for exercises
#
# Note: Commented test are the ones that produce output or require user
# input from the command line. This tests have been commented in order not to
# pause the test suite.
#
# In order to run the functions contained in these tests, you can uncomment the tests
# or open the command line in the `sections` folder
# and import the module in which the specific function is in
# and then run the function from there.
# E.G.
#
#   $ cd ~/python-exercises/sections
#   $ python
#
#   Python 2.7 (r27:82525, Jul ......
#   >>> import module_1
#   >>> module_1.historygram( [ 1, 2, 3 ] )
#   *
#   **
#   ***
#

import random
import unittest
import exercises


# Test
class TestSequenceFunctions( unittest.TestCase ):

    # Initialize
    def setUp( self ):
        self.seq = range( 10 )


    # 1. max()
    def test_max( self ):
        a, b = 10, 20

        max_num = exercises.max_num( a, b )
        self.assertEqual( max_num, b )

        # 2
        c, d = 50, 100
        max_num = exercises.max_num( c, d )
        self.assertNotEqual( max_num, c )


    # 2. max_of_three()
    def test_max_of_three( self ):
        a, b, c = 10, 20, 40

        max = exercises.max_of_three( a, b, c )
        self.assertEqual( max, c )

        # 2
        d, e, f = 54, 90, 10
        max = exercises.max_of_three( d, e, f )
        self.assertNotEqual( max, f )


    # 3. str_len()
    def test_str_len( self ):
        string = 'Sample string'

        length = exercises.str_len( string )
        self.assertEqual( length, 13 )


    # 4. is_vowel()
    def test_is_vowel( self ):
        a, b = 'a', 'z'

        is_vowel = exercises.is_vowel( a )
        self.assertTrue( is_vowel )

        is_vowel = exercises.is_vowel( b )
        self.assertFalse( is_vowel )


    # 5. translate()
    def test_translate( self ):
        original, translated = 'This is fun', 'Tothohisos isos fofunon'

        translate = exercises.translate( original )
        self.assertEqual( translate, translated )

    # 6. sum()
    def test_sum( self ):
        items = [ 1, 2, 3, 4, 5 ]
        total = exercises.sum( items )

        self.assertEqual( total, 15 )


    # 6.1 multiply()
    def test_multiply( self ):
        items = [ 1, 2, 3, 4, 5 ]
        total = exercises.multiply( items )

        self.assertEqual( total, 120 )

    # 7. reverse()
    def test_reverse( self ):
        string = 'I am testing'
        truncated = exercises.reverse( string )

        self.assertEqual( truncated, 'gnitset ma I' )

    # 8. is_palidrome()
    def test_is_palindrome( self ):
        string = 'radar'

        is_palindrome = exercises.is_palindrome( 'radar' )
        self.assertTrue( is_palindrome )

    # 9. is_member()
    def test_is_member( self ):
        val = 's'
        group = [ 'sample', 's', 1 ]

        is_member = exercises.is_member( val, group )
        self.assertTrue( is_member )


    # 10. overlapping()
    def test_overlapping( self ):

        a, b, c = [ 1, 2, 3, 4 ], [ 7, 6, 5, 4 ], [ 9, 8 ]

        overlapping = exercises.overlapping( a, b )
        self.assertTrue( overlapping )

        overlapping = exercises.overlapping( a, c )
        self.assertFalse( overlapping )


    #11. generate_n_char()
    def test_generate_n_chars( self ):

        char, times = 'x', 5

        new_string = exercises.generate_n_chars( times, char )
        self.assertEqual( new_string, 'xxxxx' )


    # 12. historygram()
    # As this function generates output
    # it will not be tested.
    # def test_historygram( self ):
        # description = [ 1, 2, 3, 4, 5 ]
        # exercises.historigram( description )


    # 13. max_in_list()
    def test_max_in_list( self ):

        list = [ 1, 2, 3, 4, 44, 6, 10, 7 ]
        max = exercises.max_in_list( list )

        self.assertEqual( max, 44 )


    # 14. map_words()
    def test_map_words( self ):

        words = [ 'one', 'two', 'three', 'four' ]
        result = exercises.map_words( words )

        self.assertEqual( result, [ 3, 3, 5, 4 ] )


    # 15. longest_word()
    def test_longest_word( self ):

        words = [ 'Sheena', 'leads', 'Shelia', 'needs' ]
        longest = exercises.longest_word( words )

        self.assertEqual( longest, 6 )


    # 16. filter_words()
    def test_filter_words( self ):

        words = [ 'How', 'can', 'a', 'clam', 'cram', 'in', 'a', 'clean', 'cream', 'can?' ]

        result = exercises.filter_long_words( words, 3 )
        self.assertEqual( [ 'How', 'can', 'clam', 'cram', 'clean', 'cream', 'can?' ], result )


    # 17. is_palindrome_advanced()
    def test_is_palindrome_advanced( self ):

        # string = 'Was it a rat I saw?'
        strings = [ 'Was it a rat I saw?', 'Step on no pets', 'Sit on a potato pan, Otis' ]

        for string in strings:
            is_palindrome = exercises.is_palindrome_advanced( string )
            self.assertTrue( is_palindrome )


    # 18. is_panagram()
    def test_is_pangram( self ):

        phrase = 'The quick brown fox jumps over the lazy dog'
        is_pangram = exercises.is_pangram( phrase )

        self.assertTrue( is_pangram )


    # 19. 99 Bottles of Beer
    # As this function produces output,it is
    # not tested
    # def test_99_bottles_of_beer( self ):
        # exercises.sing_99_bottles_of_beer()


    # 21. char_freq()
    def test_char_freq( self ):

        string = 'aabbccdddeeeefffff'

        char_freq = exercises.char_freq( string )
        self.assertEqual( char_freq, { 'a': 2, 'c': 2, 'b': 2, 'e': 4, 'd': 3, 'f': 5 } )



    # 22. rot_13_encrypt()
    def test_rot_13_encrypt( self ):
        string = 'Caesar cipher? I much prefer Caesar salad!'
        intended = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'

        encrypted = exercises.rot_13_encrypt( string )
        self.assertEqual( encrypted, intended )


    # 22.1 rot_13_decrypt()
    def test_rot_13_decrypt( self ):
        intended = 'Caesar cipher? I much prefer Caesar salad!'
        string = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'

        decrypted = exercises.rot_13_decrypt( string )
        self.assertEqual( decrypted, intended )


    # 23. correct()
    def test_correct( self ):

        string = 'This is a.Bad  formatted string.It      is to be fixed.'
        corrected = exercises.correct( string )

        self.assertEqual( 'This is a. Bad formatted string. It is to be fixed.', corrected )

    # 24. make_3d_form()
    def test_make_3d_form( self ):

        words = [ 'brush', 'run', 'fix', 'carry' ]
        spec, results = [ 'brushes', 'runs', 'fixes', 'carries' ], []

        for word in words:
            third_form = exercises.make_3d_form( word )
            results.append( third_form )

        self.assertEqual( spec, results )


    # 25. make_ing_form()
    def test_make_ing_form( self ):

        words = [ 'sleep', 'write', 'die', 'eat', 'begin' ]
        spec, results = [ 'sleeping', 'writing', 'dying', 'eating', 'beginning' ], []

        for word in words:
            ing_form = exercises.make_ing_form( word )
            results.append( ing_form )

        self.assertEqual( results, spec )


    # 26. max_in_list_v1()
    def test_max_in_list_v1( self ):

        numbers, spec = [ 5, 19, 10, 2, 7 ], 19
        result = exercises.max_in_list_v1( numbers )

        self.assertEqual( result, spec )


    # 27. map_words_v1()
    def test_map_words_v1( self ):

        words, spec = [ 'Gorilla', 'Monkey', 'Tiger', 'Giraffe' ], [ 7, 6, 5, 7 ]
        v1, v2 = exercises.map_words_v1( words ), exercises.map_words_v2( words )

        self.assertEqual( v1, spec )
        self.assertEqual( v2, spec )


    # 28. find_longest_word_advanced()
    def test_find_longest_word_advanced( self ):

        words = [ 'house', 'happiness', 'skateboarding', 'landscape'  ]
        longest, spec = exercises.find_longest_word_advanced( words ), 13

        self.assertEqual( longest, spec )


    # 29. filter_long_words_advanced()
    def test_find_long_words_advanced( self ):

        words = [ 'one', 'two', 'three', 'four', 'five', 'eighty' ]
        result = exercises.filter_long_words_advanced( words, 4 )
        spec = [ 'three', 'four', 'five', 'eighty' ]

        self.assertEqual( spec, result )


    # 30 translate_words()
    def test_translate_words( self ):
        words = [ 'merry', 'christmas', 'and', 'happy', 'new', 'year' ]
        spec = [ 'merry', 'jul', 'och', 'happy', 'nya', '\xc3\xa5r' ]

        translated = exercises.translate_words( words )
        self.assertEqual( translated, spec )


    # 31. map_v1()
    def test_map_v1( self ):
        items, spec = [ 'one', 'two', 'three' ], [ 3, 3, 5 ]
        result = exercises.map_v1( len, items )

        self.assertEqual( result, spec )


    # 31.1 filter_v1()
    def test_filter_v1( self ):
        items, spec = [ 'one', 'two', 'three', 'four' ], [ 'three', 'four' ]
        fn = lambda x: len( x ) > 3

        result = exercises.filter_v1( fn , items )
        self.assertEqual( result, spec )


    # 31.2 reduce_v1()
    def test_reduce_v1( self ):

        numbers, spec = [ 1, 2, 3, 4, 5 ], 15
        fn = lambda x, y: x + y

        result = exercises.reduce_v1( fn, numbers )
        self.assertEqual( result, spec )


    # 32. find_palidromes()
    def test_find_palindeomes( self ):

        spec = [ 'Satan, oscillate my metallic sonatas\n', 'Was it a rat I saw?\n', 'Rise to vote sir\n' ]
        palindromes = exercises.find_palidromes( 'data/palindromes-32.md' )

        self.assertEqual( spec, palindromes )


    # 33. find_semordnilaps()
    def test_find_semordnilaps( self ):

        spec = [ 'palindromes', 'semordnilap', 'desserts', 'stressed' ]

        semordnilaps = exercises.find_semordnilaps( 'data/words-33.md' )
        self.assertEqual( semordnilaps, spec )


    # 34. test_char_freq_table()
    # # This function also produces output
    # so it will not be tested.
    # def test_char_freq_table( self ):
        # exercises.char_freq_table()

    # 35. speak_ICAO
    # As this function produces sound
    # it will not be tested.
    # def test_speak_ICAO( self ):
        # string = 'Hello world.'
        # exercises.speak_ICAO( string, 0, 1 )

    # 36. find_hapax_legomenons()
    def test_hapax_legomenon( self ):

        ideal = [ 'and', 'valleys', 'over', 'it', 'greenest', 'seraph', 'our', 'its', 'stood', 'stately', 'there', 'spread', 'monarch', 'angels', 'head', 'good',
            'never', 'half', 'by', 'fabric', 'a', 'reared', 'of', 'radiant', 'tenanted', 'thought', 's', 'so', 'dominion', 'pinion', 'once' ]
        hapax_legomenons = exercises.find_hapax_legomenons( 'data/usher.md' )

        self.assertEqual( ideal, hapax_legomenons )


    # 37. copy_file_count_lines()
    def test_copy_file_count( self ):

        ideal = "1 O! nothing earthly save the ray\n2 (Thrown back from flowers) of Beauty's eye,"

        # Create file
        exercises.copy_file_count_lines( 'data/short-poem.md' )

        # Read file
        result = open( 'data/output-37.md', 'r' )
        self.assertEqual( result.read(), ideal )


    # 38. average_word_length()
    def test_average_word_length( self ):

        ideal_average = 3
        average = exercises.average_word_length( 'data/the-dream.md' )

        self.assertEqual( average, ideal_average )


    # 39. Guess the number game
    # Since this function is an interactive
    # command line game it will not be tested.
    # def test_guess_the_number_game( self ):
    #     exercises.guess_the_number_game()

    # 40. Anagram
    # Since this function is an interactive
    # command line game it will not be tested.
    # def test_anagram_game( self ):

    #     words = [ 'White', 'Blue', 'Red', 'Violet', 'Turquoise', 'Black', 'Yellow' ]
    #     exercises.anagram_game( words )


    # 41, lingo()
    def test_lingo( self ):

        word, guess, spec = 'Tiger', 'Finger', 'F[i]n(g)(e)(r)'
        result = exercises.lingo( word, guess )

        self.assertEqual( result, spec )


    # 42. Split Sentences
    # This function also generates output, so it will
    # not be tested.
    # def test_split_sentences( self ):
        # result = exercises.split_sentences( 'data/text-42.md' )
        # print result


    # 43. find_anagrams()
    def test_find_anagrams( self ):
        anagrams = exercises.find_anagrams( 'data/words-43.md' )
        self.assertTrue( isinstance( anagrams, list ) )


    # 44.0 validate_brackets()
    def test_validate_brackets( self ):

        string = '[[ [][] ]]'
        validate = exercises.validate_brackets( string )

        self.assertTrue( validate )


    # 44. Analyze brackets
    # This function is an interactive command line procedure
    # so it will not be tested.
    # def test_analyze_brackets( self ):
        # exercises.analyze_brackets()


    # 45. words_domino()
    def test_words_domino( self ):

        spec = [ 'baltoy', 'yamask', 'kangaskhan', 'nosepass', 'sableye', 'emboar', 'registeel', 'landorus', 'scolipede', 'emolga' ]
        result = exercises.words_domino( 'data/pokemons-list.md' )

        self.assertEqual( spec, result )


    # 46. alternade()
    # As alternade produces output, it will not be tested.
    # def test_alternade( self ):
        # exercises.alternade()


# Run
if __name__ == '__main__':
    unittest.main()