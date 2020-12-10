from days.day09 import (  # do_contiguous_sum_to_target,
    do_two_add_to_target,
    find_first_error,
    find_sum_min_max_cont_seq,
    load,
)

RAW = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def test_do_two_add_to_target():
    assert do_two_add_to_target([1, 5, 10], 6) is True
    assert do_two_add_to_target([1, 5, 10], 100) is False


def test_find_first_error():
    assert find_first_error(load(RAW), 5) == 127


def test_find_sum_min_max_cont_seq():
    assert find_sum_min_max_cont_seq(load(RAW), 127) == 62
