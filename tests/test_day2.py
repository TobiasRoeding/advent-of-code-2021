from src.day2 import Day2

INPUT = "tests/inputs/day2.txt"


def test_init():
    Day2(INPUT)
    Day2(INPUT).execute()


def test_part1():
    assert Day2.part1(INPUT) == 150


def test_part2():
    assert Day2.part2(INPUT) == 900
