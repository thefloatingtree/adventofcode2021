with open('day2_input.txt') as f:
    commands = list(map(lambda line: (line.split(' ')[0], int(line.split(' ')[1])), f.readlines()))
    position = [0, 0, 0]

    for command, delta in commands:
        match command:
            case "down":
                position[2] += delta
            case "up":
                position[2] -= delta
            case "forward":
                position[0] += delta
                position[1] += delta * position[2]

    print(position)
    print(position[0] * position[1])
