import os


def read_input(filename: str) -> tuple[list[tuple[int, int]], list[int]]:
    fresh_ingredients: list[tuple[int, int]] = []
    available_ingredients: list[int] = []

    with open(filename, "r") as f:
        fresh, available = f.read().split("\n\n")

        available_ingredients = [int(x) for x in available.splitlines()]
        for ingredient in fresh.splitlines():
            start, end = ingredient.split("-")
            fresh_ingredients.append((int(start), int(end)))

    return fresh_ingredients, available_ingredients


def is_availble_also_fresh(
    available: int, fresh_ingredients: list[tuple[int, int]]
) -> bool:
    for start, end in fresh_ingredients:
        if start <= available <= end:
            return True
    return False


def main(
    fresh_ingredients: list[tuple[int, int]], available_ingredients: list[int]
) -> int:
    availble_and_fresh: list[int] = []
    for available in available_ingredients:
        if is_availble_also_fresh(available, fresh_ingredients):
            availble_and_fresh.append(available)
    return len(availble_and_fresh)


if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[list[tuple[int, int]], list[int]] = read_input(input_file)

    print(f"Part 1: {main(*data)}")
