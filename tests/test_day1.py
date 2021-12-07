from src.day1 import Day1 as DayX

INPUT = "tests/inputs/day1.txt"


def test_init():
    DayX(INPUT)
    DayX(INPUT).execute()


def test_part1():
    assert DayX(INPUT).part1() == 7


def test_part2():
    assert DayX(INPUT).part2() == 5
