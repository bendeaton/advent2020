from functools import partial
import re
from typing import List, Optional, Tuple

TICKET_PATTERN = r"^([FB]{7})([LR]{3})"
MAX_COL = 7
MAX_ROW = 127


def load_file(fname: str) -> List[str]:
    f = open(fname)
    return f.readlines()


def get_row_code(ticket_code: str) -> str:
    return re.findall(TICKET_PATTERN, ticket_code)[0][0]


def get_col_code(ticket_code: str) -> str:
    return re.findall(TICKET_PATTERN, ticket_code)[0][1]


def get_lower_half_bounds(lo: int, hi: int) -> Tuple[int, int]:
    return lo, lo + (hi - lo) // 2


def get_upper_half_bounds(lo: int, hi: int) -> Tuple[int, int]:
    return hi - (hi - lo) // 2, hi


def get_loc(switches: str, lo: int, hi: int) -> int:
    switch_func = {
        "F": get_lower_half_bounds,
        "B": get_upper_half_bounds,
        "L": get_lower_half_bounds,
        "R": get_upper_half_bounds,
    }
    i, j = lo, hi
    for switch in switches:
        i, j = switch_func[switch](i, j)

    assert i == j
    return i


get_row = partial(get_loc, lo=0, hi=MAX_ROW)
get_col = partial(get_loc, lo=0, hi=MAX_COL)


def get_seat_id(ticket_code: str) -> int:
    return get_row(get_row_code(ticket_code)) * 8 + get_col(get_col_code(ticket_code))


def get_all_seat_ids(ticket_codes: List[str]) -> List[int]:
    return [get_seat_id(t) for t in ticket_codes]


def find_first_missing_seat(ticket_codes: List[str]) -> Optional[int]:
    taken_seats = sorted(get_all_seat_ids(ticket_codes))
    all_seats = range(min(taken_seats), max(taken_seats))
    (missing,) = set(all_seats) - set(taken_seats)
    return missing


def main():
    ticket_codes = load_file("inputs/day05.txt")
    print(f"Part 1 max seat id: {max(get_all_seat_ids(ticket_codes))}")
    print(f"Part 2 missing seat id: {find_first_missing_seat(ticket_codes)}")


if __name__ == "__main__":
    main()
