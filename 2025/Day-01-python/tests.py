import Part01, Part02, unittest


class TestDialRotation(unittest.TestCase):

    def test_part1_example(self):
        """Test Part 1 with the example from the puzzle"""
        data: list[str] = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]
        expected_password: int = 3
        result: int = Part01.main(data)
        self.assertEqual(result, expected_password)

    def test_part2_example(self):
        """Test Part 2 with the example from the puzzle"""
        data: list[str] = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]
        expected_password: int = 6
        result: int = Part02.main(data)
        self.assertEqual(result, expected_password)

    def test_part2_large_rotation(self):
        """Test Part 2 with a large rotation like R1000 from position 50"""
        data: list[str] = ["R1000"]
        expected_password: int = 10  # Should pass through 0 ten times
        result: int = Part02.main(data)
        self.assertEqual(result, expected_password)

    def test_part1_simple_rotation(self):
        """Test Part 1 with simple rotations"""
        data: list[str] = ["R50"]  # From 50, R50 should land on 0
        expected_password: int = 1
        result: int = Part01.main(data)
        self.assertEqual(result, expected_password)

    def test_part2_simple_rotation(self):
        """Test Part 2 with simple rotations"""
        data: list[str] = ["R50"]  # From 50, R50 should hit 0 once
        expected_password: int = 1
        result: int = Part02.main(data)
        self.assertEqual(result, expected_password)


if __name__ == "__main__":
    unittest.main()
