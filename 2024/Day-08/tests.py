import Part01, Part02, unittest

class TestAntinodeCalculation(unittest.TestCase):
    def test_example_case(self):
        grid: list[str] = [
            "............",
            "........0...",
            ".....0......",
            ".......0....",
            "....0.......",
            "......A.....",
            "............",
            "............",
            "........A...",
            ".........A..",
            "............",
            "............"
        ]
        length: int = len(grid)
        width: int = len(grid[0])
        expected_antinode_count: int = 14
        result: int = Part01.main(length, width, grid)
        self.assertEqual(result, expected_antinode_count)

    def test_original_example_updated(self):
        grid: list[str] = [
            "............",
            "........0...",
            ".....0......",
            ".......0....",
            "....0.......",
            "......A.....",
            "............",
            "............",
            "........A...",
            ".........A..",
            "............",
            "............"
        ]
        length: int = len(grid)
        width: int = len(grid[0])
        expected_antinode_count: int = 34
        result: int = Part02.main(length, width, grid)
        self.assertEqual(result, expected_antinode_count)

if __name__ == "__main__":
    unittest.main()