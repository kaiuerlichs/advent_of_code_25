def part_1(lines: list[str]) -> str | int:
    tokens = [line.split() for line in lines]
    results = []
    for i in range(len(tokens[-1])):
        column = [int(token[i]) for token in tokens[:-1]]
        if tokens[-1][i] == "+":
            results.append(sum(column))
        elif tokens[-1][i] == "*":
            prod = 1
            for num in column:
                prod *= num

            results.append(prod)

    return sum(results)

# Need to run via 'uv run aoc 6 2 full --no-strip'
def part_2(lines: list[str]) -> str | int:
    token_idx = [i for i,val in enumerate(lines[-1]) if val == "+" or val == "*"]
    lines_split = [[] for _ in lines]

    for i in range(len(token_idx)):
        start_idx = token_idx[i]
        end_idx = token_idx[i+1]-1 if i+1 < len(token_idx) else len(lines[-1])
        for j in range(len(lines)):
            lines_split[j].append(lines[j][start_idx:end_idx])

    results = []

    for idx, op in enumerate(lines_split[-1]):
        actual_nums = []
        for i in range(len(op)):
            num_str = ""
            for line in lines_split[:-1]:
                num_str += line[idx][i]
            actual_nums.append(int(num_str))

        if op.strip() == "+":
            results.append(sum(actual_nums))
        elif op.strip() == "*":
            prod = 1
            for num in actual_nums:
                prod *= num
            results.append(prod)

    return sum(results)