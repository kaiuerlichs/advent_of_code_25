def part_1(lines: list[str]) -> str | int:
    pos = 50
    count = 0

    for line in lines:
        temp = pos + _operation(line)
        pos = _wrap(temp)
        if pos == 0: count += 1

    return count


def part_2(lines: list[str]) -> str | int:
    pos = 50
    count = 0

    for line in lines:
        op = _operation(line)
        op_mod = (abs(op) % 100) * (-1 if op < 0 else 1)
        count += abs(op) // 100
        count += 1 if pos != 0 and (pos + op_mod > 99 or pos + op_mod <= 0) else 0
        new_pos = _wrap(pos + op)
        pos = new_pos

    return count


def _operation(line):
    line = line.strip()
    amount = int(line[1:])
    direction = -1 if line[0] == 'L' else 1
    return amount * direction


def _wrap(x):
    return x % 100