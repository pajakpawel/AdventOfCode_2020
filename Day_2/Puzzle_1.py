def check_password_validity(password: str) -> bool:
    policy_occurrence_range, policy_characters, given_password = password.split()

    policy_min_occurrence, policy_max_occurrence = policy_occurrence_range.split('-')
    policy_min_occurrence = int(policy_min_occurrence)
    policy_max_occurrence = int(policy_max_occurrence)

    policy_characters = policy_characters.replace(":", "")

    if policy_min_occurrence <= given_password.count(policy_characters) <= policy_max_occurrence:
        return True

    return False


def count_valid_passwords(passwords_list: list) -> int:
    counter = 0

    for password in passwords_list:
        if check_password_validity(password):
            counter += 1

    return counter
