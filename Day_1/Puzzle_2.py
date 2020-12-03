def expense_report_fix(dataset: list) -> int:
    for number_1_index, number_1 in enumerate(dataset):
        for number_2_index, number_2 in enumerate(dataset[number_1_index + 1:]):
            for number_3 in dataset[number_2_index + 1:]:
                if number_1 + number_2 + number_3 == 2020:
                    return number_1 * number_2 * number_3


if __name__ == '__main__':
    puzzle_dataset = []
    with open("puzzle_input.txt") as puzzle_input:
        for number in puzzle_input.readlines():
            puzzle_dataset.append(int(number))

    print("Solution for dataset included in './puzzle_input.txt' is equal to ", expense_report_fix(puzzle_dataset))