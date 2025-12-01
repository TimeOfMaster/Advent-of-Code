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
uv run setup_day.py <day>
```

Example: `uv run setup_day.py 1` creates `Day-01` folder with template files and downloads the input.

**Authentication:** To automatically fetch inputs, set your session cookie:

- Pass via command line: `-s your_cookie`
- Environment variable: `$env:AOC_SESSION="your_cookie"`
- Or create a `.session` file in the project root

Get your session cookie from browser DevTools after logging in to [adventofcode.com](https://adventofcode.com/).
