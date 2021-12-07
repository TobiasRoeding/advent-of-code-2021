from src.day5 import Day5 as DayX
from src.day5 import Line, Point

INPUT = "tests/inputs/day5.txt"


def test_init():
    DayX(INPUT)
    DayX(INPUT).execute()


def test_part1():
    assert DayX(INPUT).part1() == 5
    return


def test_part2():
    assert DayX(INPUT).part2() == 12


def test_point_init():
    p = Point("1", "2")
    assert p.x == 1
    assert p.y == 2


def test_line_init():
    line = Line("1", "2", "3", "4")
    assert line.start.x == 1
    assert line.start.y == 2
    assert line.end.x == 3
    assert line.end.y == 4


def test_line_horizontal():
    line = Line("1", "2", "5", "2")
    assert line.is_horizontal()


def test_line_vertical():
    line = Line("1", "0", "1", "5")
    assert line.is_vertical()


def test_line_get_max():
    line = Line("1", "0", "1", "5")
    x, y = line.get_max()
    assert x == 1
    assert y == 5


def test_line_get_points():
    line = Line("1", "0", "1", "5")
    points = line.get_points()
    assert len(points) == 6
