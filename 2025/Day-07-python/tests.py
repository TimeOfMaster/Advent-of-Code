"""
Advent of Code 2025 - Day 7: Laboratories
Tests for tachyon manifold beam splitting simulation.

Part 1: Count the total number of times a beam is split in a classical tachyon manifold.
Part 2: Count the number of different timelines in a quantum tachyon manifold using many-worlds interpretation.
"""

import Part01, Part02, unittest


class TestDay07(unittest.TestCase):

    def setUp(self):
        """Set up test data for the example manifold."""
        self.example_input = [
            ".......S.......",
            "...............",
            ".......^.......",
            "...............",
            "......^.^......",
            "...............",
            ".....^.^.^.....",
            "...............",
            "....^.^...^....",
            "...............",
            "...^.^...^.^...",
            "...............",
            "..^...^.....^..",
            "...............",
            ".^.^.^.^.^...^.",
            "...............",
        ]
        self.starting_pos = (0, 7)  # S is at row 0, column 7

    def test_part1_example(self):
        """Test Part 1 with the example input - should return 21 splits."""
        result = Part01.main(self.starting_pos, self.example_input)
        self.assertEqual(result, 21)

    def test_part2_example(self):
        """Test Part 2 with the example input - should return 40 timelines."""
        result = Part02.main(self.starting_pos, self.example_input)
        self.assertEqual(result, 40)


if __name__ == "__main__":
    unittest.main()
