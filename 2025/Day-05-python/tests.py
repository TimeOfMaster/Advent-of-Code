import Part01, Part02, unittest
import os
import tempfile


class TestDay05Part01(unittest.TestCase):
    """Test Part 1: Count how many available ingredient IDs are fresh"""
    
    def setUp(self):
        """Create a temporary test input file"""
        self.test_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        self.temp_file.write(self.test_data)
        self.temp_file.close()
    
    def tearDown(self):
        """Clean up temporary file"""
        os.unlink(self.temp_file.name)
    
    def test_example_case(self):
        """Test the example from the problem description"""
        fresh_ingredients, available_ingredients = Part01.read_input(self.temp_file.name)
        result = Part01.main(fresh_ingredients, available_ingredients)
        self.assertEqual(result, 3, "Should find 3 fresh ingredients (5, 11, 17)")
    
    def test_read_input(self):
        """Test input parsing"""
        fresh_ingredients, available_ingredients = Part01.read_input(self.temp_file.name)
        
        # Check fresh ingredient ranges
        expected_ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]
        self.assertEqual(fresh_ingredients, expected_ranges)
        
        # Check available ingredients
        expected_available = [1, 5, 8, 11, 17, 32]
        self.assertEqual(available_ingredients, expected_available)
    
    def test_is_available_also_fresh(self):
        """Test individual ingredient freshness checking"""
        fresh_ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]
        
        # Test fresh ingredients
        self.assertTrue(Part01.is_availble_also_fresh(5, fresh_ranges), "5 should be fresh (in range 3-5)")
        self.assertTrue(Part01.is_availble_also_fresh(11, fresh_ranges), "11 should be fresh (in range 10-14)")
        self.assertTrue(Part01.is_availble_also_fresh(17, fresh_ranges), "17 should be fresh (in overlapping ranges)")
        
        # Test spoiled ingredients
        self.assertFalse(Part01.is_availble_also_fresh(1, fresh_ranges), "1 should be spoiled")
        self.assertFalse(Part01.is_availble_also_fresh(8, fresh_ranges), "8 should be spoiled")
        self.assertFalse(Part01.is_availble_also_fresh(32, fresh_ranges), "32 should be spoiled")
    
    def test_overlapping_ranges(self):
        """Test that overlapping ranges work correctly"""
        fresh_ranges = [(10, 14), (12, 18)]
        
        # All numbers from 10-18 should be fresh
        for i in range(10, 19):
            self.assertTrue(Part01.is_availble_also_fresh(i, fresh_ranges), 
                          f"{i} should be fresh in overlapping ranges")
        
        # 9 and 19 should be spoiled
        self.assertFalse(Part01.is_availble_also_fresh(9, fresh_ranges))
        self.assertFalse(Part01.is_availble_also_fresh(19, fresh_ranges))
    
    def test_single_number_range(self):
        """Test ranges with single numbers"""
        fresh_ranges = [(5, 5)]
        available = [4, 5, 6]
        
        result = Part01.main(fresh_ranges, available)
        self.assertEqual(result, 1, "Only 5 should be fresh")
    
    def test_empty_available(self):
        """Test with no available ingredients"""
        fresh_ranges = [(1, 10)]
        available = []
        
        result = Part01.main(fresh_ranges, available)
        self.assertEqual(result, 0, "Should return 0 when no ingredients available")


class TestDay05Part02(unittest.TestCase):
    """Test Part 2: Count total fresh ingredient IDs in all ranges"""
    
    def setUp(self):
        """Create a temporary test input file"""
        self.test_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        self.temp_file.write(self.test_data)
        self.temp_file.close()
    
    def tearDown(self):
        """Clean up temporary file"""
        os.unlink(self.temp_file.name)
    
    def test_example_case(self):
        """Test the example from the problem description"""
        fresh_ingredients = Part02.read_input(self.temp_file.name)
        result = Part02.main(fresh_ingredients)
        self.assertEqual(result, 14, "Should find 14 total fresh ingredient IDs")
    
    def test_merge_intervals_no_overlap(self):
        """Test merging intervals with no overlap"""
        intervals = [(1, 3), (5, 7), (9, 10)]
        merged = Part02.merge_intervals(intervals)
        self.assertEqual(merged, [(1, 3), (5, 7), (9, 10)])
    
    def test_merge_intervals_with_overlap(self):
        """Test merging overlapping intervals"""
        intervals = [(10, 14), (12, 18)]
        merged = Part02.merge_intervals(intervals)
        self.assertEqual(merged, [(10, 18)], "Should merge overlapping ranges")
    
    def test_merge_intervals_adjacent(self):
        """Test merging adjacent intervals"""
        intervals = [(1, 3), (4, 6), (7, 9)]
        merged = Part02.merge_intervals(intervals)
        self.assertEqual(merged, [(1, 9)], "Should merge adjacent ranges")
    
    def test_merge_intervals_all_overlap(self):
        """Test the example case merging"""
        intervals = [(3, 5), (10, 14), (16, 20), (12, 18)]
        merged = Part02.merge_intervals(intervals)
        expected = [(3, 5), (10, 20)]
        self.assertEqual(merged, expected, "Should merge to [(3, 5), (10, 20)]")
    
    def test_merge_intervals_unsorted(self):
        """Test that merging works with unsorted input"""
        intervals = [(16, 20), (3, 5), (12, 18), (10, 14)]
        merged = Part02.merge_intervals(intervals)
        expected = [(3, 5), (10, 20)]
        self.assertEqual(merged, expected, "Should handle unsorted input")
    
    def test_merge_intervals_contained(self):
        """Test intervals where one is contained in another"""
        intervals = [(1, 10), (3, 5)]
        merged = Part02.merge_intervals(intervals)
        self.assertEqual(merged, [(1, 10)], "Should merge contained intervals")
    
    def test_single_range(self):
        """Test with a single range"""
        intervals = [(5, 10)]
        result = Part02.main(intervals)
        self.assertEqual(result, 6, "Range 5-10 should contain 6 numbers")
    
    def test_single_number_range(self):
        """Test with a range containing a single number"""
        intervals = [(5, 5)]
        result = Part02.main(intervals)
        self.assertEqual(result, 1, "Single number range should count as 1")
    
    def test_large_range(self):
        """Test with a large range to ensure optimization works"""
        intervals = [(1, 1000000)]
        result = Part02.main(intervals)
        self.assertEqual(result, 1000000, "Should handle large ranges efficiently")
    
    def test_multiple_large_ranges(self):
        """Test multiple large non-overlapping ranges"""
        intervals = [(1, 1000000), (2000000, 3000000)]
        result = Part02.main(intervals)
        self.assertEqual(result, 2000001, "Should sum multiple large ranges")
    
    def test_empty_ranges(self):
        """Test with empty input"""
        intervals = []
        result = Part02.main(intervals)
        self.assertEqual(result, 0, "Empty ranges should return 0")


if __name__ == '__main__':
    unittest.main()
