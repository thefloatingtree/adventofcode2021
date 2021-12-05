with open('day3_input.txt') as f:
    lines = list(map(lambda line: line.strip(), f.readlines()))

    ones_count = [0] * len(lines[0])
    for line in lines:
        for index, character in enumerate(line):
            ones_count[index] += int(character)

    gamma = ''.join(list(map(lambda count: '1' if count > len(lines) - count else '0', ones_count)))
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

    print(int(gamma, 2) * int(epsilon, 2))