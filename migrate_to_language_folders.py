#!/usr/bin/env python3
"""
Migration script to rename existing day folders to include language suffix.
Renames Day-XX to Day-XX-python for all existing Python solutions.
"""

import os
import sys
from pathlib import Path
import shutil

def find_day_folders(year_dir: Path) -> list[Path]:
    """
    Find all day folders without language suffix in a year directory.
    
    Args:
        year_dir: Path to the year directory
    
    Returns:
        List of day folder paths that need migration
    """
    folders = []
    if not year_dir.exists() or not year_dir.is_dir():
        return folders
    
    for item in year_dir.iterdir():
        if item.is_dir() and item.name.startswith('Day-'):
            # Check if it doesn't already have a language suffix
            # Format: Day-XX (needs migration) vs Day-XX-python (already migrated)
            parts = item.name.split('-')
            if len(parts) == 2 and parts[1].isdigit():
                folders.append(item)
    
    return sorted(folders)

def migrate_folder(folder: Path, language: str = 'python', dry_run: bool = False) -> bool:
    """
    Migrate a single day folder to include language suffix.
    
    Args:
        folder: Path to the folder to migrate
        language: Language suffix to add
        dry_run: If True, only print what would be done
    
    Returns:
        True if successful, False otherwise
    """
    new_name = f"{folder.name}-{language}"
    new_path = folder.parent / new_name
    
    if new_path.exists():
        print(f"  ⚠ Skipping {folder.name}: {new_name} already exists")
        return False
    
    if dry_run:
        print(f"  Would rename: {folder.name} → {new_name}")
        return True
    
    try:
        folder.rename(new_path)
        print(f"  ✓ Renamed: {folder.name} → {new_name}")
        return True
    except Exception as e:
        print(f"  ✗ Error renaming {folder.name}: {e}")
        return False

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Migrate existing day folders to include language suffix'
    )
    parser.add_argument('-y', '--year', type=int, action='append',
                       help='Year(s) to migrate (can be specified multiple times). If not provided, migrates all years.')
    parser.add_argument('-l', '--language', type=str, default='python',
                       help='Language suffix to add (default: python)')
    parser.add_argument('-d', '--dry-run', action='store_true',
                       help='Show what would be done without making changes')
    parser.add_argument('--skip-template', action='store_true',
                       help='Skip template folders during migration')
    
    args = parser.parse_args()
    
    script_dir = Path(__file__).parent
    
    # Determine which years to process
    if args.year:
        years = args.year
    else:
        # Find all year directories
        years = [int(item.name) for item in script_dir.iterdir() 
                if item.is_dir() and item.name.isdigit()]
        years.sort()
    
    if not years:
        print("No year directories found.")
        return
    
    print("=== Advent of Code Folder Migration ===\n")
    if args.dry_run:
        print("DRY RUN MODE - No changes will be made\n")
    
    total_migrated = 0
    total_skipped = 0
    
    for year in years:
        year_dir = script_dir / str(year)
        if not year_dir.exists():
            print(f"Year {year}: Directory not found, skipping")
            continue
        
        folders = find_day_folders(year_dir)
        
        if not folders:
            print(f"Year {year}: No folders to migrate")
            continue
        
        print(f"Year {year}: Found {len(folders)} folder(s) to migrate")
        
        for folder in folders:
            # Skip template folders if requested
            if args.skip_template and 'template' in folder.name.lower():
                continue
            
            success = migrate_folder(folder, args.language, args.dry_run)
            if success:
                total_migrated += 1
            else:
                total_skipped += 1
        
        print()
    
    # Summary
    print("=== Migration Summary ===")
    if args.dry_run:
        print(f"Would migrate: {total_migrated} folder(s)")
        print(f"Would skip: {total_skipped} folder(s)")
        print("\nRun without --dry-run to perform the migration.")
    else:
        print(f"Migrated: {total_migrated} folder(s)")
        print(f"Skipped: {total_skipped} folder(s)")
        if total_migrated > 0:
            print("\n✓ Migration complete!")

if __name__ == "__main__":
    main()
