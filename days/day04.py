import re
from typing import Dict, List


def load_as_dicts(fname: str) -> List[Dict[str, str]]:
    f = open(fname)
    lines = f.readlines()
    each_as_str = [s.replace("\n", " ") for s in "".join(lines).split("\n\n")]
    return [
        {i.split(":")[0]: i.split(":")[1] for i in s.split(" ")} for s in each_as_str
    ]


def is_year_valid(x: str, lo: int, hi: int) -> bool:
    if re.fullmatch(r"^^(\d{4})$", x):
        if lo <= int(x) <= hi:
            return True
    return False


def is_byr_valid(x: str) -> bool:
    return is_year_valid(x, 1920, 2002)


def is_iyr_valid(x: str) -> bool:
    return is_year_valid(x, 2010, 2020)


def is_eyr_valid(x: str) -> bool:
    return is_year_valid(x, 2020, 2030)


def is_hgt_valid(x: str) -> bool:
    g = re.findall(r"^(\d+)(cm|in)", x)
    if g:
        num, unit = g[0]
        if unit == "cm":
            return 150 <= int(num) <= 193
        elif unit == "in":
            return 59 <= int(num) <= 76

    return False


def is_hcl_valid(x: str) -> bool:
    return True if re.fullmatch(r"^#[0-9a-f]{6}$", x) else False


def is_ecl_valid(x: str) -> bool:
    return x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_pid_valid(x: str) -> bool:
    return True if re.fullmatch(r"^[\d]{9}$", x) else False


def is_valid_naive(passport: Dict[str, str]) -> bool:
    REQ_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return REQ_FIELDS.issubset(set(passport.keys()))


def is_valid(passport: Dict[str, str]) -> bool:
    return all(
        [
            is_byr_valid(passport.get("byr", "")),
            is_iyr_valid(passport.get("iyr", "")),
            is_eyr_valid(passport.get("eyr", "")),
            is_hgt_valid(passport.get("hgt", "")),
            is_hcl_valid(passport.get("hcl", "")),
            is_ecl_valid(passport.get("ecl", "")),
            is_pid_valid(passport.get("pid", "")),
        ]
    )


def num_valid_passports_naive(passports: List[Dict[str, str]]) -> int:
    return sum([is_valid_naive(passport) for passport in passports])


def num_valid_passports(passports: List[Dict[str, str]]) -> int:
    return sum([is_valid(passport) for passport in passports])


def test_final():
    passports = load_as_dicts("inputs/day04.txt")
    assert num_valid_passports_naive(passports) == 208
    assert num_valid_passports(passports) == 167


def main():
    passports = load_as_dicts("inputs/day04.txt")
    print(f"Part 1 num valid is: {num_valid_passports_naive(passports)}")
    print(f"Part 2 num valid is: {num_valid_passports(passports)}")


if __name__ == "__main__":
    main()
