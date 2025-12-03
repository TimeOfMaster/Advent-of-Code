import os

def read_input(filename: str) -> tuple[int, int, int, list[int]]:
    lines: list[str] = open(filename).read().split('\n')

    reg_a: int = int(lines[0][12:])
    reg_b: int = int(lines[1][12:])
    reg_c: int = int(lines[2][12:])
    program: list[int] = list(map(int,lines[4][9:].split(',')))

    return reg_a, reg_b, reg_c, program

def combo_op(operand: int, reg_a: int, reg_b: int, reg_c: int) -> int:
    if operand < 4:
        return operand
    if operand == 4:
        return reg_a
    if operand == 5:
        return reg_b
    if operand == 6:
        return reg_c

def program_output(reg_a: int, reg_b: int, reg_c: int, program: list[int]):
    pointer: int = 0
    output: list[int] = []
    while True:
        operator: int = program[pointer]
        operand: int = program[pointer+1]
        
        if operator == 0:
            reg_a = reg_a // (pow(2, combo_op(operand, reg_a, reg_b, reg_c)))
        if operator == 1:
            reg_b = reg_b ^ operand
        if operator == 2:
            reg_b = combo_op(operand, reg_a, reg_b, reg_c) % 8
        if operator == 3:
            if reg_a != 0:
                pointer = operand -2
        if operator == 4:
            reg_b = reg_b ^ reg_c
        if operator == 5:
            output.append(combo_op(operand, reg_a, reg_b, reg_c) % 8)
        if operator == 6:
            reg_b = reg_a // (pow(2, combo_op(operand, reg_a, reg_b, reg_c)))
        if operator == 7:
            reg_c = reg_a // (pow(2, combo_op(operand, reg_a, reg_b, reg_c)))
    
        pointer += 2
        if pointer >= len(program):
            break
    return output

def main(reg_a: int, reg_b: int, reg_c: int, program: list[int]) -> str:
    return ','.join(list(map(str, program_output(reg_a, reg_b, reg_c, program))))

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[int, int, int, list[int]] = read_input(input_file)
    
    reg_a: int = data[0]
    reg_b: int = data[1]
    reg_c: int = data[2]
    program: list[int] = data[3]
    
    print(f"Part 1: {main(reg_a, reg_b, reg_c, program)}")