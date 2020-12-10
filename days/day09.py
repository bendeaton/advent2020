# https://adventofcode.com/2020/day/9

from typing import List, Tuple


def load(raw: str) -> List[int]:
    return [int(n) for n in raw.split("\n")]


def get_preambles_targets(nums: List[int], len_pre: int) -> List[Tuple[List[int], int]]:
    # Return list containing (list preamble ints, target int) tuples
    pairs = []
    for i in range(len_pre, len(nums)):
        pairs.append((nums[i - len_pre : i], nums[i]))  # noqa: E203
    return pairs


def do_two_add_to_target(nums: List[int], target: int) -> bool:
    valids = set([target - num for num in nums])
    return any([n in valids for n in nums])


def find_first_error(nums: List[int], len_preamble: int) -> int:
    for preamble, target in get_preambles_targets(nums, len_preamble):
        if not do_two_add_to_target(preamble, target):
            return target
    return 0


def find_sum_min_max_cont_seq(nums: List[int], target: int) -> int:
    target_index = nums.index(target)
    for i in range(target_index):
        for j in range(i + 1, target_index):
            contig_sublist = nums[i : j + 1]  # noqa: E203
            if target == sum(contig_sublist):
                return min(contig_sublist) + max(contig_sublist)
    return 0


def main():
    with open("inputs/day09.txt") as f:
        raw = f.read()

    nums = load(raw)
    first_wrong_val = find_first_error(nums, len_preamble=25)
    print(f"Part 1: {first_wrong_val}")
    print(f"Part 2: {find_sum_min_max_cont_seq(nums, first_wrong_val)}")


if __name__ == "__main__":
    main()
