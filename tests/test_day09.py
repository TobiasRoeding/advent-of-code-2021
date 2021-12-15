from src.day9 import Day9 as DayX

INPUT = "tests/inputs/day9.txt"


def test_init():
    DayX(INPUT)


def test_part1():
    assert DayX(INPUT).part1() == 15


def test_part2():
    assert DayX(INPUT).part2() == 1134
