import itertools
from typing import List, Optional

import numpy as np


def test_case_1():
    items = [1721, 979, 366, 299, 675, 1456]
    expected = 1721 * 299
    actual = get_combo(items, target=2020)
    assert actual == expected


def get_combo(
    items: List[int], num_in_combo: int = 2, target: int = 2020
) -> Optional[int]:
    for combo in itertools.combinations(items, num_in_combo):
        if np.sum(combo) == target:
            return np.prod(combo)

    return None


def main():
    test_case_1()

    f = open("inputs/day01.txt")
    items = [int(i) for i in f.readlines()]

    print(get_combo(items, num_in_combo=2))
    print(get_combo(items, num_in_combo=3))


if __name__ == "__main__":
    main()
