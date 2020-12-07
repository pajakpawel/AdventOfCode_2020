from typing import List


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


def count_valid_passwords(passwords_list: List[str]) -> int:
    counter = 0

    for password in passwords_list:
        if check_password_validity(password):
            counter += 1

    return counter


if __name__ == '__main__':
    from Input_handler import handle_input_for_given_function

    handle_input_for_given_function("puzzle_input.txt", count_valid_passwords)
