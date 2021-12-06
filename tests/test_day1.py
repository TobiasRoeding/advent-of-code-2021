from src.day1 import Day1

INPUT = "tests/inputs/day1.txt"


def test_init():
    Day1(INPUT)
    Day1(INPUT).execute()


def test_part1():
    assert Day1.part1(INPUT) == 7


def test_part2():
    assert Day1.part2(INPUT) == 5
