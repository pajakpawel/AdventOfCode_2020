def count_group_positive_answers(group_answers: str) -> int:
    positive_answers = 0
    individual_answers_list = group_answers.split()
    first_person_answers = individual_answers_list[0]

    for answer in first_person_answers:
        if all(answer in other_person_answers for other_person_answers in individual_answers_list[1:]):
            positive_answers += 1

    return positive_answers


def sum_up_groups_positive_answers(filepath: str) -> int:
    with open(filepath) as collected_groups_answers:
        answers_per_group = collected_groups_answers.read().split('\n\n')

    positive_answers_per_group = map(count_group_positive_answers, answers_per_group)

    return sum(positive_answers_per_group)


if __name__ == '__main__':
    solution = sum_up_groups_positive_answers('puzzle_input.txt')
    print("Solution for dataset included in 'puzzle_input.txt' is equal to {solution}".format(solution=solution))
