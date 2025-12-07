"""
Unit tests for Advent of Code 2025 Day 6: Trash Compactor

Tests both Part 1 (top-to-bottom reading) and Part 2 (right-to-left reading)
using the example worksheet provided in the problem description.
"""

import os
import unittest
import Part01
import Part02


class TestDay06Part1(unittest.TestCase):
    """Test cases for Part 1: Top-to-bottom column reading."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test input file path."""
        cls.test_input = os.path.join(os.path.dirname(__file__), "testinput.txt")
    
    def test_read_input(self):
        """Test that input is correctly parsed into columns."""
        data = Part01.read_input(self.test_input)
        
        # Should have 4 columns (problems)
        self.assertEqual(len(data), 4)
        
        # First column: 123, 45, 6, '*'
        self.assertEqual(data[0], [123, 45, 6, '*'])
        
        # Second column: 328, 64, 98, '+'
        self.assertEqual(data[1], [328, 64, 98, '+'])
        
        # Third column: 51, 387, 215, '*'
        self.assertEqual(data[2], [51, 387, 215, '*'])
        
        # Fourth column: 64, 23, 314, '+'
        self.assertEqual(data[3], [64, 23, 314, '+'])
    
    def test_process_data_multiplication(self):
        """Test processing a multiplication problem: 123 * 45 * 6 = 33210."""
        column_data = [123, 45, 6, '*']
        result = Part01.process_data(column_data)
        self.assertEqual(result, 33210)
    
    def test_process_data_addition(self):
        """Test processing an addition problem: 328 + 64 + 98 = 490."""
        column_data = [328, 64, 98, '+']
        result = Part01.process_data(column_data)
        self.assertEqual(result, 490)
    
    def test_process_data_multiplication_large(self):
        """Test processing a larger multiplication: 51 * 387 * 215 = 4243455."""
        column_data = [51, 387, 215, '*']
        result = Part01.process_data(column_data)
        self.assertEqual(result, 4243455)
    
    def test_process_data_addition_three_numbers(self):
        """Test processing addition with three numbers: 64 + 23 + 314 = 401."""
        column_data = [64, 23, 314, '+']
        result = Part01.process_data(column_data)
        self.assertEqual(result, 401)
    
    def test_main_grand_total(self):
        """Test the grand total from the example: 33210 + 490 + 4243455 + 401 = 4277556."""
        data = Part01.read_input(self.test_input)
        grand_total = Part01.main(data)
        self.assertEqual(grand_total, 4277556)


class TestDay06Part2(unittest.TestCase):
    """Test cases for Part 2: Right-to-left column reading."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test input file path."""
        cls.test_input = os.path.join(os.path.dirname(__file__), "testinput.txt")
    
    def test_read_input(self):
        """Test that input is correctly parsed into columns for right-to-left reading."""
        data = Part02.read_input(self.test_input)
        
        # Should have 4 columns (problems) when reading the worksheet structure
        self.assertEqual(len(data), 4)
        
        # Each column should have 4 elements (3 numbers + 1 operator)
        for col in data:
            self.assertEqual(len(col), 4)
    
    def test_main_grand_total_part2(self):
        """
        Test the grand total from Part 2 example: 1058 + 3253600 + 625 + 8544 = 3263827.
        
        Problems when reading right-to-left:
        - Rightmost problem: 4 + 431 + 623 = 1058 (operator: +)
        - Second from right: 175 * 581 * 32 = 3253600 (operator: *)
        - Third from right: 8 + 248 + 369 = 625 (operator: +)
        - Leftmost problem: 356 * 24 * 1 = 8544 (operator: *)
        
        Grand total: 1058 + 3253600 + 625 + 8544 = 3263827
        """
        data = Part02.read_input(self.test_input)
        grand_total = Part02.main(data)
        self.assertEqual(grand_total, 3263827)


class TestDay06InvalidOperator(unittest.TestCase):
    """Test error handling for invalid operators."""
    
    def test_invalid_operator_part1(self):
        """Test that Part 1 raises ValueError for invalid operators."""
        invalid_data = [10, 20, 30, '!']
        with self.assertRaises(ValueError) as context:
            Part01.process_data(invalid_data)
        self.assertIn("Unknown operator", str(context.exception))


if __name__ == "__main__":
    unittest.main()
