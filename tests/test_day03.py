from unittest import TestCase

from src.day3 import Day3 as DayX
from src.utils import read_array_from_file

INPUT = "tests/inputs/day3.txt"


def test_init():
    DayX(INPUT)
    DayX(INPUT).execute()


def test_part1():
    assert DayX(INPUT).part1() == 198


def test_part2():
    assert DayX(INPUT).part2() == 230


def test_get_numbers():
    arr = ["111", "000", "101", "110"]
    d = DayX()
    TestCase().assertCountEqual(d.get_numbers(arr, 0, "1"), ["111", "101", "110"])
    TestCase().assertCountEqual(d.get_numbers(arr, 0, "0"), ["000"])
    TestCase().assertCountEqual(d.get_numbers(arr, 2, "1"), ["111", "101"])


def test_find_oxygen_generator_rating():
    arr = read_array_from_file(INPUT)
    assert DayX.find_oxygen_generator_rating(arr) == "10111"


def test_find_co2_scrubber_rating():
    arr = read_array_from_file(INPUT)
    assert DayX.find_co2_scrubber_rating(arr) == "01010"
