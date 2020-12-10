import unittest
from Day_3 import Puzzle_2


class TestSecondPuzzle(unittest.TestCase):
    def test_multiply_trees_on_slopes(self):
        terrain_map = """
                        ..##.......
                        #...#...#..
                        .#....#..#.
                        ..#.#...#.#
                        .#...##..#.
                        ..#.##.....
                        .#.#.#....#
                        .#........#
                        #.##...#...
                        #...##....#
                        .#..#...#.#
                      """.split()

        slopes = (
            # A tuple of (right, down)
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
        )

        self.assertEqual(336, Puzzle_2.multiply_trees_on_slopes(terrain_map, slopes))


if __name__ == '__main__':
    unittest.main()
