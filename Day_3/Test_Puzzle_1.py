import unittest
from Day_3 import Puzzle_1


class TestFirstPuzzle(unittest.TestCase):
    def test_count_trees_on_path(self):
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

        self.assertEqual(Puzzle_1.count_trees_on_path(terrain_map), 7)


if __name__ == '__main__':
    unittest.main()
