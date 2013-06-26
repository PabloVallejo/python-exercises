
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

    # 6. Sum: sum()
    def test_sum( self ):
        items = [ 1, 2, 3, 4, 5 ]
        total = exercises.sum( items )

        self.assertEqual( total, 15 )


    # 6.1 Multiply
    def test_multiply( self ):
        items = [ 1, 2, 3, 4, 5 ]
        total = exercises.multiply( items )

        self.assertEqual( total, 120 )

    # 7. Reverse
    def test_reverse( self ):
        string = 'I am testing'
        truncated = exercises.reverse( string )

        self.assertEqual( truncated, 'gnitset ma I' )

    # 8. Is palidrome
    def test_is_palindrome( self ):
        string = 'radar'

        is_palindrome = exercises.is_palindrome( 'radar' )
        self.assertTrue( is_palindrome )

    # 9. Is member
    def test_is_member( self ):
        val = 's'
        group = [ 'sample', 's', 1 ]

        is_member = exercises.is_member( val, group )
        self.assertTrue( is_member )


    # 10. Overlaping
    def test_overlaping( self ):
        a, b, c = [ 1, 2, 3, 4 ], [ 7, 6, 5, 4 ], [ 9, 8 ]

        overlaping = exercises.overlaping( a, b )
        self.assertTrue( overlaping )

        overlaping = exercises.overlaping( a, c )
        self.assertFalse( overlaping )


    #11. Generate n chars
    def test_generate_n_chars( self ):
        char, times = 'x', 5

        new_string = exercises.generate_n_chars( times, char )
        self.assertEqual( new_string, 'xxxxx' )


    # 12. Historygram
    # def test_historygram( self ):

        # description = [ 1, 2, 3, 4, 5 ]
        # exercises.historigram( description )


    # 13. Max in list
    def test_max_in_list( self ):

        list = [ 1, 2, 3, 4, 44, 6, 10, 7 ]
        max = exercises.max_in_list( list )

        self.assertEqual( max, 44 )


    # 14. Map word list to length list
    def test_map_words( self ):

        words = [ 'one', 'two', 'three', 'four' ]
        result = exercises.map_words( words )

        self.assertEqual( result, [ 3, 3, 5, 4 ] )


    # 15. Longest word
    def test_longest_word( self ):

        words = [ 'Sheena', 'leads', 'Shelia', 'needs' ]
        longest = exercises.longest_word( words )

        self.assertEqual( longest, 6 )


    # 16. Filter words
    def test_filter_words( self ):

        words = [ 'How', 'can', 'a', 'clam', 'cram', 'in', 'a', 'clean', 'cream', 'can?' ]

        result = exercises.filter_long_words( words, 3 )
        self.assertEqual( [ 'How', 'can', 'clam', 'cram', 'clean', 'cream', 'can?' ], result )


    # 17. Is Palindrome advances
    def test_is_palindrome_advances( self ):

        # string = 'Was it a rat I saw?'
        strings = [ 'Was it a rat I saw?', 'Step on no pets', 'Sit on a potato pan, Otis' ]

        for string in strings:
            is_palindrome = exercises.is_palindrome_advanced( string )
            self.assertTrue( is_palindrome )


    # 18. Is pangram
    def test_is_pangram( self ):

        phrase = 'The quick brown fox jumps over the lazy dog'
        is_pangram = exercises.is_pangram( phrase )

        self.assertTrue( is_pangram )


    # 21. Character frequecy
    def test_char_freq( self ):

        string = 'aabbccdddeeeefffff'
        char_freq = exercises.char_freq( string )

        self.assertEqual( char_freq, { 'a': 2, 'c': 2, 'b': 2, 'e': 4, 'd': 3, 'f': 5 } )


    # 22. ROT-13 encrypt
    def test_rot_13_encrypt( self ):
        string = 'Caesar cipher? I much prefer Caesar salad!'
        intended = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'

        encrypted = exercises.rot_13_encrypt( string )
        self.assertEqual( encrypted, intended )


    # 22.1 ROT-13 decrypt
    def test_rot_13_decrypt( self ):
        intended = 'Caesar cipher? I much prefer Caesar salad!'
        string = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'

        decrypted = exercises.rot_13_decrypt( string )
        self.assertEqual( decrypted, intended )


    # 23. Correct
    def test_correct( self ):

        string = 'This is a.Bad  formatted string.It      is to be fixed.'
        corrected = exercises.correct( string )

        self.assertEqual( 'This is a. Bad formatted string. It is to be fixed.', corrected )

    # 24. Make third form
    def test_make_3d_form( self ):

        words = [ 'brush', 'run', 'fix', 'carry' ]
        spec, results = [ 'brushes', 'runs', 'fixes', 'carries' ], []

        for word in words:
            third_form = exercises.make_3d_form( word )
            results.append( third_form )

        self.assertEqual( spec, results )

    # 25. Make `ing` form
    def test_make_ing_form( self ):

        words = [ 'sleep', 'write', 'die', 'eat', 'begin' ]
        spec, results = [ 'sleeping', 'writing', 'dying', 'eating', 'beginning' ], []

        for word in words:
            ing_form = exercises.make_ing_form( word )
            results.append( ing_form )

        self.assertEqual( results, spec )

    # 26. Largest number
    def test_max_in_list_v1( self ):

        numbers, spec = [ 5, 19, 10, 2, 7 ], 19
        result = exercises.max_in_list_v1( numbers )

        self.assertEqual( result, spec )


    # 27. Map words
    def test_map_words_v1( self ):

        words, spec = [ 'Gorilla', 'Monkey', 'Tiger', 'Giraffe' ], [ 7, 6, 5, 7 ]
        v1, v2 = exercises.map_words_v1( words ), exercises.map_words_v2( words )

        self.assertEqual( v1, spec )
        self.assertEqual( v2, spec )



    # 28. Find longest word advanced
    def test_find_longest_word_advanced( self ):

        words = [ 'house', 'happiness', 'skateboarding', 'landscape'  ]
        longest, spec = exercises.find_longest_word_advanced( words ), 13

        self.assertEqual( longest, spec )


    # 29. Find Long words advanced
    def test_find_long_words_advanced( self ):

        words = [ 'one', 'two', 'three', 'four', 'five', 'eighty' ]
        result = exercises.filter_long_words_advanced( words, 4 )
        spec = [ 'three', 'four', 'five', 'eighty' ]

        self.assertEqual( spec, result )


    # 30 Translate words
    def test_translate_words( self ):
        words = [ 'merry', 'christmas', 'and', 'happy', 'new', 'year' ]
        spec = [ 'merry', 'jul', 'och', 'happy', 'nya', '\xc3\xa5r' ]

        translated = exercises.translate_words( words )
        self.assertEqual( translated, spec )


    # 31. Map
    def test_map_v1( self ):
        items, spec = [ 'one', 'two', 'three' ], [ 3, 3, 5 ]
        result = exercises.map_v1( len, items )

        self.assertEqual( result, spec )

    # 31.1 Filter
    def test_filter_v1( self ):
        items, spec = [ 'one', 'two', 'three', 'four' ], [ 'three', 'four' ]
        fn = lambda x: len( x ) > 3

        result = exercises.filter_v1( fn , items )
        self.assertEqual( result, spec )


    # 31.2 Reducce
    def test_reduce_v1( self ):
        print ''


    # 32. Find palindromes
    def test_find_palindeomes( self ):

        spec = [ 'Satan, oscillate my metallic sonatas\n', 'Was it a rat I saw?\n', 'Rise to vote sir\n' ]
        palindromes = exercises.find_palidromes( 'data/palindromes-32.md' )

        self.assertEqual( spec, palindromes )


    # 33. Find semordnilaps
    def test_find_semordnilaps( self ):

        spec = [ 'palindromes', 'semordnilap', 'desserts', 'stressed' ]

        semordnilaps = exercises.find_semordnilaps( 'data/words-33.md' )
        self.assertEqual( semordnilaps, spec )


    # 36. Hapax Legomenon
    def test_hapax_legomenon( self ):

        ideal = [ 'and', 'valleys', 'over', 'it', 'greenest', 'seraph', 'our', 'its', 'stood', 'stately', 'there', 'spread', 'monarch', 'angels', 'head', 'good',
            'never', 'half', 'by', 'fabric', 'a', 'reared', 'of', 'radiant', 'tenanted', 'thought', 's', 'so', 'dominion', 'pinion', 'once' ]
        hapax_legomenons = exercises.find_hapax_legomenons( 'data/usher.md' )

        self.assertEqual( ideal, hapax_legomenons )


    # 37. Copy file count
    def test_copy_file_count( self ):

        ideal = "1 O! nothing earthly save the ray\n2 (Thrown back from flowers) of Beauty's eye,"

        # Create file
        exercises.copy_file_count_lines( 'data/short-poem.md' )

        # Read file
        result = open( 'data/output-37.md', 'r' )
        self.assertEqual( result.read(), ideal )


    # 38. Average word length
    def test_average_word_length( self ):

        ideal_average = 3
        average = exercises.average_word_length( 'data/the-dream.md' )

        self.assertEqual( average, ideal_average )


    # 39. Guess the number game
    # def test_guess_the_number_game( self ):
    #     exercises.guess_the_number_game()

    # 40. Anagram
    # def test_anagram_game( self ):

    #     words = [ 'White', 'Blue', 'Red', 'Violet', 'Turquoise', 'Black', 'Yellow' ]
    #     exercises.anagram_game( words )


    # 41, Lingo
    def test_lingo( self ):

        word, guess, spec = 'Tiger', 'Finger', 'F[i]n(g)(e)(r)'
        result = exercises.lingo( word, guess )

        self.assertEqual( result, spec )


    # 43. Anagram
    def test_find_anagrams( self ):
        # result = exercises.find_anagrams( 'data/words-43.md' )
        # print result
        # anagrams = exercises.anagrams()
        # print anagrams

        # Stack
        anagrams = exercises.find_anagrams()
        # print anagrams

    # 44.0 Validate brackets
    def test_validate_brackets( self ):

        string = '[[ [][] ]]'
        validate = exercises.validate_brackets( string )

        self.assertTrue( validate )


    # def test_analyze_brackets( self ):
        # brackets = exercises.analyze_brackets()
        # print brackets


    # 44. Analyze brackets
    # def test_analyze_brackets( self ):
        # brackets = exercises.analyze_brackets()
        # print brackets


# Run
if __name__ == '__main__':
    unittest.main()