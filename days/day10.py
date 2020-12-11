# https://adventofcode.com/2020/day/10

from collections import Counter, defaultdict
from typing import Dict, List


def get_adapters(raw: str) -> List[int]:
    nums = [int(n) for n in raw.split("\n")]
    return sorted([0] + nums + [max(nums) + 3])


def part1(adapters: List[int]) -> int:
    diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
    counts = Counter(diffs)
    if max(counts.keys()) <= 3:
        return counts.get(1, 0) * counts.get(3, 0)
    return 0


def part2(adapters: List[int]) -> int:
    max_adapter = max(adapters)
    paths: Dict[int, int] = defaultdict(int)
    paths[0] = 1

    for i in range(1, max_adapter + 1):
        if i in adapters:
            # How many ways can I get within 3 of this adapter (prior 3 positions)?
            paths[i] = paths[i - 1] + paths[i - 2] + paths[i - 3]

    return paths[max_adapter]


def main():
    with open("inputs/day10.txt") as f:
        raw = f.read()

    adapters = get_adapters(raw)
    print(f"Part 1: {part1(adapters)}")
    print(f"Part 2: {part2(adapters)}")


if __name__ == "__main__":
    main()
