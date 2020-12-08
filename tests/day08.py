from days.day08 import (
    Instruction,
    get_instruction,
    parse_str,
    repair_run_instructions_and_get_acc,
    run_instructions_and_get_acc,
)

RAW1 = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

RAW2 = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
nop -4
acc +6"""


def test_parse_str():
    assert parse_str("acc +7") == ("acc", 7)
    assert parse_str("jmp +2") == ("jmp", 2)
    assert parse_str("jmp -2") == ("jmp", -2)
    assert parse_str("nop +0") == ("nop", 0)


def test_get_instruction():
    assert get_instruction(10, "acc", 7) == Instruction(
        loc=10, op="acc", val=7, next_loc=11, acc_inc=7, loc_inc=1
    )
    assert get_instruction(10, "jmp", 2) == Instruction(
        loc=10, op="jmp", val=2, next_loc=12, acc_inc=0, loc_inc=2
    )
    assert get_instruction(10, "nop", 0) == Instruction(
        loc=10, op="nop", val=0, next_loc=11, acc_inc=0, loc_inc=1
    )


def test_run_instructions_and_get_acc():
    assert run_instructions_and_get_acc(RAW1) == 5
    assert run_instructions_and_get_acc(RAW2) == 8


def test_repair_run_instructions_and_get_acc():
    assert repair_run_instructions_and_get_acc(RAW1) == 8
