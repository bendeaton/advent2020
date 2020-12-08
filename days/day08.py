# https://adventofcode.com/2020/day/8

from typing import List, NamedTuple, Tuple


class Instruction(NamedTuple):
    loc: int
    op: str
    val: int
    next_loc: int
    acc_inc: int
    loc_inc: int


def parse_str(line: str) -> Tuple[str, int]:
    op, val_str = line.split(" ")
    return op, int(val_str)


def get_instruction(loc: int, op: str, val: int) -> Instruction:
    if op == "acc":
        acc_inc = val
        loc_inc = 1
    elif op == "jmp":
        acc_inc = 0
        loc_inc = val
    else:  # op == "nop"
        acc_inc = 0
        loc_inc = 1
    next_loc = loc + loc_inc
    return Instruction(loc, op, val, next_loc, acc_inc, loc_inc)


def get_instructions(raw: str) -> List[Instruction]:
    return [get_instruction(i, *parse_str(l)) for i, l in enumerate(raw.split("\n"))]


def run_instructions(instructions: List[Instruction]) -> Tuple[List[int], int, bool]:
    loc = 0
    acc = 0
    sequence: List[int] = []
    num_instructions = len(instructions)
    while loc not in sequence and loc < num_instructions:
        sequence.append(loc)
        acc += instructions[loc].acc_inc
        loc = instructions[loc].next_loc

    completed_successfully = loc >= num_instructions
    return sequence, acc, completed_successfully


def run_instructions_and_get_acc(raw: str) -> int:
    instructions = get_instructions(raw)
    _, acc, _ = run_instructions(instructions)
    return acc


def repair_run_instructions_and_get_acc(raw: str) -> int:
    instructions = get_instructions(raw)
    sequence, acc, completed_successfully = run_instructions(instructions)
    switch = {"jmp": "nop", "nop": "jmp"}

    if not completed_successfully:
        for loc in sequence:  # Error is in initial sequence
            cur_op, cur_val = instructions[loc].op, instructions[loc].val
            if cur_op in switch.keys():
                trial_instructions = get_instructions(raw)
                trial_instructions[loc] = get_instruction(loc, switch[cur_op], cur_val)
                _, acc, completed_successfully = run_instructions(trial_instructions)
                if completed_successfully:
                    break

    return acc


def main():
    with open("inputs/day08.txt") as f:
        raw = f.read()

    print(f"Part 1: {run_instructions_and_get_acc(raw)}")
    print(f"Part 2: {repair_run_instructions_and_get_acc(raw)}")


if __name__ == "__main__":
    main()
