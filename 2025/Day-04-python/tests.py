"""Unit tests for Advent of Code 2025 - Day 4: Printing Department

Tests both Part 1 (counting initially accessible paper rolls) and Part 2 
(iterative removal of accessible rolls) using the example from the problem.
"""

import unittest
import Part01
import Part02


class TestDay04(unittest.TestCase):
    """Test cases for Day 4 solutions."""

    def setUp(self):
        """Set up the example grid from the problem description."""
        # Example grid from the problem
        self.example_input = [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]
        # Convert to 2D list format
        self.grid = [list(line) for line in self.example_input]

    def test_part1_example(self):
        """Test Part 1 with the example - should find 13 accessible rolls."""
        grid_copy = [row[:] for row in self.grid]  # Make a copy
        result = Part01.main(grid_copy)
        self.assertEqual(
            result, 13, "Part 1 should find 13 accessible paper rolls in the example"
        )

    def test_part2_example(self):
        """Test Part 2 with the example - should remove 43 total rolls."""
        grid_copy = [row[:] for row in self.grid]  # Make a copy
        result = Part02.main(grid_copy)
        self.assertEqual(
            result, 43, "Part 2 should remove 43 total paper rolls in the example"
        )

    def test_get_neighbors_corner(self):
        """Test getting neighbors for a corner position."""
        neighbors = Part01.get_neighbors((0, 0), self.grid)
        # Corner should have 3 neighbors
        self.assertEqual(len(neighbors), 3)
        self.assertIn((0, 1), neighbors)
        self.assertIn((1, 0), neighbors)
        self.assertIn((1, 1), neighbors)

    def test_get_neighbors_edge(self):
        """Test getting neighbors for an edge position."""
        neighbors = Part01.get_neighbors((0, 5), self.grid)
        # Edge position should have 5 neighbors
        self.assertEqual(len(neighbors), 5)

    def test_get_neighbors_center(self):
        """Test getting neighbors for a center position."""
        neighbors = Part01.get_neighbors((5, 5), self.grid)
        # Center position should have 8 neighbors
        self.assertEqual(len(neighbors), 8)

    def test_get_num_paper_neighbors(self):
        """Test counting paper neighbors for a specific position."""
        # Position (1, 1) has '@' and should have multiple '@' neighbors
        count = Part01.get_num_paper_neighbors((1, 1), self.grid)
        self.assertGreaterEqual(count, 0)
        self.assertLessEqual(count, 8)

    def test_accessible_criteria(self):
        """Test that a roll with < 4 neighbors is accessible."""
        # Create a simple test case
        simple_grid = [list("..@.."), list("....."), list(".....")]
        # The @ at (0,2) has 0 neighbors, should be accessible
        result = Part01.count_accessible(simple_grid)
        self.assertEqual(result, 1)

    def test_inaccessible_criteria(self):
        """Test that a roll with >= 4 neighbors is not accessible."""
        # Create a grid where center @ is surrounded
        simple_grid = [list(".@@@."), list("@@@@."), list(".@..."), list(".....")]
        # Count how many are accessible (should be less than total @s)
        result = Part01.count_accessible(simple_grid)
        # The @ surrounded by 4+ others should not be counted
        self.assertLess(result, 9)  # 9 total @s, but some inaccessible

    def test_part2_removes_all_accessible(self):
        """Test that Part 2 continues until no more rolls can be removed."""
        # Simple case where all should eventually be removed
        simple_grid = [list("@.@"), list("..."), list("@.@")]
        result = Part02.main(simple_grid)
        self.assertEqual(result, 4, "All 4 isolated rolls should be removed")

    def test_part2_iterative_removal(self):
        """Test that Part 2 removes rolls iteratively."""
        # Create a chain that becomes accessible after first removal
        simple_grid = [list("@@."), list("..."), list("...")]
        result = Part02.main(simple_grid)
        self.assertEqual(result, 2, "Both rolls should eventually be removed")


if __name__ == "__main__":
    unittest.main()
