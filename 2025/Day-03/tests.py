import Part01, Part02, unittest


class TestPart01(unittest.TestCase):
    def test_example_banks(self):
        """Test Part 1 examples from the problem description."""
        # 987654321111111 -> 98 (first two batteries)
        self.assertEqual(Part01.activate_batteries([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1]), 98)
        
        # 811111111111119 -> 89 (batteries 8 and 9)
        self.assertEqual(Part01.activate_batteries([8,1,1,1,1,1,1,1,1,1,1,1,1,1,9]), 89)
        
        # 234234234234278 -> 78 (last two batteries)
        self.assertEqual(Part01.activate_batteries([2,3,4,2,3,4,2,3,4,2,3,4,2,7,8]), 78)
        
        # 818181911112111 -> 92 (batteries 9 and 2)
        self.assertEqual(Part01.activate_batteries([8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]), 92)
    
    def test_total_joltage(self):
        """Test total joltage calculation for all example banks."""
        data = [
            [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],
            [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9],
            [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8],
            [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]
        ]
        # 98 + 89 + 78 + 92 = 357
        self.assertEqual(Part01.main(data), 357)


class TestPart02(unittest.TestCase):
    def test_example_banks(self):
        """Test Part 2 examples from the problem description."""
        # 987654321111111 -> 987654321111 (everything except some 1s at the end)
        self.assertEqual(Part02.activate_batteries([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1]), 987654321111)
        
        # 811111111111119 -> 811111111119 (everything except some 1s)
        self.assertEqual(Part02.activate_batteries([8,1,1,1,1,1,1,1,1,1,1,1,1,1,9]), 811111111119)
        
        # 234234234234278 -> 434234234278 (skip 2, 3, 2 near start)
        self.assertEqual(Part02.activate_batteries([2,3,4,2,3,4,2,3,4,2,3,4,2,7,8]), 434234234278)
        
        # 818181911112111 -> 888911112111 (skip some 1s near front)
        self.assertEqual(Part02.activate_batteries([8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]), 888911112111)
    
    def test_total_joltage(self):
        """Test total joltage calculation for all example banks."""
        data = [
            [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],
            [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9],
            [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8],
            [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]
        ]
        # 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619
        self.assertEqual(Part02.main(data), 3121910778619)


if __name__ == "__main__":
    unittest.main()
