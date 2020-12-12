import unittest
from Day_4 import Puzzle_2


class TestSecondPuzzle(unittest.TestCase):
    def test_validate_required_fields_presence(self):
        passports_with_solutions = (
            # A tuple of (solution, passport)
            (True, "ecl:oth hcl:#602927 eyr:2025 iyr:2013 hgt:151cm byr:1992 pid:812583062"),
            (True, "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm"),
            (True, "hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm"),
            (False, "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929"),
            (False, "hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in")
        )

        for solution, passport in passports_with_solutions:
            with self.subTest("Passport field presence check test", solution=solution, passport=passport):
                self.assertEqual(solution, Puzzle_2.validate_required_fields_presence(passport))

    def test_validate_birth_year(self):
        years_with_solution = (
            # A tuple of (solution, year)
            (True, "1920"),
            (True, "1921"),
            (True, "1943"),
            (True, "2001"),
            (True, "2002"),
            (False, "1919"),
            (False, "1900"),
            (False, "2003"),
            (False, "191a"),
            (False, "191"),
            (False, "191213")
        )

        for solution, year in years_with_solution:
            with self.subTest("Birth year validation test", solution=solution, year=year):
                self.assertEqual(solution, Puzzle_2.validate_birth_year(year))

    def test_validate_issue_year(self):
        years_with_solution = (
            # A tuple of (solution, year)
            (True, "2010"),
            (True, "2011"),
            (True, "2015"),
            (True, "2019"),
            (True, "2020"),
            (False, "2009"),
            (False, "1900"),
            (False, "2021"),
            (False, "202a"),
            (False, "202"),
            (False, "20153")
        )

        for solution, year in years_with_solution:
            with self.subTest("Issue year validation test", solution=solution, year=year):
                self.assertEqual(solution, Puzzle_2.validate_issue_year(year))

    def test_validate_expiration_year(self):
        years_with_solution = (
            # A tuple of (solution, year)
            (True, "2020"),
            (True, "2021"),
            (True, "2025"),
            (True, "2029"),
            (True, "2030"),
            (False, "2019"),
            (False, "2000"),
            (False, "2031"),
            (False, "202a"),
            (False, "202"),
            (False, "20234")
        )

        for solution, year in years_with_solution:
            with self.subTest("Expiration year validation test", solution=solution, year=year):
                self.assertEqual(solution, Puzzle_2.validate_expiration_year(year))

    def test_validate_height_cm(self):
        heights_with_solutions = (
            # A tuple of (solution, height)
            (True, "150cm"),
            (True, "151cm"),
            (True, "178cm"),
            (True, "191cm"),
            (True, "193cm"),
            (False, "149cm"),
            (False, "194cm"),
            (False, "180c"),
            (False, "cm170"),
            (False, "170")
        )

        for solution, height in heights_with_solutions:
            with self.subTest("Height cm validation test", solution=solution, height=height):
                self.assertEqual(solution, Puzzle_2.validate_height(height))

    def test_validate_height_in(self):
        heights_with_solutions = (
            # A tuple of (solution, height)
            (True, "59in"),
            (True, "60in"),
            (True, "69in"),
            (True, "75in"),
            (True, "76in"),
            (False, "58in"),
            (False, "77in"),
            (False, "70i"),
            (False, "in70"),
            (False, ""),
            (False, "70")
        )

        for solution, height in heights_with_solutions:
            with self.subTest("Height in validation test", solution=solution, height=height):
                self.assertEqual(solution, Puzzle_2.validate_height(height))

    def test_validate_hair_color(self):
        colors_with_solution = (
            # A tuple of (solution, color)
            (True, "#012345"),
            (True, "#456789"),
            (True, "#45ae89"),
            (True, "#abcdef"),
            (False, "123456"),
            (False, "1234567"),
            (False, "#abcdef1"),
            (False, "#abcde"),
            (False, "#abcdes")
        )

        for solution, color in colors_with_solution:
            with self.subTest("Hair color validation test", solution=solution, color=color):
                self.assertEqual(solution, Puzzle_2.validate_hair_color(color))

    def test_validate_eye_color(self):
        colors_with_solution = (
            # A tuple of (solution, color)
            (True, "amb"),
            (True, "blu"),
            (True, "brn"),
            (True, "gry"),
            (True, "grn"),
            (True, "hzl"),
            (True, "oth"),
            (False, "mb"),
            (False, "grf"),
            (False, "bl"),
            (False, "blue"),
            (False, "")
        )

        for solution, color in colors_with_solution:
            with self.subTest("Eye color validation test", solution=solution, color=color):
                self.assertEqual(solution, Puzzle_2.validate_eye_color(color))

    def test_validate_passport_id(self):
        ids_with_solution = (
            # A tuple of (solution, id)
            (True, '000000000'),
            (True, '000000324'),
            (True, '012345678'),
            (True, '987654321'),
            (True, '987650000'),
            (False, ''),
            (False, '12345678'),
            (False, '1234567890'),
            (False, '12345678a'),
            (False, 'asnfrtyni'),
        )

        for solution, id in ids_with_solution:
            with self.subTest("Passport id validation test", solution=solution, id=id):
                self.assertEqual(solution, Puzzle_2.validate_passport_id(id))

    def test_parse_passport_to_dictionary(self):
        passports_with_expected_output = (
            # A tuple of (expected_output, passport)
            ({'bry': '1920', 'hgt': '150cm'}, "bry:1920 hgt:150cm"),
            ({'ecl': 'amb', 'pid': '000000001'}, "ecl:amb\n pid:000000001"),
            ({'bry': '1980', 'hgt': '65in', 'ecl': 'blu', 'eyr': '2025'}, "ecl:blu\n eyr:2025 bry:1980\nhgt:65in")
        )

        for expected_output, passport in passports_with_expected_output:
            with self.subTest("Passport to dictionary parse test", expected_output=expected_output, passport=passport):
                self.assertEqual(expected_output, Puzzle_2.parse_passport_to_dictionary(passport))

    def test_count_valid_passports(self):
        self.assertEqual(4, Puzzle_2.count_valid_passports('puzzle_2_test_input.txt'))


if __name__ == '__main__':
    unittest.main()
