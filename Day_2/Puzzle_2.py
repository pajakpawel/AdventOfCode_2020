def check_password_validity(password: str) -> bool:
    policy_occurrence_indexes, policy_characters, given_password = password.split()

    policy_first_occurrence_index, policy_second_occurrence_index = policy_occurrence_indexes.split('-')
    policy_first_occurrence_index = int(policy_first_occurrence_index)
    policy_second_occurrence_index = int(policy_second_occurrence_index)

    policy_characters = policy_characters.replace(":", "")

    if given_password[policy_first_occurrence_index - 1] == policy_characters:
        if given_password[policy_second_occurrence_index - 1] != policy_characters:
            return True
    elif given_password[policy_second_occurrence_index - 1] == policy_characters:
        return True

    return False


def count_valid_passwords(passwords_list: list) -> int:
    counter = 0

    for password in passwords_list:
        if check_password_validity(password):
            counter += 1

    return counter


if __name__ == '__main__':
    puzzle_dataset = []
    with open("puzzle_input.txt") as puzzle_input:
        for line in puzzle_input.readlines():
            puzzle_dataset.append(line)

    print("Solution for dataset included in './puzzle_input.txt' is equal to ", count_valid_passwords(puzzle_dataset))
