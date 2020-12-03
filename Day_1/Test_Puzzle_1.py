import unittest
from Day_1 import Puzzle_1


class TestFirstPuzzle(unittest.TestCase):
    def test_expense_report_fix(self):

        datasets_with_solutions = (
            # A tuple of (dataset, solution)
            ([1721, 979, 366, 299, 675, 1456], 514579),
            ([2020, 0], 0),
            ([2030, 5, 1682, -10, 14], -20300)
        )

        for dataset, solution in datasets_with_solutions:
            with self.subTest("Expense report fix correctness for given dataset", dataset=dataset, solution=solution):
                self.assertEqual(Puzzle_1.expense_report_fix(dataset), solution)


if __name__ == '__main__':
    unittest.main()
