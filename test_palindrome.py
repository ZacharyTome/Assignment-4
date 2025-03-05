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

      def test_abc(self):
        self.assertFalse(is_palindrome("abc"))

      def test_laval(self):
        self.assertTrue(is_palindrome("laval"))

      def test_toronto(self):
        self.assertFalse(is_palindrome("toronto"))

       def test_able(self):
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))

if __name__ == '__main__':
    unittest.main()
