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

def find_powers(powers: list[int], i: int, reg_a: int, reg_b: int, reg_c: int, program: list[int]) -> int | None:
    base_reg_a = 0
    for k, p in enumerate(powers):
        base_reg_a += p * pow(8, k)
    for a in range(8):
        reg_a = base_reg_a + a * pow(8, i)
        output = program_output(reg_a, reg_b, reg_c, program)
        if len(output) == len(powers) and output[i] == program[i]:
            if i == 0:
                return reg_a
            powers[i] = a
            result = find_powers(powers, i-1, reg_a, reg_b, reg_c, program) 
            if result is not None:
                return result
    powers[i] = 0
    return None

def main(reg_a: int, reg_b: int, reg_c: int, program: list[int]) -> int:
    i: int = len(program) - 1
    powers: list[int] = [0] * len(program)
    result: int = find_powers(powers, i, reg_a, reg_b, reg_c, program)
    return result

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[int, int, int, list[int]] = read_input(input_file)
    
    reg_a: int = data[0]
    reg_b: int = data[1]
    reg_c: int = data[2]
    program: list[int] = data[3]
    
    print(f"Part 2: {main(reg_a, reg_b, reg_c, program)}")