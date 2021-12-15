from parse import findall


class Day13:
    def __init__(self, input="src/input/day13.txt"):
        self.INPUT = input

    def read_input(self):
        instr = open(self.INPUT).read()
        dots = findall("{:d},{:d}", instr)
        folds = findall("{:l}={:d}", instr)
        return dots, folds

    def fold(self, axis, line, dots):
        return {
            (
                min(x, 2 * line - x) if axis == "x" else x,
                min(y, 2 * line - y) if axis == "y" else y,
            )
            for x, y in dots
        }

    def part1(self):
        dots, folds = self.read_input()
        fold = next(folds)
        dots = self.fold(fold[0], fold[1], dots)
        return len(dots)

    def part2(self):
        dots, folds = self.read_input()
        for axis, line in folds:
            dots = {
                (
                    min(x, 2 * line - x) if axis == "x" else x,
                    min(y, 2 * line - y) if axis == "y" else y,
                )
                for x, y in dots
            }

        # print the result
        for y in range(6):
            print(*[" #"[(x, y) in dots] for x in range(40)])

        return len(dots)

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day13().execute()
