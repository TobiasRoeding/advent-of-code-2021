from src.day13 import Day13 as DayX

INPUT = "tests/inputs/day13.txt"


def test_init():
    DayX(INPUT)


def test_part1():
    assert DayX(INPUT).part1() == 17


def test_part2():
    assert DayX(INPUT).part2() == 16
