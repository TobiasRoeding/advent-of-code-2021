import math


class Day9:
    def __init__(self, input="src/input/day9.txt"):
        self.INPUT = input

    def read_input(self):
        heightmap = []
        with open(self.INPUT, "r") as fp:
            lines = fp.readlines()
            for line in lines:
                heights = [int(height) for height in line.strip()]
                heightmap.append(heights)
        return heightmap

    def get_height(self, heightmap, row, col):
        if (
            row < 0
            or row > len(heightmap) - 1
            or col < 0
            or col > len(heightmap[0]) - 1
        ):
            return 10
        else:
            return heightmap[row][col]

    def part1(self):
        heightmap = self.read_input()

        low_points = []
        for row in range(len(heightmap)):
            for col in range(len(heightmap[0])):
                current = heightmap[row][col]
                top = self.get_height(heightmap, row - 1, col)
                bottom = self.get_height(heightmap, row + 1, col)
                left = self.get_height(heightmap, row, col - 1)
                right = self.get_height(heightmap, row, col + 1)

                if all(adjacent > current for adjacent in [top, bottom, left, right]):
                    low_points.append(current)

        risk = sum(low_points) + len(low_points)

        return risk

    def get_basin_points(self, heightmap, points, current_point):
        row, col = current_point
        current = self.get_height(heightmap, row, col)
        if current < 9:
            points.add(current_point)

            top = self.get_height(heightmap, row - 1, col)
            if top > current:
                self.get_basin_points(heightmap, points, (row - 1, col))
            bottom = self.get_height(heightmap, row + 1, col)
            if bottom > current:
                self.get_basin_points(heightmap, points, (row + 1, col))
            left = self.get_height(heightmap, row, col - 1)
            if left > current:
                self.get_basin_points(heightmap, points, (row, col - 1))
            right = self.get_height(heightmap, row, col + 1)
            if right > current:
                self.get_basin_points(heightmap, points, (row, col + 1))

            return points
        else:
            return

    def part2(self):
        heightmap = self.read_input()

        # find low points
        low_points = []
        for row in range(len(heightmap)):
            for col in range(len(heightmap[0])):
                current = heightmap[row][col]
                top = self.get_height(heightmap, row - 1, col)
                bottom = self.get_height(heightmap, row + 1, col)
                left = self.get_height(heightmap, row, col - 1)
                right = self.get_height(heightmap, row, col + 1)

                if all(adjacent > current for adjacent in [top, bottom, left, right]):
                    low_points.append((row, col))

        # expand low points to basins
        basin_sizes = []
        for low_point in low_points:
            basin_points = self.get_basin_points(heightmap, set(), low_point)
            basin_sizes.append(len(basin_points))

        # sort result
        basin_sizes.sort()

        # return top3 multiplied
        return math.prod(basin_sizes[-3:])

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day9().execute()
