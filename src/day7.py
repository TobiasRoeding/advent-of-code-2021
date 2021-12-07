class Day7:
    def __init__(self, input="src/input/day7.txt"):
        self.INPUT = input

    def read_input(self):
        with open(self.INPUT, "r") as fp:
            line = fp.readline().split(",")
            positions = [int(position) for position in line]
        return positions

    def fuel_cost_constant(self, positions, new_position):
        cost = 0
        for position in positions:
            cost += abs(position - new_position)
        return cost

    def fuel_cost(self, positions, new_position):
        cost = 0
        for position in positions:
            diff = abs(position - new_position)
            cost += sum(range(1, diff + 1))
        return cost

    def part1(self):
        positions = self.read_input()

        min_cost = float("inf")
        for position in range(min(positions), max(positions)):
            cost = self.fuel_cost_constant(positions, position)
            if cost < min_cost:
                min_cost = cost

        return min_cost

    def part2(self):
        positions = self.read_input()

        min_cost = float("inf")
        for position in range(min(positions), max(positions)):
            cost = self.fuel_cost(positions, position)
            if cost < min_cost:
                min_cost = cost

        return min_cost

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day7().execute()
