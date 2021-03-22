import unittest
from Day_6 import Puzzle_2


class TestSecondPuzzle(unittest.TestCase):
    def test_count_group_positive_answers(self):
        group_answers = "abcx\nabcy\nabcz"
        self.assertEqual(3, Puzzle_2.count_group_positive_answers(group_answers))

    def test_sum_up_groups_positive_answers(self):
        self.assertEqual(6, Puzzle_2.sum_up_groups_positive_answers('puzzles_test_input.txt'))


if __name__ == '__main__':
    unittest.main()
