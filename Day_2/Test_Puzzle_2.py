import unittest
from Day_2 import Puzzle_2


class TestSecondPuzzle(unittest.TestCase):
    def test_check_password_validity(self):
        passwords_with_solutions = (
            # A tuple of (password, solution)
            ('1-2 g: agrs', True),
            ('1-5 g: hjrsgg', True),
            ('1-5 g: ghjrsgg', True),
            ('1-4 g: ghjgsgggg', False),
            ('1-2 g: ars', False),
            ('1-4 g: hjrs', False),
            ('5-8 g: hjrggggg', False)
        )

        for password, solution in passwords_with_solutions:
            with self.subTest("Password validity check test", password=password, solution=solution):
                self.assertEqual(Puzzle_2.check_password_validity(password), solution)

    def test_count_valid_passwords(self):
        datasets_with_solutions = (
            # A tuple of (dataset, solution)
            (['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'], 1),
            (['1-2 g: agrs', '1-4 g: ghjgsgggg', '1-5 g: ghjrsgg', '1-4 g: hjrs'], 2)
        )

        for dataset, solution in datasets_with_solutions:
            with self.subTest("Counting valid passwords test", dataset=dataset, solution=solution):
                self.assertEqual(Puzzle_2.count_valid_passwords(dataset), solution)


if __name__ == '__main__':
    unittest.main()
