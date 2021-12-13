from src.day12 import Day12 as DayX

INPUT = "tests/inputs/day12a.txt"


def test_init():
    DayX(INPUT)


def test_part1():
    assert DayX("tests/inputs/day12a.txt").part1() == 10
    assert DayX("tests/inputs/day12b.txt").part1() == 19
    assert DayX("tests/inputs/day12c.txt").part1() == 226


def test_part2():
    assert DayX("tests/inputs/day12a.txt").part2() == 36
    assert DayX("tests/inputs/day12b.txt").part2() == 103
    assert DayX("tests/inputs/day12c.txt").part2() == 3509
