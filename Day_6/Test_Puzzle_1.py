import unittest
from Day_6 import Puzzle_1


class TestFirstPuzzle(unittest.TestCase):
    def test_count_positive_answers(self):
        group_answers = "abcx\nabcy\nabcz"
        self.assertEqual(6, Puzzle_1.count_positive_answers(group_answers))

    def test_count_positive_answers_sum(self):
        self.assertEqual(11, Puzzle_1.count_positive_answers_sum('puzzles_test_input.txt'))


if __name__ == '__main__':
    unittest.main()
