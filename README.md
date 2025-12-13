# Advent-of-Code

```text
                 | 
                \|/ 
               --*-- 
                >o< 
               >0<<< 
              >>o>>*< 
             >o<<<o<<< 
            >>@>*<<0<<< 
           >o>>@>>>o>o<< 
          >*>>*<o<@<o<<<< 
         >o>o<<<0<*>>*>>0< 
            _ __| |__ _
```

This is my repository for the Advent of Code tasks  
The tasks are found on the [AoC Website](https://adventofcode.com/)

## Setup Day

To create a new day folder with template files and automatically fetch the puzzle input:

```bash
uv run setup_day.py <day> -t <template>
```

Example: `uv run setup_day.py 1 -t python` creates `Day-01-python` folder with template files and downloads the input.

**Template Options:**
- Use `-t python` for Python solutions (default for 2025)
- Use `-t dart` for Dart solutions
- Use `-l` to list all available templates: `uv run setup_day.py -l`

**Authentication:** To automatically fetch inputs, set your session cookie:

- Pass via command line: `-s your_cookie`
- Environment variable: `$env:AOC_SESSION="your_cookie"`
- Or create a `.session` file in the project root

Get your session cookie from browser DevTools after logging in to [adventofcode.com](https://adventofcode.com/).

**Additional Options:**
- Specify year with `-y <year>` (default: current year)  
  Example: `uv run setup_day.py 1 -y 2022 -t python`
- Fetch input only for existing day with `-f` or `--fetch-only`:  
  Example: `uv run setup_day.py 1 -f -t python`

## Run Day

To run a solution for 2025 (which uses a uv workspace):

```bash
cd 2025/Day-XX-python
uv run PartYY.py
```

Example: `cd 2025/Day-12-python` then `uv run Part01.py`

This will automatically install the day's dependencies and execute the solution.
