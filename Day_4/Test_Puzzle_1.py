import unittest
from Day_4 import Puzzle_1


class TestFirstPuzzle(unittest.TestCase):
    def test_count_valid_passports(self):
        self.assertEqual(3, Puzzle_1.count_valid_passports('puzzle_1_test_input.txt'))


if __name__ == '__main__':
    unittest.main()
