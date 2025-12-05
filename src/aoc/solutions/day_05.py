def part_1(lines: list[str]) -> str | int:
    ranges, ids = _get_lines_and_ids(lines)
    count = 0

    for i in ids:
        for r in ranges:
            if i in range(r[0], r[1] + 1):
                count += 1
                break

    return count


def part_2(lines: list[str]) -> str | int:
    input_ranges, _ = _get_lines_and_ids(lines)
    sorted_ranges = sorted(input_ranges, key=lambda x: x[0])
    merged_ranges = [sorted_ranges[0]]

    for iter_range in sorted_ranges[1:]:
        if iter_range[0] <= merged_ranges[-1][1]:
            if iter_range[1] > merged_ranges[-1][1]:
                merged_ranges[-1] = (merged_ranges[-1][0], iter_range[1])
        else:
            merged_ranges.append(iter_range)

    return sum([r[1] - r[0] + 1 for r in merged_ranges])


def _get_lines_and_ids(lines: list[str]):
    ranges = []
    id_start_idx = 0

    for i in range(len(lines)):
        line = lines[i]
        if line == "":
            id_start_idx = i + 1
            break

        range_min, range_max = line.split("-")
        ranges.append((int(range_min), int(range_max)))

    return ranges, [int(lines[i]) for i in range(id_start_idx, len(lines))]