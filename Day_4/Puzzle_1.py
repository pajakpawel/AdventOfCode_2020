def count_valid_passports(filepath: str) -> int:
    valid_passports_number = 0
    required_passport_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    with open(filepath) as bach_file:
        passports_list = bach_file.read().split('\n\n')

    for passport in passports_list:
        if all(field in passport for field in required_passport_fields):
            valid_passports_number += 1

    return valid_passports_number


if __name__ == "__main__":
    solution = count_valid_passports('puzzle_input.txt')
    print("Solution for dataset included in 'puzzle_input.txt' is equal to {solution}".format(solution=solution))