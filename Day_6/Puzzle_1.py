def count_positive_answers(group_answers: str) -> int:
    positive_answers = 0
    counted_questions = set()
    group_answers = ''.join(group_answers.split())

    for answer in group_answers:
        if answer not in counted_questions:
            counted_questions.add(answer)
            positive_answers += 1

    return positive_answers


def count_positive_answers_sum(filepath: str) -> int:
    with open(filepath) as collected_groups_answers:
        answers_per_group = collected_groups_answers.read().split('\n\n')

    positive_answers_per_group = map(count_positive_answers, answers_per_group)

    return sum(positive_answers_per_group)


if __name__ == '__main__':
    solution = count_positive_answers_sum('puzzle_input.txt')
    print("Solution for dataset included in 'puzzle_input.txt' is equal to {solution}".format(solution=solution))
