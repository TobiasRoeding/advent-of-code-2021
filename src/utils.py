from typing import List


def read_array_from_file(path: str) -> List[str]:

    with open(path, "r") as fp:
        # read all lines from file
        lines = fp.readlines()
        # remove line endings from array
        lines = [line.strip() for line in lines]

    return lines


def convert_array_from_string_to_int(arr: List[str]) -> List[int]:
    return [int(a) for a in arr]


def read_file_as_int_array(path: str) -> List[int]:
    arr = read_array_from_file(path)
    return convert_array_from_string_to_int(arr)
