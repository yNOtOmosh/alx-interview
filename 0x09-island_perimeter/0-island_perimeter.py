#!/usr/bin/python3
"""Island Perimeter"""

def island_perimeter(grid):
    """Initialize perimeter count"""
    perimeter = 0

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                """Check all four directions (up, down, left, right)"""
                if r == 0 or grid[r-1][c] == 0: # Up
                    perimeter += 1
                if r == rows-1 or grid[r+1][c] == 0: # Down
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0: # Left
                    perimeter += 1
                if c == cols-1 or grid[r][c+1] == 0: # Right
                    perimeter += 1

    return perimeter
