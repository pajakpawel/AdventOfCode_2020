import unittest
from Day_5 import Puzzle_2


class TestSecondPuzzle(unittest.TestCase):
    def test_find_missing_seat_id(self):
        boarding_passes_with_solutions = (
            # A tuple of (solution, boarding_passes_list)
            (358, ['FBFBBFFRLR', 'FBFBBFFRRR']),
            (566, ['BFFFBBFRLR', 'BFFFBBFRRR']),
            (120, ['FFFBBBFRRR', 'FFFBBBBLLR']),
        )
        for solution, boarding_passes_list in boarding_passes_with_solutions:
            with self.subTest("Missing seat id finding test", solution=solution,
                              boarding_passes_list=boarding_passes_list):
                self.assertEqual(solution, Puzzle_2.find_missing_seat_id(boarding_passes_list))


if __name__ == '__main__':
    unittest.main()
