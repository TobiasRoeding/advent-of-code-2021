from typing import List

from src.utils import read_array_from_file


class Day3:
    def __init__(self, input="src/input/day3.txt"):
        self.INPUT = input

    def part1(self):
        arr = read_array_from_file(self.INPUT)

        most_common_bit = ""
        least_common_bit = ""
        for position in range(len(arr[0])):
            result = Day3.check_bits(arr, position)
            if result > 0:
                most_common_bit += "1"
                least_common_bit += "0"
            else:
                most_common_bit += "0"
                least_common_bit += "1"

        gamma_rate = int(most_common_bit, 2)
        epsilon_rate = int(least_common_bit, 2)

        power_consumption = gamma_rate * epsilon_rate

        return power_consumption

    @staticmethod
    def get_numbers(arr: List[str], pos: int, bit: str) -> List[str]:
        numbers = []
        for i in range(len(arr)):
            if arr[i][pos] == bit:
                numbers.append(arr[i])
        return numbers

    @staticmethod
    def check_bits(arr: List[str], pos: int) -> int:
        result = 0
        for a in arr:
            b = a[pos]
            if b == "1":
                result += 1
            else:
                result -= 1
        return result

    @staticmethod
    def find_oxygen_generator_rating(arr):
        pos = 0
        while len(arr) > 1 and pos < len(arr[0]):
            result = Day3.check_bits(arr, pos)
            if result >= 0:
                arr = Day3.get_numbers(arr, pos, "1")
            else:
                arr = Day3.get_numbers(arr, pos, "0")
            pos += 1
        return arr[0]

    @staticmethod
    def find_co2_scrubber_rating(arr):
        pos = 0
        while len(arr) > 1 and pos < len(arr[0]):
            result = Day3.check_bits(arr, pos)
            if result >= 0:
                arr = Day3.get_numbers(arr, pos, "0")
            else:
                arr = Day3.get_numbers(arr, pos, "1")
            pos += 1
        return arr[0]

    def part2(self):
        arr = read_array_from_file(self.INPUT)

        oxygen_generator_rating = int(Day3.find_oxygen_generator_rating(arr), 2)
        co2_scrubber_rating = int(Day3.find_co2_scrubber_rating(arr), 2)
        life_support_rating = oxygen_generator_rating * co2_scrubber_rating

        return life_support_rating

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day3().execute()
