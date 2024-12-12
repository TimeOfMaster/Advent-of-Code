import Part01, Part02, unittest

class TestDefrag(unittest.TestCase):

    def test_Part01_example_checksum(self):
        # Example disk map: "2333133121414131402"
        disk_map: list[int] = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]
        expected_checksum: int = 1928
        self.assertEqual(Part01.main(disk_map), expected_checksum)

    def test_Part02_example_checksum(self):
        # Example disk map: "2333133121414131402"
        disk_map: list[int] = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]
        expected_checksum: int = 2858
        result: int = Part02.main(disk_map)
        self.assertEqual(result, expected_checksum)
    
if __name__ == "__main__":
    unittest.main()