from typing import List, Tuple

TEST_MAP = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test():
    assert is_tree(TEST_MAP, 0, 0) is False
    assert is_tree(TEST_MAP, 0, 2) is True
    assert is_tree(TEST_MAP, 0, len(TEST_MAP[0]) + 1) is False
    assert wheeeeeeeeeeee(TEST_MAP, step_i=1, step_j=3) == 7
    assert wheeeeeeeeeeee(TEST_MAP, step_i=1, step_j=1) == 2
    assert wheeeeeeeeeeee(TEST_MAP, step_i=1, step_j=3) == 7
    assert wheeeeeeeeeeee(TEST_MAP, step_i=1, step_j=5) == 3
    assert wheeeeeeeeeeee(TEST_MAP, step_i=1, step_j=7) == 4
    assert wheeeeeeeeeeee(TEST_MAP, step_i=2, step_j=1) == 2
    assert part2(TEST_MAP, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]) == 336


def load_items() -> List[str]:
    f = open("inputs/day03.txt")
    return [i.strip() for i in f.readlines()]


def is_tree(items: List[str], i: int, j: int) -> bool:
    jdim = len(items[0])
    return items[i][j % jdim] == "#"


def wheeeeeeeeeeee(tree_map: List[str], step_i: int = 1, step_j: int = 3) -> int:
    num_trees = 0
    cur_i = 0
    cur_j = 0
    while cur_i + step_i < len(tree_map):
        cur_i += step_i
        cur_j += step_j
        if is_tree(tree_map, cur_i, cur_j):
            num_trees += 1

    return num_trees


def part2(tree_map: List[str], slopes: List[Tuple[int, int]]) -> int:
    prod = 1
    for i, j in slopes:
        prod *= wheeeeeeeeeeee(tree_map, step_i=i, step_j=j)

    return prod


def main():
    test()
    real_map = load_items()
    print(f"Part 1: {wheeeeeeeeeeee(real_map, step_i=1, step_j=3)}")
    print(f"Part 2: {part2(real_map, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])}")


if __name__ == "__main__":
    main()
