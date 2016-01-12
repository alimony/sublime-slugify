#!/usr/bin/env python3
# encoding: utf-8

'''Run some basic tests on various pieces of text.'''

from __future__ import unicode_literals

if __name__ == '__main__':
    import unittest
    from slugify import slugify

    class TestSlugify(unittest.TestCase):

        def test_empty_string(self):
            test_string = ''
            slug_string = ''
            self.assertEqual(slug_string, slugify(test_string))

        def test_single_char(self):
            test_string = 'a'
            slug_string = 'a'
            self.assertEqual(slug_string, slugify(test_string))

        def test_two_chars(self):
            test_string = 'ab'
            slug_string = 'ab'
            self.assertEqual(slug_string, slugify(test_string))

        def test_two_chars_with_space(self):
            test_string = 'a b'
            slug_string = 'a-b'
            self.assertEqual(slug_string, slugify(test_string))

        def test_three_chars_with_spaces(self):
            test_string = 'a b c'
            slug_string = 'a-b-c'
            self.assertEqual(slug_string, slugify(test_string))

        def test_umlauts(self):
            test_string = 'abc åäö'
            slug_string = 'abc-aao'
            self.assertEqual(slug_string, slugify(test_string))

        def test_sentence(self):
            test_string = 'Flygande bäckasiner söka hwila på mjuka tuvor'
            slug_string = 'flygande-backasiner-soka-hwila-pa-mjuka-tuvor'
            self.assertEqual(slug_string, slugify(test_string))

        def test_unicode(self):
            test_string = '★'
            slug_string = ''
            self.assertEqual(slug_string, slugify(test_string))

        def test_chars_unicode_and_umlauts(self):
            test_string = 'abc åäö ★'
            slug_string = 'abc-aao'
            self.assertEqual(slug_string, slugify(test_string))

        def test_some_punctuation(self):
            test_string = ' a!b"c#d$e&f&g\'h;i:j'
            slug_string = 'a-b-c-d-e-f-g-h-i-j'
            self.assertEqual(slug_string, slugify(test_string))

        def test_multiple_punctuation(self):
            test_string = ' a!:b;"c!!#d;;$e&f:&g\'h;;i::j'
            slug_string = 'a-b-c-d-e-f-g-h-i-j'
            self.assertEqual(slug_string, slugify(test_string))

    unittest.main(argv=['TestSlugify'])
