def part_1(lines: list[str]) -> str | int:
    ranges = _parse_input(lines[0])
    ids = []

    for r in ranges:
        start, end = r
        for i in range(start, end+1):
            str_id = str(i)
            id_len = len(str_id)
            if id_len % 2 == 0 and str_id[0:id_len//2] == str_id[id_len//2:]:
                ids.append(i)

    return sum(ids)


def part_2(lines: list[str]) -> str | int:
    ranges = _parse_input(lines[0])
    ids = []

    for r in ranges:
        start, end = r
        for i in range(start, end+1):
            if _check_for_patterns(i):
                ids.append(i)

    return sum(ids)


def _parse_input(line:str) -> list[tuple[int, int]]:
    ranges = line.split(",")
    range_tuples = []
    for r in ranges:
        start, end = r.split("-")
        range_tuples.append((int(start), int(end)))
    return range_tuples


def _check_for_patterns(id: int) -> bool:
    str_id = str(id)
    len_id = len(str_id)
    for i in range(len_id-1):
        if len_id % (i+1) != 0: continue
        segments = [str_id[j:j+i+1] for j in range(0, len_id, i+1)]
        if all(s==segments[0] for s in segments): return True
    return False