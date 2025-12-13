import unittest
from shapely.geometry import Polygon
import Part01
import Part02


class TestDay09(unittest.TestCase):
    
    def setUp(self):
        """Set up test data from the problem example."""
        self.example_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
        
        # Parse example data for Part 1
        self.red_tiles = set()
        for line in self.example_input.strip().splitlines():
            x, y = line.split(",")
            self.red_tiles.add((int(x), int(y)))
        
        # Parse example data for Part 2
        self.coords = []
        for line in self.example_input.strip().splitlines():
            x, y = line.split(",")
            self.coords.append((int(x), int(y)))
        self.polygon = Polygon(self.coords)
    
    def test_part1_example(self):
        """Test Part 1 with example input - should find max area of 50."""
        max_area = Part01.get_largest_rect(self.red_tiles)
        self.assertEqual(max_area, 50)
    
    def test_part2_example(self):
        """Test Part 2 with example input - should find max area of 24."""
        max_area = Part02.find_largest_rectangle(self.polygon, self.coords)
        self.assertEqual(max_area, 24)


if __name__ == "__main__":
    unittest.main()
