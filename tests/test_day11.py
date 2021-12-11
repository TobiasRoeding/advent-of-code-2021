from src.day11 import Day11 as DayX

INPUT = "tests/inputs/day11.txt"


def test_init():
    DayX(INPUT)


def test_part1():
    assert DayX(INPUT).part1() == 1656


def test_part2():
    assert DayX(INPUT).part2() == 195
