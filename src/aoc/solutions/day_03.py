def part_1(lines: list[str]) -> str | int:
    joltages = []
    for line in lines:
        joltages.append(_get_max_joltage(line))
    print(joltages)
    return sum(joltages)


def part_2(lines: list[str]) -> str | int:
    joltages = []
    for line in lines:
        joltages.append(_get_max_joltage_2(line))
    print(joltages)
    return sum(joltages)


def _get_max_joltage(bank: str):
    digit_largest = max(bank[:-1])
    digit_second_largest = max(bank.split(digit_largest, maxsplit=1)[1])
    return int(digit_largest + digit_second_largest)


def _get_max_joltage_2(bank: str):
    digit_count = 12
    digits = []
    for i in range(digit_count):
        digits_to_keep = digit_count - i - 1
        if digits_to_keep == 0:
            max_digit = max(bank)
            digits.append(max_digit)
        else:
            max_digit = max(bank[:-digits_to_keep])
            digits.append(max_digit)
            bank = bank.split(max_digit, maxsplit=1)[1]

    return int(''.join(digits))