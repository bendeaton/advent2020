from days.day10 import get_adapters, part1, part2

RAW1 = """16
10
15
5
1
11
7
19
6
12
4"""

RAW2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def test_part1_a():
    assert part1(get_adapters(RAW1)) == 35


def test_part1_b():
    assert part1(get_adapters(RAW2)) == 220


def test_part2_a():
    assert part2(get_adapters(RAW1)) == 8


def test_part2_debug():
    assert part2([0, 1, 4, 7]) == 1
    assert part2([0, 1, 5, 7]) == 0
    assert part2([0, 11, 12, 13]) == 0
    assert part2([0, 2, 4, 7]) == 1


def test_another():
    assert part2([0, 3, 4]) == 1


def test_part2_b():
    assert part2(get_adapters(RAW2)) == 19208
