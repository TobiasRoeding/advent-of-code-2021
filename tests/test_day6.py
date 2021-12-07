from src.day6 import Day6 as DayX

INPUT = "tests/inputs/day6.txt"


def test_init():
    DayX(INPUT)


def test_part1():
    assert DayX(INPUT).part1(18) == 26
    assert DayX(INPUT).part1(80) == 5934


def test_part2():
    assert DayX(INPUT).part2(256) == 26984457539
