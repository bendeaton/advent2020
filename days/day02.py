from dataclasses import dataclass
import re
from typing import Callable, List

TEST_ITEMS = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


@dataclass
class PasswordRow:
    lo: int
    hi: int
    char: str
    pwd: str


def load_items() -> List[str]:
    f = open("inputs/day02.txt")
    return f.readlines()


def extract_case(s: str) -> PasswordRow:
    g = re.findall(r"^(\d+)-(\d+) (\w+): (\w+)", s)[0]
    return PasswordRow(lo=int(g[0]), hi=int(g[1]), char=g[2], pwd=g[3])


def is_valid_part_1(row: PasswordRow) -> bool:
    return row.lo <= row.pwd.count(row.char) <= row.hi


def is_valid_part_2(row: PasswordRow) -> bool:
    return sum([row.pwd[row.lo - 1] == row.char, row.pwd[row.hi - 1] == row.char]) == 1


def get_num_valid(items: List[str], is_valid: Callable) -> int:
    password_rows = [extract_case(j) for j in items]
    return sum([is_valid(row) for row in password_rows])


def main():
    items = load_items()

    assert extract_case("1-3 a: abcde") == PasswordRow(1, 3, "a", "abcde")

    # Part 1
    assert is_valid_part_1(PasswordRow(1, 3, "a", "abcde")) is True
    assert is_valid_part_1(PasswordRow(1, 3, "b", "cdefg")) is False
    assert is_valid_part_1(PasswordRow(2, 9, "c", "ccccccccc")) is True
    assert get_num_valid(TEST_ITEMS, is_valid_part_1) == 2
    print(f"Part 1: {get_num_valid(items, is_valid_part_1)}")

    # Part 2
    assert is_valid_part_2(PasswordRow(1, 3, "a", "abcde")) is True
    assert is_valid_part_2(PasswordRow(1, 3, "b", "cdefg")) is False
    assert is_valid_part_2(PasswordRow(2, 9, "c", "ccccccccc")) is False
    assert get_num_valid(TEST_ITEMS, is_valid_part_2) == 1
    print(f"Part 2: {get_num_valid(items, is_valid_part_2)}")


if __name__ == "__main__":
    main()
