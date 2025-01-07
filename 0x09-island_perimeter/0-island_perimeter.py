#!/usr/bin/python3
"""0x09-island_perimeter"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    The grid consists of 0s (water) and 1s (land).
    Each land cell contributes 4 to the perimeter,
    but adjacent land cells reduce the total perimeter
    by 2 for each shared edge.

    Args:
        grid (list of list of int): A 2D list representing
        the island grid.

    Returns:
        int: The total perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4  # Each land cell contributes 4 to the perimeter

                # Check adjacent cells and subtract 2 for each shared edge
                if r > 0 and grid[r - 1][c] == 1:  # Check cell above
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Check cell to the left
                    perimeter -= 2

    return perimeter
