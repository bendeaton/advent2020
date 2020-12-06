import pytest

from days.day05 import (
    get_col,
    get_col_code,
    get_lower_half_bounds,
    get_row,
    get_row_code,
    get_seat_id,
    get_upper_half_bounds,
)

TEST_CASES = [
    {"ticket_code": "FBFBBFFRLR", "row": 44, "col": 5, "seat": 357},
    {"ticket_code": "BFFFBBFRRR", "row": 70, "col": 7, "seat": 567},
    {"ticket_code": "FFFBBBFRRR", "row": 14, "col": 7, "seat": 119},
    {"ticket_code": "BBFFBBFRLL", "row": 102, "col": 4, "seat": 820},
]


def test_get_row_code():
    assert get_row_code("FBFBBFFRLR") == "FBFBBFF"


def test_get_col_code():
    assert get_col_code("FBFBBFFRLR") == "RLR"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((0, 127), (0, 63)),
        ((32, 63), (32, 47)),
        ((44, 47), (44, 45)),
        ((44, 45), (44, 44)),
        ((4, 7), (4, 5)),
        ((4, 5), (4, 4)),
        ((100, 100), (100, 100)),
    ],
)
def test_get_lower_half_bounds(test_input, expected):
    assert get_lower_half_bounds(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((0, 63), (32, 63)),
        ((32, 47), (40, 47)),
        ((40, 47), (44, 47)),
        ((44, 45), (45, 45)),
        ((0, 7), (4, 7)),
        ((4, 5), (5, 5)),
        ((100, 100), (100, 100)),
    ],
)
def test_get_upper_half_bounds(test_input, expected):
    assert get_upper_half_bounds(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [(c["ticket_code"], c["col"]) for c in TEST_CASES],
)
def test_get_col(test_input, expected):
    col_code = get_col_code(test_input)
    assert get_col(col_code) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [(c["ticket_code"], c["row"]) for c in TEST_CASES],
)
def test_get_row(test_input, expected):
    row_code = get_row_code(test_input)
    assert get_row(row_code) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [(c["ticket_code"], c["seat"]) for c in TEST_CASES],
)
def test_get_seat_id(test_input, expected):
    assert get_seat_id(test_input) == expected
