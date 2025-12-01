#!/usr/bin/env python3
"""
Setup script for Advent of Code days.
Creates a new day folder from template and fetches the puzzle input.
"""

import os
import shutil
import sys
from pathlib import Path
import requests

def fetch_input(year: int, day: int, output_path: Path, session_cookie: str | None = None):
    """
    Fetch puzzle input from Advent of Code website.
    
    Args:
        year: The year (e.g., 2025)
        day: The day number (1-25)
        output_path: Path where to save the input file
        session_cookie: Optional session cookie for authentication
    
    Returns:
        bool: True if successful, False otherwise
    """
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    script_dir = Path(__file__).parent
    
    print(f"Fetching input from {input_url}...")
    
    # Try to get session cookie from environment or parameter
    if session_cookie is None:
        session_cookie = os.environ.get('AOC_SESSION')
    
    if session_cookie is None:
        # Try to read from a .session file in the script directory
        session_file = script_dir / ".session"
        if session_file.exists():
            session_cookie = session_file.read_text().strip()
    
    if session_cookie is None:
        print("\nWarning: No session cookie found!")
        print("To automatically fetch inputs, you need to provide your session cookie.")
        print("\nOptions:")
        print("  1. Set AOC_SESSION environment variable")
        print("  2. Create a .session file in the project root")
        print("  3. Pass it as an argument with -s")
        print("\nTo get your session cookie:")
        print("  1. Log in to https://adventofcode.com")
        print("  2. Open browser DevTools (F12)")
        print("  3. Go to Application/Storage > Cookies")
        print("  4. Copy the value of the 'session' cookie")
        print("\nYou can manually download the input and save it to:")
        print(f"  {output_path}")
        return False
    
    # Fetch with session cookie
    headers = {
        'Cookie': f'session={session_cookie}',
        'User-Agent': 'github.com/TimeOfMaster/Advent-of-Code setup script'
    }
    
    try:
        response = requests.get(input_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Check if we got HTML (error page) instead of input
        if response.text.strip().startswith('<!DOCTYPE') or response.text.strip().startswith('<html'):
            print("Error: Received HTML instead of input. Possible issues:")
            print("  - Session cookie may be invalid or expired")
            print("  - Puzzle may not be available yet")
            print("  - You may not have access to this puzzle")
            return False
        
        output_path.write_text(response.text)
        print(f"✓ Input saved to {output_path.name}")
        print(f"  ({len(response.text)} bytes)")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching input: {e}")
        print(f"\nYou can manually download the input from:")
        print(f"  {input_url}")
        print(f"And save it to:")
        print(f"  {output_path}")
        return False

def setup_day(year: int, day: int, session_cookie: str | None = None):
    """
    Set up a new Advent of Code day folder with template files and input.
    
    Args:
        year: The year (e.g., 2025)
        day: The day number (1-25)
        session_cookie: Optional session cookie for authentication
    """
    # Validate inputs
    if not (1 <= day <= 25):
        print(f"Error: Day must be between 1 and 25, got {day}")
        return False
    
    # Define paths
    script_dir = Path(__file__).parent
    year_dir = script_dir / str(year)
    template_dir = year_dir / "template"
    day_folder = year_dir / f"Day-{day:02d}"
    
    # Check if template exists
    if not template_dir.exists():
        print(f"Error: Template directory not found at {template_dir}")
        return False
    
    # Create day folder
    if day_folder.exists():
        response = input(f"Folder {day_folder.name} already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            return False
        shutil.rmtree(day_folder)
    
    print(f"Creating {day_folder.name}...")
    day_folder.mkdir(parents=True, exist_ok=True)
    
    # Copy template files
    for file in template_dir.iterdir():
        if file.is_file() and file.name != '__pycache__':
            dest = day_folder / file.name
            shutil.copy2(file, dest)
            print(f"  Copied {file.name}")
    
    # Fetch input
    input_file = day_folder / "input.txt"
    print()
    fetch_input(year, day, input_file, session_cookie)
    
    return True

def fetch_input_only(year: int, day: int, session_cookie: str | None = None):
    """
    Fetch puzzle input only (without creating day folder).
    
    Args:
        year: The year (e.g., 2025)
        day: The day number (1-25)
        session_cookie: Optional session cookie for authentication
    """
    # Validate inputs
    if not (1 <= day <= 25):
        print(f"Error: Day must be between 1 and 25, got {day}")
        return False
    
    # Define paths
    script_dir = Path(__file__).parent
    year_dir = script_dir / str(year)
    day_folder = year_dir / f"Day-{day:02d}"
    
    # Check if day folder exists
    if not day_folder.exists():
        print(f"Error: Day folder {day_folder} does not exist.")
        print(f"Run without --fetch-only to create the folder first.")
        return False
    
    input_file = day_folder / "input.txt"
    
    # Check if input already exists
    if input_file.exists():
        response = input(f"Input file already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            return False
    
    return fetch_input(year, day, input_file, session_cookie)

def main():
    """Main entry point."""
    import argparse
    from datetime import datetime
    
    current_year = datetime.now().year
    
    parser = argparse.ArgumentParser(
        description='Setup Advent of Code day folder with template and input'
    )
    parser.add_argument('day', type=int, help='Day number (1-25)')
    parser.add_argument('-y', '--year', type=int, default=current_year, 
                       help=f'Year (default: {current_year})')
    parser.add_argument('-s', '--session', type=str,
                       help='Session cookie for authentication')
    parser.add_argument('-f', '--fetch-only', action='store_true',
                       help='Only fetch input (day folder must already exist)')
    
    args = parser.parse_args()
    
    if args.fetch_only:
        print(f"=== Fetching Input for {args.year} Day {args.day} ===\n")
        success = fetch_input_only(args.year, args.day, args.session)
    else:
        print(f"=== Advent of Code {args.year} - Day {args.day} Setup ===\n")
        success = setup_day(args.year, args.day, args.session)
        
        if success:
            print("\n✓ Setup complete!")
            print(f"  cd {args.year}/Day-{args.day:02d}")
    
    if not success:
        print("\n✗ Operation encountered errors.")
        sys.exit(1)

if __name__ == "__main__":
    main()
