import unittest
from anagram import is_anagram

class TestAnagram(unittest.TestCase):
    def test_contain_same_letters(self):
        self.assertTrue(is_anagram("dusty","study"))
    def test_contain_capital_letters(self):
        self.assertTrue(is_anagram("Dusty","Study"))
    def test_contain_punctuation(self):
        self.assertTrue(is_anagram("night!","thing?"))

if __name__ == "__main__":
    unittest.main()