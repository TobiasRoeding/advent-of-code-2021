from collections import defaultdict


class Day6:
    def __init__(self, input="src/input/day6.txt"):
        self.INPUT = input

    def read_input(self):
        numbers = defaultdict(int)
        with open(self.INPUT, "r") as fp:
            line = fp.readline().split(",")
            for number in line:
                numbers[int(number)] += 1
        return numbers

    def simulate(self, numbers, days):
        for _ in range(days):
            new_numbers = defaultdict(int)

            for k in numbers.keys():
                if k == 0:
                    new_numbers[8] += numbers[0]
                    new_numbers[6] += numbers[0]
                else:
                    new_numbers[k - 1] += numbers[k]
            numbers = new_numbers
        return numbers

    def part1(self, days):
        numbers = self.read_input()
        final_numbers = self.simulate(numbers, days)
        sum = 0
        for k in final_numbers.keys():
            sum += final_numbers[k]
        return sum

    def part2(self, days):
        return self.part1(days)

    def execute(self):
        print(f"Solution for part 1: {self.part1(80)}")
        print(f"Solution for part 2: {self.part2(256)}")


if __name__ == "__main__":
    Day6().execute()
