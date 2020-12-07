from typing import List


def expense_report_fix(dataset: List[str]) -> int:
    dataset = list(map(int, dataset))
    for number_1_index, number_1 in enumerate(dataset):
        for number_2_index, number_2 in enumerate(dataset[number_1_index + 1:]):
            for number_3 in dataset[number_2_index + 1:]:
                if number_1 + number_2 + number_3 == 2020:
                    return number_1 * number_2 * number_3


if __name__ == '__main__':
    from Input_handler import handle_input_for_given_function

    handle_input_for_given_function('puzzle_input.txt', expense_report_fix)
