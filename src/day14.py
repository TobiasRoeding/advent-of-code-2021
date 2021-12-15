from collections import Counter


class Day14:
    def __init__(self, input="src/input/day14.txt"):
        self.INPUT = input

    def read_input(self):
        template, _, *rules = open(self.INPUT).read().split("\n")
        rules = dict(r.split(" -> ") for r in rules)
        return template, rules

    def step(self, pairs, chars, rules):
        for (a, b), c in pairs.copy().items():
            x = rules[a + b]
            pairs[a + b] -= c
            pairs[a + x] += c
            pairs[x + b] += c
            chars[x] += c

    def part1(self, steps=10):
        template, rules = self.read_input()

        pairs = Counter(map(str.__add__, template, template[1:]))
        chars = Counter(template)

        for _ in range(steps):
            self.step(pairs, chars, rules)

        return max(chars.values()) - min(chars.values())

    def part2(self):
        return self.part1(40)

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day14().execute()
