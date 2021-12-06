class Board:
    def __init__(self):
        self.data = {}
        self.row = 0
        self.column_counts = [0, 0, 0, 0, 0]
        self.row_counts = [0, 0, 0, 0, 0]
        self.unmarked = set()

    def add_line(self, line):
        for column, number in enumerate(map(lambda x: int(x), line.strip().split())):
            self.unmarked.add(number)
            self.data[number] = (column, self.row)
        self.row += 1

    def reveal_number(self, number):
        if number not in self.data.keys():
            return self.check_win()
        self.unmarked.discard(number)
        position = self.data[number]
        self.column_counts[position[0]] += 1
        self.row_counts[position[1]] += 1
        return self.check_win()

    def sum_unmarked(self):
        return sum(self.unmarked)

    def check_win(self):
        return any(x == 5 for x in self.row_counts) or any(
            x == 5 for x in self.column_counts
        )


def main():

    with open("day4_input.txt") as f:
        lines = f.readlines()

        numbers = map(lambda x: int(x), lines[0].strip().split(","))
        board_lines = lines[2:]

        boards = [Board()]
        index = 0
        for line in board_lines:
            if line == "\n":
                boards.append(Board())
                index += 1
                continue
            boards[index].add_line(line)

        for number in numbers:
            # make a copy of the array to iterate on so we can safely call .remove() on the original
            for board in boards[:]:
                if board.reveal_number(number):
                    if len(boards) == 1:
                        print(board.sum_unmarked() * number)
                        return
                    boards.remove(board)


main()
