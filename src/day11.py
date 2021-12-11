import numpy as np


class Day11:
    def __init__(self, input="src/input/day11.txt"):
        self.INPUT = input

    def read_input(self):
        with open(self.INPUT, "r") as fp:
            lines = fp.readlines()
            lines = [list(line.strip()) for line in lines]
            return np.array(lines).astype(int)

    def has_flashable(self, grid):
        return np.any(grid > 9)

    def flash(self, grid, row, col):
        adjacent_positions = [
            (row - 1, col - 1),  # top left
            (row - 1, col),  # top middle
            (row - 1, col + 1),  # top right
            (row, col - 1),  # left
            (row, col + 1),  # right
            (row + 1, col - 1),  # bottom left
            (row + 1, col),  # bottom middle
            (row + 1, col + 1),  # bottom right
        ]

        for row, col in adjacent_positions:
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                if grid[row][col] != -1:
                    grid[row][col] += 1

        return grid

    def step(self, grid):
        flashes = 0

        # add 1 to each number
        grid += 1

        # let numbers greater than 9 flash
        while self.has_flashable(grid):
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] > 9:
                        self.flash(grid, row, col)
                        flashes += 1
                        grid[row][col] = -1

        # reset numbers from -1 to 0
        grid = np.where(grid == -1, 0, grid)

        return grid, flashes

    def part1(self):
        grid = self.read_input()

        total_flashes = 0
        for i in range(100):
            grid, flashes = self.step(grid)
            total_flashes += flashes

        return total_flashes

    def part2(self):
        grid = self.read_input()

        step = 0
        flashes = 0
        while flashes != 100:
            grid, flashes = self.step(grid)
            step += 1
        return step

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day11().execute()
