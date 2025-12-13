import os


def read_input(file_path: str) -> dict[str, list[str]]:
    data: dict[str, list[str]] = {}

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                device: str = line.split(": ")[0]
                outputs: list[str] = line.split(": ")[1].split(" ")
                data[device] = outputs
    return data


def get_every_path(
    start_device: str, data: dict[str, list[str]]
) -> set[tuple[str, ...]]:
    """_summary_

    Args:
        start_device (str): _description_
        data (dict[str, list[str]]): _description_

    Returns:
        set[tuple[str, ...]]: _description_
    """

    all_paths: set[tuple[str, ...]] = set()

    def dfs(current_device: str, path: list[str]):
        """_summary_

        Args:
            current_device (str): _description_
            path (list[str]): _description_
        """

        path.append(current_device)

        if current_device not in data or not data[current_device]:
            if current_device == "out":
                all_paths.add(tuple(path))
            else:
                return
        else:
            for next_device in data[current_device]:
                dfs(next_device, path.copy())

    dfs(start_device, [])

    return all_paths


def main(data: dict[str, list[str]]) -> int:
    return len(get_every_path("svr", data))


if __name__ == "__main__":
    input_file: str = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "input.txt"
    )
    data: dict[str, list[str]] = read_input(input_file)
    print(f"Part 1: {main(data)}")
