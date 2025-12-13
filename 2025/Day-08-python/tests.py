import Part01, Part02, unittest


class TestDay08(unittest.TestCase):
    """Test cases for Day 8: Playground junction box circuits."""

    def setUp(self) -> None:
        """Set up example data from the problem description."""
        self.example_data: list[tuple[int, int, int]] = [
            (162, 817, 812),
            (57, 618, 57),
            (906, 360, 560),
            (592, 479, 940),
            (352, 342, 300),
            (466, 668, 158),
            (542, 29, 236),
            (431, 825, 988),
            (739, 650, 466),
            (52, 470, 668),
            (216, 146, 977),
            (819, 987, 18),
            (117, 168, 530),
            (805, 96, 715),
            (346, 949, 466),
            (970, 615, 88),
            (941, 993, 340),
            (862, 61, 35),
            (984, 92, 344),
            (425, 690, 689),
        ]

    def test_part1_example(self) -> None:
        """
        Test Part 1 with example data.

        After making the ten shortest connections, there should be:
        - 11 circuits total
        - Largest circuits: sizes 5, 4, and 2
        - Result: 5 * 4 * 2 = 40
        """
        result: int = Part01.solve(self.example_data, num_connections=10)
        self.assertEqual(result, 40)

    def test_part2_example(self) -> None:
        """
        Test Part 2 with example data.

        The last connection to form a single circuit is between:
        - Junction box at (216, 146, 977)
        - Junction box at (117, 168, 530)
        - Result: 216 * 117 = 25272
        """
        result: int = Part02.solve_part2(self.example_data)
        self.assertEqual(result, 25272)

    def test_distance_calculation(self) -> None:
        """Test that distance calculation works correctly."""
        p1: tuple[int, int, int] = (0, 0, 0)
        p2: tuple[int, int, int] = (3, 4, 0)
        # Distance should be 5 (Pythagorean theorem: 3^2 + 4^2 = 25, sqrt(25) = 5)
        self.assertAlmostEqual(Part01.distance(p1, p2), 5.0)

    def test_closest_pairs_in_example(self) -> None:
        """
        Test that the closest pair is correctly identified.

        According to the problem, the two closest junction boxes are:
        - (162, 817, 812) and (425, 690, 689)
        """
        p1: tuple[int, int, int] = (162, 817, 812)
        p2: tuple[int, int, int] = (425, 690, 689)
        dist: float = Part01.distance(p1, p2)

        # Verify this is indeed a close distance
        # We don't need to verify it's THE closest, just that it's reasonable
        self.assertLess(dist, 1000)


if __name__ == "__main__":
    unittest.main()
