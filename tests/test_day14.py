from src.day14 import Day14 as DayX

INPUT = "tests/inputs/day14.txt"


def test_init():
    DayX(INPUT)


def test_part1():
    assert DayX(INPUT).part1() == 1588


def test_part2():
    assert DayX(INPUT).part2() == 2188189693529
