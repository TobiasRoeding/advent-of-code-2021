from src.day2 import Day2 as DayX

INPUT = "tests/inputs/day2.txt"


def test_init():
    DayX(INPUT)
    DayX(INPUT).execute()


def test_part1():
    assert DayX(INPUT).part1() == 150


def test_part2():
    assert DayX(INPUT).part2() == 900
