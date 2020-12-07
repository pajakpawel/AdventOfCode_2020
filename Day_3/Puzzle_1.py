from typing import List


def count_trees_on_path(terrain_map: List[str]) -> int:
    counter = 0
    position = 0
    max_position = len(terrain_map[0])

    for line in terrain_map[1:]:
        position += 3
        if position >= max_position:
            position -= max_position
        if line[position] == '#':
            counter += 1

    return counter


if __name__ == '__main__':
    from Input_handler import handle_input_for_given_function

    handle_input_for_given_function('puzzle_input.txt', count_trees_on_path)
