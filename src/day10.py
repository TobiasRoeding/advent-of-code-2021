class Day10:

    ILLEGAL_CHAR_TO_POINTS = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    def __init__(self, input="src/input/day10.txt"):
        self.INPUT = input

    def read_input(self):
        input = []
        with open(self.INPUT, "r") as fp:
            lines = fp.readlines()
            input = [line.strip() for line in lines]
        return input

    def part1(self):
        input = self.read_input()

        # remove all legal chunks
        legal_chunks = ["()", "{}", "<>", "[]"]
        cleaned_input = []
        for line in input:
            prev_length = float("inf")
            while prev_length > len(line):
                prev_length = len(line)
                for chunk in legal_chunks:
                    line = line.replace(chunk, "")
            cleaned_input.append(line)

        # check if incomplete or illegal
        illegal_characters = []
        for line in cleaned_input:
            for char in line:
                if char not in ["(", "{", "<", "["]:
                    illegal_characters.append(char)
                    break

        return sum([self.ILLEGAL_CHAR_TO_POINTS[char] for char in illegal_characters])

    def part2(self):
        input = self.read_input()

        # remove all legal chunks
        legal_chunks = ["()", "{}", "<>", "[]"]
        cleaned_input = []
        for line in input:
            prev_length = float("inf")
            while prev_length > len(line):
                prev_length = len(line)
                for chunk in legal_chunks:
                    line = line.replace(chunk, "")
            cleaned_input.append(line)

        # discard corrupted lines
        incomplete_input = []
        for line in cleaned_input:
            closings = [")", "}", ">", "]"]
            check = False
            for closing in closings:
                if closing in line:
                    check = True
            if not check:
                incomplete_input.append(line)

        # reverse the order
        missing_input = [line[::-1] for line in incomplete_input]

        # reverse doesn't change opening to closing brackets,
        # which is why we use opening brackets to calculate the final score
        char_to_points = {
            "(": 1,
            "[": 2,
            "{": 3,
            "<": 4,
        }

        # calculate result
        scores = []
        for line in missing_input:
            score = 0
            for char in line:
                score *= 5
                score += char_to_points[char]
            scores.append(score)

        # sort scores and return middle
        return sorted(scores)[len(scores) // 2]

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day10().execute()
