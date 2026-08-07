import unittest
from anagram import is_anagram

class TestAnagram(unittest.TestCase):
    def test_contain_same_letters(self):
        self.assertTrue(is_anagram("dusty","study"))

if __name__ == "__main__":
    unittest.main()