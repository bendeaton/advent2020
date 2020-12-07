# https://adventofcode.com/2020/day/6

from collections import Counter
from itertools import groupby
from typing import List


def load_file(fname: str) -> List[str]:
    f = open(fname)
    data = f.read()
    return data.replace("\n", " ").split("  ")


def main():
    groups_of_answers = load_file("inputs/day06.txt")

    # Using itertools.groupby
    part1 = 0
    part2 = 0
    for answers in groups_of_answers:
        num_ppl = len(answers.split(" "))
        chars = sorted(answers.replace(" ", ""))
        part1 += len(list(groupby(chars)))
        part2 += sum([len(list(v)) == num_ppl for _, v in groupby(chars)])

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

    # Using collections.Counter
    part1 = 0
    part2 = 0
    for answers in groups_of_answers:
        num_ppl = len(answers.split(" "))
        chars = Counter(answers.replace(" ", ""))
        part1 += len(chars)
        part2 += sum([v == num_ppl for _, v in chars.items()])

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

    # Using sets
    part1 = 0
    part2 = 0
    for answers in groups_of_answers:
        answer_sets = [set(ans) for ans in answers.split(" ")]
        part1 += len(set.union(*answer_sets))
        part2 += len(set.intersection(*answer_sets))

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
