import unittest
from Day_5 import Puzzle_1


class TestFirstPuzzle(unittest.TestCase):
    def test_calculate_seat_location_for_rows(self):
        row_specifications_with_solutions = (
            # A tuple of (solution, row_specification)
            (44, 'FBFBBFF'),
            (70, 'BFFFBBF'),
            (14, 'FFFBBBF'),
            (102, 'BBFFBBF')
        )

        for solution, row_specification in row_specifications_with_solutions:
            with self.subTest("Seat location calculate test for rows", solution=solution,
                              row_specification=row_specification):
                self.assertEqual(solution,
                                 Puzzle_1.calculate_seat_location(row_specification, {'min': 0, 'max': 127}, 'F'))

    def test_calculate_seat_location_for_columns(self):
        column_specifications_with_solutions = (
            # A tuple of (solution, column_specification)
            (0, 'LLL'),
            (1, 'LLR'),
            (2, 'LRL'),
            (3, 'LRR'),
            (4, 'RLL'),
            (5, 'RLR'),
            (6, 'RRL'),
            (7, 'RRR')
        )

        for solution, column_specification in column_specifications_with_solutions:
            with self.subTest("Seat location calculate test for columns", solution=solution,
                              column_specification=column_specification):
                self.assertEqual(solution,
                                 Puzzle_1.calculate_seat_location(column_specification, {'min': 0, 'max': 7}, 'L'))

    def test_calculate_seat_id(self):
        seat_specifications_with_solutions = (
            # A tuple of (solution, seat_specification)
            (357, 'FBFBBFFRLR '),
            (567, 'BFFFBBFRRR '),
            (119, 'FFFBBBFRRR '),
            (820, 'BBFFBBFRLL '),
        )

        for solution, seat_specification in seat_specifications_with_solutions:
            with self.subTest("Seat id calculate test", solution=solution, seat_specification=seat_specification):
                self.assertEqual(solution, Puzzle_1.calculate_seat_id(seat_specification))

    def test_find_highest_seat_id(self):
        boarding_passes_with_solutions = (
            # A tuple of (solution, boarding_passes_list)
            (119, ['FFFBBBFRRR']),
            (357, ['FFFBBBFRRR', 'FBFBBFFRLR ']),
            (567, ['FFFBBBFRRR', 'FBFBBFFRLR ', 'BFFFBBFRRR']),
            (820, ['FFFBBBFRRR', 'FBFBBFFRLR ', 'BFFFBBFRRR', 'BBFFBBFRLL']),
        )

        for solution, boarding_passes_list in boarding_passes_with_solutions:
            with self.subTest("Highest seat id finding test", solution=solution,
                              boarding_passes_list=boarding_passes_list):
                self.assertEqual(solution, Puzzle_1.find_highest_seat_id(boarding_passes_list))


if __name__ == '__main__':
    unittest.main()
