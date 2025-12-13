import os
from functools import cache


def read_input(file_path: str) -> dict[str, list[str]]:
    """Read input file and parse device connections."""
    data: dict[str, list[str]] = {}

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                device: str = line.split(": ")[0]
                outputs: list[str] = line.split(": ")[1].split(" ")
                data[device] = outputs
    return data


@cache
def part2(x: str, seen_dac: bool, seen_fft: bool, GRAPH: tuple) -> int:
    """
    Calculate paths from x to 'out' that pass through both 'dac' and 'fft'.

    Args:
        x: Current node
        seen_dac: Whether 'dac' has been seen in the path
        seen_fft: Whether 'fft' has been seen in the path
        graph: Immutable graph representation (tuple of items)

    Returns:
        Number of valid paths
    """
    if x == "out":
        return 1 if seen_dac and seen_fft else 0
    else:
        # Convert graph back to dict for lookup
        graph_dict = dict(GRAPH)
        ans = 0
        for y in graph_dict.get(x, []):
            new_seen_dac = seen_dac or y == "dac"
            new_seen_fft = seen_fft or y == "fft"
            ans += part2(y, new_seen_dac, new_seen_fft, GRAPH)
        return ans


def main(data: dict[str, list[str]]) -> int:
    # Convert dict to tuple of items for caching (lists must be tuples too)
    graph_tuple = tuple((k, tuple(v)) for k, v in data.items())
    return part2("svr", False, False, graph_tuple)


if __name__ == "__main__":
    input_file: str = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "input.txt"
    )
    DATA: dict[str, list[str]] = read_input(input_file)
    result: int = main(DATA)
    print(f"Part 2: {result}")
