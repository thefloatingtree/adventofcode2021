def main():
    with open("day7_input.txt") as f:
        x_positions = list(map(lambda x: int(x), f.readlines()[0].split(",")))

        answers = []
        for possible_x in range(-max(x_positions), max(x_positions) + 1):
            fuel = 0
            for pos in x_positions:
                fuel += abs(possible_x - pos)
            answers.append((possible_x, fuel))

        print(answers)
        print(min(answers, key=lambda x: x[1]))


main()
