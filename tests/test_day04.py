import numpy as np
from numpy.testing import assert_array_equal

from src.day4 import Board
from src.day4 import Day4 as DayX

INPUT = "tests/inputs/day4.txt"


def test_init():
    DayX(INPUT)
    DayX(INPUT).execute()


def test_part1():
    assert DayX(INPUT).part1() == 4512
    return


def test_part2():
    assert DayX(INPUT).part2() == 1924


def test_read_input():
    n, b = DayX(INPUT).read_input(INPUT)
    assert len(n) == 27
    assert len(b) == 3


def test_board_init():
    arr = [["1", "2"], ["3", "4"]]
    b = Board(arr)
    assert_array_equal(b.board, np.array(arr))


def test_board_mark_number():
    b = Board([["1", "2"], ["3", "4"]])
    b.mark_number("1")
    assert b.board[0][0] == "x"


def test_board_get_sum_of_unmarked_numbers():
    b = Board([["1", "x"], ["x", "4"]])
    assert b.get_sum_of_unmarked_numbers() == 5


def test_board_check_complete():
    b = Board([["x", "x"], ["3", "4"]])
    assert b.check_complete()
