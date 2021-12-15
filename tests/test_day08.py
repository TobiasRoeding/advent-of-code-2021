from src.day8 import Day8 as DayX

INPUT = "tests/inputs/day8.txt"


def test_init():
    DayX(INPUT)


def test_part1():
    assert DayX(INPUT).part1() == 26


def test_part2():
    assert DayX(INPUT).part2() == 61229
