import unittest
from palindrome import is_palindrome

class PalindromeTest(unittest.TestCase):

      def test_non_string(self):
        with self.assertRaises(ValueError):
            is_palindrome(12345)

      def test_empty_string(self):
        self.assertFalse(is_palindrome(""))

      def test_a(self):
        self.assertTrue(is_palindrome("a"))
      
      def test_bb(self):
        self.assertTrue(is_palindrome("bb"))    
