from src.day10 import Day10 as DayX

INPUT = "tests/inputs/day10.txt"


def test_init():
    DayX(INPUT)


def test_part1():
    assert DayX(INPUT).part1() == 26397


def test_part2():
    assert DayX(INPUT).part2() == 288957
