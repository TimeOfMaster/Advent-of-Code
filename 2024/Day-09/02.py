import os, unittest

def read_input(filename: str) -> list[int]:
    with open(filename, 'r') as f:
        disk_map: list[int] = [int(x) for x in f.readlines()[0]]
    return disk_map

def checksum(memory: list[int, None]) -> int:
    result: int = 0
    for i, id_num in enumerate(memory):
        if id_num is not None:
            result += i*id_num
    return result

def defrag(memory: list[int, None]) -> list[int, None]:
    p_file: int = len(memory)-1
    id_num = max(x for x in memory if x is not None)
    while id_num >= 0:
        # pull p_file back
        while 0 < p_file and memory[p_file] != id_num:
            p_file -= 1
        if p_file == 0:
            return
        # find size of file
        p_temp = p_file
        while memory[p_temp] == id_num:
            p_temp -= 1
        file_size = p_file - p_temp
        # find first free block to fit file
        for p_free in range(0, p_file-file_size+1):
            if all(memory[p_free + k] is None for k in range(file_size)):
                # move file
                for k in range(file_size):
                    memory[p_free + k], memory[p_file - k] = memory[p_file - k], memory[p_free + k]
                break
        p_file -= file_size
        id_num -= 1

def main(disk_map: list[int]):
    memory: list[int, None] = []
    is_file: bool = True
    id_num: int = 0
    for num in disk_map:
        if is_file:
            for _ in range(num):
                memory.append(id_num)
            id_num += 1
        else:
            for _ in range(num):
                memory.append(None)
        is_file = not is_file
    memory = memory[:]

    defrag(memory)
    return checksum(memory)

class TestDefrag(unittest.TestCase):
    def test_example(self):
        disk_map: list[int] = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]
        expected_checksum: int = 2858
        result: int = main(disk_map)
        self.assertEqual(result, expected_checksum)

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[int] = read_input(input_file)
    
    print(f"Part 2: {main(data)}")
    
    unittest.main()