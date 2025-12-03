import Part01, Part02, unittest

class TestClawContraption(unittest.TestCase):
    def test_part01(self):
        data: list[str] = [
            "Button A: X+94, Y+34",
            "Button B: X+22, Y+67",
            "Prize: X=8400, Y=5400",
            "",
            "Button A: X+26, Y+66",
            "Button B: X+67, Y+21",
            "Prize: X=12748, Y=12176",
            "",
            "Button A: X+17, Y+86",
            "Button B: X+84, Y+37",
            "Prize: X=7870, Y=6450",
            "",
            "Button A: X+69, Y+23",
            "Button B: X+27, Y+71",
            "Prize: X=18641, Y=10279"
        ]
        total_tokens: int = Part01.main(data)
        self.assertEqual(total_tokens, 480)

    def test_part02(self): # i don't know the correct output but 0
        data: list[str] = [
            "Button A: X+94, Y+34",
            "Button B: X+22, Y+67",
            "Prize: X=10000000008400, Y=10000000005400",
            "",
            "Button A: X+26, Y+66",
            "Button B: X+67, Y+21",
            "Prize: X=10000000012748, Y=10000000012176",
            "",
            "Button A: X+17, Y+86",
            "Button B: X+84, Y+37",
            "Prize: X=10000000007870, Y=10000000006450",
            "",
            "Button A: X+69, Y+23",
            "Button B: X+27, Y+71",
            "Prize: X=10000000018641, Y=10000000010279"
        ]
        total_tokens: int = Part02.main(data)
        self.assertEqual(total_tokens, 0)

if __name__ == "__main__":
    unittest.main()