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
    p_free: int = 0
    p_file: int = len(memory)-1
    while True:
        # push p_free forwards
        while p_free < p_file and memory[p_free] is not None:
            p_free += 1
        # pull p_file back
        while p_free < p_file and memory[p_file] is None:
            p_file -= 1
        if p_free >= p_file:
            return memory
        memory[p_free], memory[p_file] = memory[p_file], memory[p_free]

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

    defrag(memory)
    return checksum(memory)

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[int] = read_input(input_file)
    
    print(f"Part 1: {main(data)}")
