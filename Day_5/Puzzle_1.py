from typing import List, Dict
import math


def calculate_seat_location(specification: str, location_range: Dict[str, int], lower_half_character: str) -> int:
    if len(specification) == 1:
        if specification[0] == lower_half_character:
            return location_range['min']
        else:
            return location_range['max']

    if specification[0] == lower_half_character:
        new_max = location_range['min'] + ((location_range['max'] - location_range['min']) // 2)
        new_location_range = {'min': location_range['min'], 'max': new_max}
    else:
        new_min = location_range['min'] + math.ceil((location_range['max'] - location_range['min']) / 2)
        new_location_range = {'min': new_min, 'max': location_range['max']}

    return calculate_seat_location(specification[1:], new_location_range, lower_half_character)


def calculate_seat_id(seat_specification: str) -> int:
    seat_row = calculate_seat_location(seat_specification[:7], {'min': 0, 'max': 127}, 'F')
    seat_column = calculate_seat_location(seat_specification[7:], {'min': 0, 'max': 7}, 'L')

    seat_id = (seat_row * 8) + seat_column

    return seat_id


def find_highest_seat_id(boarding_passes: List[str]) -> int:
    seats_ids_list = map(calculate_seat_id, boarding_passes)

    return max(seats_ids_list)


if __name__ == '__main__':
    from Input_handler import handle_input_for_given_function

    handle_input_for_given_function('puzzle_input.txt', find_highest_seat_id)
