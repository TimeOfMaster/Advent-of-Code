import os


def read_input(filename: str) -> list[tuple[int, int]]:
    fresh_ingredients: list[tuple[int, int]] = []

    with open(filename, "r") as f:
        fresh, available = f.read().split("\n\n")

        for ingredient in fresh.splitlines():
            start, end = ingredient.split("-")
            fresh_ingredients.append((int(start), int(end)))

    return fresh_ingredients


def get_fresh_set(fresh_ingredients: list[tuple[int, int]]) -> set[int]:
    fresh_set: set[int] = set()
    for start, end in fresh_ingredients:
        for i in range(start, end + 1):
            fresh_set.add(i)
    return fresh_set


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []

    # Sort by start position
    sorted_intervals = sorted(intervals)
    merged = [sorted_intervals[0]]

    for current in sorted_intervals[1:]:
        last = merged[-1]
        # Check if intervals overlap or are adjacent
        if current[0] <= last[1] + 1:
            # Merge by extending the end
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)

    return merged


def main(fresh_ingredients: list[tuple[int, int]]) -> int:
    merged = merge_intervals(fresh_ingredients)
    # Sum up the lengths of all merged intervals
    return sum(end - start + 1 for start, end in merged)


if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[tuple[int, int]] = read_input(input_file)

    print(f"Part 2: {main(data)}")
