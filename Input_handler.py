from typing import Callable, List, Any


def handle_input_for_given_function(filepath: str, function: Callable[[List[str]], Any]) -> None:
    puzzle_dataset = []
    with open(filepath) as puzzle_input:
        puzzle_dataset = puzzle_input.read().splitlines()
        # for line in puzzle_input.readlines():
        #     puzzle_dataset.append(line)

    solution = function(puzzle_dataset)
    print("Solution for dataset included in '{filepath}' is equal to {solution}".format(filepath=filepath,
                                                                                        solution=solution))
