from src.utils import read_file_as_int_array


class Day1:
    def __init__(self, input="input/day1.txt"):
        self.INPUT = input

    @staticmethod
    def part1(input):
        arr = read_file_as_int_array(input)

        prev = float("inf")
        increases = 0
        for current in arr:
            if current > prev:
                increases += 1
            prev = current

        return increases

    @staticmethod
    def part2(input):
        arr = read_file_as_int_array(input)

        prev = float("inf")
        increases = 0
        for i in range(len(arr) - 2):
            s = sum(arr[i : i + 3])
            if s > prev:
                increases += 1
            prev = s

        return increases

    def execute(self):
        print(f"Solution for part 1: {self.part1(self.INPUT)}")
        print(f"Solution for part 2: {self.part2(self.INPUT)}")


if __name__ == "__main__":
    Day1().execute()
