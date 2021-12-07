import numpy as np


class Board:
    def __init__(self, arr):
        self.board = np.array(arr)

    def mark_number(self, number):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == number:
                    self.board[r][c] = "x"

    def get_sum_of_unmarked_numbers(self):
        sum = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] != "x":
                    sum += int(self.board[r][c])
        return sum

    def check_complete(self):
        rows_complete = np.any(np.all(self.board == "x", axis=0))
        columns_complete = np.any(np.all(self.board == "x", axis=1))
        return rows_complete or columns_complete


class Day4:
    def __init__(self, input="src/input/day4.txt"):
        self.INPUT = input

    def read_input(self, input):
        with open(input, "r") as fp:
            # get numbers to draw
            numbers_to_draw = fp.readline().split(",")
            # read empty line
            line = fp.readline()

            boards = []
            while line:
                line = line.strip()
                if not line:
                    board = []
                    for i in range(5):
                        line = fp.readline()
                        line = line.replace("  ", " ")
                        row = line.strip().split(" ")
                        board.append(row)
                    boards.append(board)
                line = fp.readline()

            return numbers_to_draw, boards

    def part1(self):
        numbers_to_draw, arrays = self.read_input(self.INPUT)

        # initalize the boards
        boards = []
        for arr in arrays:
            boards.append(Board(arr))

        # play the game
        for draw in numbers_to_draw:
            for i in range(len(boards)):
                boards[i].mark_number(draw)
                if boards[i].check_complete():
                    return int(draw) * boards[i].get_sum_of_unmarked_numbers()

    def part2(self):
        numbers_to_draw, arrays = self.read_input(self.INPUT)

        # initalize the boards
        boards = []
        for arr in arrays:
            boards.append(Board(arr))

        # play the game
        winning_boards = set()
        for draw in numbers_to_draw:
            for i in range(len(boards)):
                boards[i].mark_number(draw)
                if boards[i].check_complete():
                    if i not in winning_boards:
                        winning_boards.add(i)
                        if len(winning_boards) == len(boards):
                            return int(draw) * boards[i].get_sum_of_unmarked_numbers()

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day4().execute()
