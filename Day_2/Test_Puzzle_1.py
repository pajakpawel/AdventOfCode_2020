import unittest
from Day_2 import Puzzle_1


class TestFirstPuzzle(unittest.TestCase):
    def test_check_password_validity(self):
        passwords_with_solutions = (
            # A tuple of (password, solution)
            ('0-0 g: asdf', True),
            ('1-1 g: agrs', True),
            ('1-4 g: hjrsgg', True),
            ('1-4 g: hjrsgggg', True),
            ('0-0 g: asdfg', False),
            ('1-1 g: ars', False),
            ('1-4 g: hjrs', False),
            ('1-4 g: hjrsggggg', False)
        )

        for password, solution in passwords_with_solutions:
            with self.subTest("Password validity check test", password=password, solution=solution):
                self.assertEqual(Puzzle_1.check_password_validity(password), solution)

    def test_count_valid_passwords(self):
        datasets_with_solutions = (
            # A tuple of (dataset, solution)
            (['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'], 2),
            (['0-0 g: asdf', '1-4 g: hjrsgggg', '1-1 g: agrs', '0-0 g: asdfg', '1-4 g: hjrsggggg'], 3)
        )

        for dataset, solution in datasets_with_solutions:
            with self.subTest("Counting valid passwords test", dataset=dataset, solution=solution):
                self.assertEqual(Puzzle_1.count_valid_passwords(dataset), solution)


if __name__ == '__main__':
    unittest.main()
