import Part01, Part02
import unittest


class TestFactoryMachines(unittest.TestCase):

    def test_example_case(self) -> None:
        lines: list[str] = [
            "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
            "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
            "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
        ]
        expected_total: int = 7
        result: int = Part01.main(lines)
        self.assertEqual(result, expected_total)

    def test_first_machine(self) -> None:
        """Test just the first machine."""
        lines: list[str] = ["[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"]
        expected_presses: int = 2
        result: int = Part01.main(lines)
        self.assertEqual(result, expected_presses)

    def test_second_machine(self) -> None:
        """Test just the second machine."""
        lines: list[str] = [
            "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}"
        ]
        expected_presses: int = 3
        result: int = Part01.main(lines)
        self.assertEqual(result, expected_presses)

    def test_third_machine(self) -> None:
        """Test just the third machine."""
        lines: list[str] = [
            "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
        ]
        expected_presses: int = 2
        result: int = Part01.main(lines)
        self.assertEqual(result, expected_presses)


class TestFactoryMachines2(unittest.TestCase):

    def test_example_case_part2(self) -> None:
        lines: list[str] = [
            "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
            "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
            "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
        ]
        expected_total: int = 33
        result: int = Part02.main(lines)
        self.assertEqual(result, expected_total)

    def test_first_machine_part2(self) -> None:
        """Test just the first machine - requires 10 button presses."""
        lines: list[str] = ["[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"]
        expected_presses: int = 10
        result: int = Part02.main(lines)
        self.assertEqual(result, expected_presses)

    def test_second_machine_part2(self) -> None:
        """Test just the second machine - requires 12 button presses."""
        lines: list[str] = [
            "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}"
        ]
        expected_presses: int = 12
        result: int = Part02.main(lines)
        self.assertEqual(result, expected_presses)

    def test_third_machine_part2(self) -> None:
        """Test just the third machine - requires 11 button presses."""
        lines: list[str] = [
            "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
        ]
        expected_presses: int = 11
        result: int = Part02.main(lines)
        self.assertEqual(result, expected_presses)


if __name__ == "__main__":
    unittest.main()
