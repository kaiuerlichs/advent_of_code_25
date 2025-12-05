def part_1(lines: list[str]) -> str | int:
    grid = _generate_grid(lines)
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                adjacent_rolls = _count_adjacent_rolls(grid, row, col)
                if adjacent_rolls < 4:
                    count +=1
    return count


def part_2(lines: list[str]) -> str | int:
    grid = _generate_grid(lines)
    global_count = 0
    while True:
        _print_grid(grid)
        local_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    adjacent_rolls = _count_adjacent_rolls(grid, row, col)
                    if adjacent_rolls < 4:
                        local_count +=1
                        grid[row][col] = False

        global_count += local_count

        if local_count == 0:
            break

    return global_count


def _generate_grid(lines: list[str]) -> list[list[bool]]:
    grid = []
    for line in lines:
        grid.append([True if c == "@" else False for c in line])
    return grid


def _count_adjacent_rolls(grid: list[list[bool]], row: int, col: int) -> int:
    directions = [
        (-1, -1),   (-1, 0),    (-1, 1),
        (0, -1),                (0, 1),
        (1, -1),    (1, 0),     (1, 1),
    ]
    count = 0
    for dx, dy in directions:
        x, y = row + dx, col + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]:
            count += 1
    return count

def _print_grid(grid: list[list[bool]]):
    for row in grid:
        print(["@" if cell else "." for cell in row])