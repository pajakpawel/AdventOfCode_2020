import unittest
from Day_1 import Puzzle_2


class TestSecondPuzzle(unittest.TestCase):
    def test_expense_report_fix(self):

        datasets_with_solutions = (
            # A tuple of (dataset, solution)
            ([1721, 979, 366, 299, 675, 1456], 241861950),
            ([2020, 0, 0], 0),
            ([2030, 5, 1682, -15, 14], -152250)
        )

        for dataset, solution in datasets_with_solutions:
            with self.subTest("Expense report fix correctness for given dataset", dataset=dataset, solution=solution):
                self.assertEqual(Puzzle_2.expense_report_fix(dataset), solution)


if __name__ == '__main__':
    unittest.main()
