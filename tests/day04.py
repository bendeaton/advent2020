from days.day04 import (
    is_ecl_valid,
    is_hcl_valid,
    is_hgt_valid,
    is_pid_valid,
    is_year_valid,
    load_as_dicts,
    num_valid_passports_naive,
)


def test_is_year_valid():
    cases = [
        ("", False),
        ("1", False),
        ("12345", False),
        ("1919", False),
        ("1920", True),
        ("2002", True),
        ("2003", False),
    ]
    for val, expected in cases:
        assert is_year_valid(val, 1920, 2002) is expected


def test_is_hgt_valid():
    cases = [
        ("", False),
        ("60in", True),
        ("190cm", True),
        ("190in", False),
        ("190", False),
    ]
    for val, expected in cases:
        assert is_hgt_valid(val) is expected


def test_is_hcl_valid():
    cases = [
        ("", False),
        ("#123abc", True),
        ("#abc123", True),
        ("#123abz", False),
        ("123abc", False),
    ]
    for val, expected in cases:
        assert is_hcl_valid(val) is expected


def test_is_ecl_valid():
    cases = [("", False), ("blu", True), ("blk", False)]
    for val, expected in cases:
        assert is_ecl_valid(val) is expected


def test_is_pid_valid():
    cases = [("", False), ("000000001", True), ("0123456789", False)]
    for val, expected in cases:
        assert is_pid_valid(val) is expected


def test_num_valid_passports_naive():
    test_passports = load_as_dicts("inputs/day04_test.txt")
    assert num_valid_passports_naive(test_passports) == 2
