import itertools


class Day8:
    """
      aaaa
    b      c
    b      c
      dddd
    e      f
    e      f
      gggg
    """

    UNIQUE_LENGTH_DIGITS = [2, 4, 3, 7]
    ALL_SEGMENTS = "abcdefg"
    DIGIT_SEGMENTS = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]

    def __init__(self, input="src/input/day8.txt"):
        self.INPUT = input

    def read_input(self):
        with open(self.INPUT, "r") as fp:
            lines = fp.readlines()
            notes = []
            for line in lines:
                observations, digits = line.strip().split(" | ")
                observations = observations.split(" ")
                digits = digits.split(" ")
                notes.append([observations, digits])
        return notes

    def part1(self):
        notes = self.read_input()

        count = 0
        for entry in notes:
            digits = entry[1]
            for digit in digits:
                if len(digit) in self.UNIQUE_LENGTH_DIGITS:
                    count += 1

        return count

    def get_digit(self, segments):
        try:
            return self.DIGIT_SEGMENTS.index("".join(sorted(segments)))
        except ValueError:
            return None

    def could_be_digit(self, segments):
        return self.get_digit(segments) is not None

    def permute(self, segments, permutation_dict):
        return "".join([permutation_dict[s] for s in segments])

    def get_permutations(self, segments):
        permutations = itertools.permutations(segments)
        permutations = [{a: b for a, b in zip(segments, p)} for p in permutations]
        return permutations

    def part2(self):
        notes = self.read_input()

        # generate all possible permutations of segment mappings
        permutations = self.get_permutations(self.ALL_SEGMENTS)

        unscrambled_digits = []
        for observations, digits in notes:
            for permutation in permutations:
                # permute observations using current permutation
                permuted = [self.permute(o, permutation) for o in observations]
                # check if all observations are digits
                if all(self.could_be_digit(p) for p in permuted):
                    # permute output digits using the same permutation
                    digits = [self.permute(n, permutation) for n in digits]
                    # convert to real digits
                    digits = [self.get_digit(n) for n in digits]
                    # add to result
                    unscrambled_digits.append(digits)
                    # break as we found the solution
                    break

        # convert all output digits to int
        unscrambled_numbers = [
            int("".join(map(str, digits))) for digits in unscrambled_digits
        ]

        # return the sum
        return sum(unscrambled_numbers)

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day8().execute()
