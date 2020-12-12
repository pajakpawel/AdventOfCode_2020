def validate_required_fields_presence(passport: str) -> bool:
    required_passport_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    if all(field in passport for field in required_passport_fields):
        return True

    return False


def validate_birth_year(birth_year: str) -> bool:
    if len(birth_year) == 4 and birth_year.isdigit():
        year = int(birth_year)
        if 1920 <= year <= 2002:
            return True

    return False


def validate_issue_year(issue_year: str) -> bool:
    if len(issue_year) == 4 and issue_year.isdigit():
        year = int(issue_year)
        if 2010 <= year <= 2020:
            return True

    return False


def validate_expiration_year(expiration_year: str) -> bool:
    if len(expiration_year) == 4 and expiration_year.isdigit():
        year = int(expiration_year)
        if 2020 <= year <= 2030:
            return True

    return False


def validate_height(height: str) -> bool:
    number = height[:-2]
    unit = height[-2:]

    if number.isdigit():
        number = int(number)
        if unit == "cm" and 150 <= number <= 193:
            return True
        if unit == "in" and 59 <= number <= 76:
            return True

    return False


def validate_hair_color(hair_color: str) -> bool:
    if hair_color[0] == "#" and len(hair_color) == 7:
        for character in hair_color[1:]:
            if character.isdigit():
                continue
            if not 'a' <= character <= 'f':
                return False
        return True

    return False


def validate_eye_color(eye_color: str) -> bool:
    allowed_eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if eye_color in allowed_eye_colors:
        return True

    return False


def validate_passport_id(passport_id: str) -> bool:
    if passport_id.isdigit() and len(passport_id) == 9:
        return True

    return False


def parse_passport_to_dictionary(passport: str) -> dict:
    fields_with_values_string_list = passport.split()
    fields_with_values_dictionary = {}

    for field_with_value in fields_with_values_string_list:
        field, value = field_with_value.split(':')
        fields_with_values_dictionary[field] = value

    return fields_with_values_dictionary


def count_valid_passports(filepath: str) -> int:
    valid_passports_number = 0

    with open(filepath) as bach_file:
        passports_list = bach_file.read().split('\n\n')

    for passport in passports_list:
        if validate_required_fields_presence(passport):
            passport_fields_validity = []
            passport_dictionary = parse_passport_to_dictionary(passport)

            passport_fields_validity.append(validate_birth_year(passport_dictionary['byr']))
            passport_fields_validity.append(validate_issue_year(passport_dictionary['iyr']))
            passport_fields_validity.append(validate_expiration_year(passport_dictionary['eyr']))
            passport_fields_validity.append(validate_height(passport_dictionary['hgt']))
            passport_fields_validity.append(validate_hair_color(passport_dictionary['hcl']))
            passport_fields_validity.append(validate_eye_color(passport_dictionary['ecl']))
            passport_fields_validity.append(validate_passport_id(passport_dictionary['pid']))

            if all(passport_fields_validity):
                valid_passports_number += 1

    return valid_passports_number


if __name__ == "__main__":
    solution = count_valid_passports('puzzle_input.txt')
    print("Solution for dataset included in 'puzzle_input.txt' is equal to {solution}".format(solution=solution))
