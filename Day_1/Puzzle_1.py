def expense_report_fix(dataset: list) -> int:
    for number_1_index, number_1 in enumerate(dataset):
        for number_2 in dataset[number_1_index + 1:]:
            if number_1 + number_2 == 2020:
                return number_1 * number_2
