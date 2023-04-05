import unittest
from palindrome import is_palindrome


class TestStringMethods(unittest.TestCase):

    def test_even_palindrome_4_ch(self):
        self.assertEqual(is_palindrome("abba"), True)

    def test_even_non_palindrome_2_ch(self):
        self.assertEqual(is_palindrome("no"), False)

    def test_even_palindrome_repeated_ch(self):
        self.assertEqual(is_palindrome("pp"), True)

    def test_odd_palindrome_repeated_ch(self):
        self.assertEqual(is_palindrome("xxx"), True)

    def test_odd_palindrome_1_ch(self):
        self.assertEqual(is_palindrome("c"), True)

    def test_odd_palindrome_3_ch(self):
        self.assertEqual(is_palindrome("asa"), True)

    def test_even_palindrome_10_ch(self):
        self.assertEqual(is_palindrome("cisabbasic"), True)

    def test_odd_non_palindrome_15_ch(self):
        self.assertEqual(is_palindrome("onionsandgarlic"), False)

    def test_even_non_palindrome_18_ch(self):
        self.assertEqual(is_palindrome("evencharactercount"), False)


if __name__ == '__main__':
    unittest.main()
