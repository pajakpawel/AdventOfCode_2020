from typing import List
from Day_5 import Puzzle_1


def find_missing_seat_id(boarding_passes: List[str]) -> int:
    seats_ids_list = list(map(Puzzle_1.calculate_seat_id, boarding_passes))
    seat_id_min = min(seats_ids_list)
    seat_id_max = max(seats_ids_list)

    for seat_id in range(seat_id_min, seat_id_max):
        if seat_id not in seats_ids_list:
            return seat_id


if __name__ == '__main__':
    from Input_handler import handle_input_for_given_function

    handle_input_for_given_function('puzzle_input.txt', find_missing_seat_id)
