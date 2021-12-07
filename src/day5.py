import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"{self.x}, {self.y}"


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.start = Point(x1, y1)
        self.end = Point(x2, y2)

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x

    def get_max(self):
        x = max([self.start.x, self.end.x])
        y = max([self.start.y, self.end.y])
        return x, y

    def get_points(self):
        points = []
        points.append(self.start)
        prev = self.start

        diff_x = self.end.x - self.start.x
        diff_y = self.end.y - self.start.y
        for i in range(1, max(abs(diff_x), abs(diff_y))):
            if diff_x == 0 and diff_y != 0:
                x = 0
                y = diff_y / abs(diff_y)
            elif diff_x != 0 and diff_y == 0:
                x = diff_x / abs(diff_x)
                y = 0
            else:
                x = diff_x / abs(diff_x)
                y = diff_y / abs(diff_y)

            p = Point(prev.x + x, prev.y + y)
            points.append(p)
            prev = p

        points.append(self.end)
        return points


class Day5:
    def __init__(self, input="src/input/day5.txt"):
        self.INPUT = input

    def read_input(self):
        with open(self.INPUT, "r") as fp:
            lines = fp.readlines()

        result = []
        for line in lines:
            start, end = line.strip().split(" -> ")
            x1, y1 = start.split(",")
            x2, y2 = end.split(",")
            line_obj = Line(x1, y1, x2, y2)
            result.append(line_obj)

        return result

    def convert_lines_to_grid(self, lines):
        max_x = 0
        max_y = 0
        for line in lines:
            x, y = line.get_max()
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        grid = np.zeros((max_x + 1, max_y + 1), dtype=int)

        for line in lines:
            points = line.get_points()
            for point in points:
                grid[point.x, point.y] += 1

        return grid

    def part1(self):
        arr = self.read_input()

        # filter to only horizontal or vertical lines
        lines = []
        for line in arr:
            if line.is_horizontal() or line.is_vertical():
                lines.append(line)

        grid = self.convert_lines_to_grid(lines)
        return (grid >= 2).sum()

    def part2(self):
        arr = self.read_input()
        grid = self.convert_lines_to_grid(arr)
        return (grid >= 2).sum()

    def execute(self):
        print(f"Solution for part 1: {self.part1()}")
        print(f"Solution for part 2: {self.part2()}")


if __name__ == "__main__":
    Day5().execute()
