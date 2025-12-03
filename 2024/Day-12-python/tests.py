import Part01, Part02, unittest

class TestPlantPricing(unittest.TestCase):
    def test_part01(self):
        grid: list[str] = [
            list("RRRRIICCFF"),
            list("RRRRIICCCF"),
            list("VVRRRCCFFF"),
            list("VVRCCCJFFF"),
            list("VVVVCJJCFE"),
            list("VVIVCCJJEE"),
            list("VVIIICJJEE"),
            list("MIIIIIJJEE"),
            list("MIIISIJEEE"),
            list("MMMISSJEEE")
        ]
        length: int = len(grid)
        width: int = len(grid[0])
        visited_grid: list[str] = [[0 for _ in range(width)] for _ in range(length)]
        total_price: int = Part01.main(length, width, grid, visited_grid)
        self.assertEqual(total_price, 1930)

    def test_part02(self):
        grid: list[str] = [
            list("RRRRIICCFF"),
            list("RRRRIICCCF"),
            list("VVRRRCCFFF"),
            list("VVRCCCJFFF"),
            list("VVVVCJJCFE"),
            list("VVIVCCJJEE"),
            list("VVIIICJJEE"),
            list("MIIIIIJJEE"),
            list("MIIISIJEEE"),
            list("MMMISSJEEE")
        ]
        length: int = len(grid)
        width: int = len(grid[0])
        visited_grid: list[str] = [[0 for _ in range(width)] for _ in range(length)]
        total_price: int = Part02.main(length, width, grid, visited_grid)
        self.assertEqual(total_price, 1206)

if __name__ == "__main__":
    unittest.main()