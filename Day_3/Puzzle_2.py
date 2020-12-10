from typing import List, Tuple
import math


def multiply_trees_on_slopes(terrain_map: List[str], slopes: Tuple[Tuple[int, int], ...]) -> int:
    trees_amount_per_slope = list()
    counter = 0
    position = 0
    max_position = len(terrain_map[0])

    for slope in slopes:
        for line in terrain_map[slope[1]::slope[1]]:
            position += slope[0]
            if position >= max_position:
                position -= max_position
            if line[position] == '#':
                counter += 1

        print(f"Slope: {slope} counter: {counter}")
        trees_amount_per_slope.append(counter)
        counter = 0
        position = 0

    return math.prod(trees_amount_per_slope)


if __name__ == "__main__":
    with open('puzzle_input.txt') as puzzle_input:
        puzzle_dataset = puzzle_input.read().splitlines()

    input_slopes = (
        # A tuple of (right, down)
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    )
    solution = multiply_trees_on_slopes(puzzle_dataset, input_slopes)
    print("Solution for dataset included in 'puzzle_input.txt' is equal to {solution}".format(solution=solution))
