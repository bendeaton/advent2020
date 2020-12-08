# https://adventofcode.com/2020/day/7

import re
from typing import Dict, List, Set, Tuple

RAW1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

RAW2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


def load_file(fname: str) -> str:
    f = open(fname)
    return f.read()


def parse_bag_def(bag: str) -> Dict[str, Dict[str, int]]:
    color = re.findall(r"^([\w\s]+) bags contain", bag)[0]
    contents = re.findall(r"\s([\d]+) ([\w\s]+) bag", bag)
    return {color: {g[1]: int(g[0]) for g in contents}}


assert parse_bag_def(
    "light red bags contain 1 bright white bag, 2 muted yellow bags."
) == {"light red": {"bright white": 1, "muted yellow": 2}}

assert parse_bag_def("faded blue bags contain no other bags.") == {"faded blue": {}}


def get_bag_data(raw: str) -> Dict:
    bags = [parse_bag_def(x) for x in raw.split("\n")]
    return {k: v for d in bags for k, v in d.items()}


def get_outer_bags(bag_data: Dict, cur: Set[str]) -> Set[str]:
    return {k for k, v in bag_data.items() for c in cur if c in v.keys()}


def get_num_outer_bags(bag_data: Dict, starting_bag: str) -> int:
    bags: Set[str] = set()
    outer_bags = get_outer_bags(bag_data, {starting_bag})
    while outer_bags:
        bags = bags | outer_bags
        outer_bags = get_outer_bags(bag_data, outer_bags)

    return len(bags)


assert get_num_outer_bags(get_bag_data(RAW1), "shiny gold") == 4


def get_num_inner_bags(bag_data: Dict, starting_bag: str) -> int:
    n = -1  # Don't count the starting bag
    inner_bags: List[Tuple[str, int]] = [(starting_bag, 1)]  # bag, multiplier pairs
    while inner_bags:
        n += sum([v for _, v in inner_bags])
        inner_bags = [(k, m * v) for b, m in inner_bags for k, v in bag_data[b].items()]

    return n


assert get_num_inner_bags(get_bag_data(RAW1), "shiny gold") == 32
assert get_num_inner_bags(get_bag_data(RAW2), "shiny gold") == 126


def main():
    raw = load_file("inputs/day07.txt")
    print(f"Part 1: {get_num_outer_bags(get_bag_data(raw), 'shiny gold')}")
    print(f"Part 2: {get_num_inner_bags(get_bag_data(raw), 'shiny gold')}")


if __name__ == "__main__":
    main()
