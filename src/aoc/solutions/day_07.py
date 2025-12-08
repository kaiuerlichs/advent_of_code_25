def part_1(lines: list[str]) -> str | int:
    count_splits = 0
    lines = [list(line) for line in lines]

    for line_idx in range(len(lines)-1):
        for char_idx in range(len(lines[line_idx])):
            if lines[line_idx][char_idx] == "S" or lines[line_idx][char_idx] == "|":
                if lines[line_idx + 1][char_idx] == "^":
                    count_splits += 1
                    lines[line_idx + 1][char_idx - 1] = "|"
                    lines[line_idx + 1][char_idx + 1] = "|"
                else:
                    lines[line_idx + 1][char_idx] = "|"

        _print_grid(lines)

    return count_splits


def part_2(lines: list[list[str]]) -> str | int:
    tuple_lines = tuple(tuple(line) for line in lines)
    start_char_idx = tuple_lines[0].index("S")
    from functools import cache

    @cache
    def _process_recursively(line_idx: int, char_idx: int) -> int:
        if line_idx == len(tuple_lines) - 1:
            return 1

        if tuple_lines[line_idx][char_idx] == "^":
            return (
                _process_recursively(line_idx + 1, char_idx - 1)
                + _process_recursively(line_idx + 1, char_idx + 1)
            )

        return _process_recursively(line_idx + 1, char_idx)

    return _process_recursively(1, start_char_idx)


def _print_grid(lines: list[list[str]]):
    for line in lines:
        print("".join(line))
    print()