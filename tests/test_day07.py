from src.day7 import Day7 as DayX

INPUT = "tests/inputs/day7.txt"


def test_init():
    DayX(INPUT)


def test_part1():
    assert DayX(INPUT).part1() == 37


def test_part2():
    assert DayX(INPUT).part2() == 168
