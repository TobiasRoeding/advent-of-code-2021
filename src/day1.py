from src.utils import read_file_as_int_array


class Day1:
    def __init__(self, input="src/input/day1.txt"):
        self.INPUT = input

    def part1(self):
        arr = read_file_as_int_array(self.INPUT)

        prev = float("inf")
        increases = 0
        for current in arr:
            if current > prev:
                increases += 1
            prev = current

        return increases

    def part2(self):
        arr = read_file_as_int_array(self.INPUT)

        prev = float("inf")
        increases = 0
        for i in range(len(arr) - 2):
            s = sum(arr[i : i + 3])
            if s > prev:
                increases += 1
            prev = s

        return increases

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day1().execute()
