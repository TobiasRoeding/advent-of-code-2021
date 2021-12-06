from src.utils import read_array_from_file


class Day2:
    def __init__(self, input="input/day2.txt"):
        self.INPUT = input

    @staticmethod
    def part1(input):
        arr = read_array_from_file(input)
        arr = [(a.split(" ")) for a in arr]

        horizontal, depth = 0, 0
        for direction, amount in arr:
            amount = int(amount)

            if direction == "forward":
                horizontal += amount
            elif direction == "up":
                depth -= amount
            elif direction == "down":
                depth += amount

        print(f"horizontal position: {horizontal}, depth: {depth}")

        result = horizontal * depth

        return result

    @staticmethod
    def part2(input):
        arr = read_array_from_file(input)
        arr = [(a.split(" ")) for a in arr]

        horizontal, depth, aim = 0, 0, 0
        for direction, amount in arr:
            amount = int(amount)

            if direction == "forward":
                horizontal += amount
                depth += amount * aim
            elif direction == "up":
                aim -= amount
            elif direction == "down":
                aim += amount

        print(f"horizontal position: {horizontal}, depth: {depth}, aim: {aim}")

        result = horizontal * depth

        return result

    def execute(self):
        print(f"Solution for part 1: {self.part1(self.INPUT)}")
        print(f"Solution for part 2: {self.part2(self.INPUT)}")


if __name__ == "__main__":
    Day2().execute()
