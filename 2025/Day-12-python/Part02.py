from rich.console import Console
from rich.style import Style
from rich.text import Text


def main() -> None:
	URL = "https://adventofcode.com/2025/day/12"
	console = Console()
	STYLE = Style(color="white", link=URL)
	TEXT = Text(
		"See Advent of Code 2025 Day 12 \"problem\".",
		style=STYLE,
	)
	console.print(TEXT)

main()