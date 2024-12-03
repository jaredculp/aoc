import operator
import re
from functools import lru_cache
from typing import Dict, Union

inputs = [x.strip() for x in open("2015/inputs/07.txt").readlines()]
outputs: Dict[str, Union[str, int]] = dict()

commands = {
    r"^(\w+)$": lambda x: x,
    r"^(\w+) AND (\w+)$": operator.and_,
    r"^([a-z]+) OR ([a-z]+)$": operator.or_,
    r"^([a-z]+) LSHIFT (\d+)$": operator.lshift,
    r"^([a-z]+) RSHIFT (\d+)$": operator.rshift,
    r"^NOT ([a-z]+)$": operator.inv,
}


@lru_cache()
def get_wire(wire: str) -> int:
    instr = str(outputs[wire])
    for regex, func in commands.items():
        match = re.search(regex, instr)
        if match:
            parsed_groups = []
            for group in match.groups():
                if group.isnumeric():
                    parsed_groups.append(int(group))
                else:
                    parsed_groups.append(get_wire(group))

            return func(*parsed_groups) & 0xFFFF
    else:
        raise ValueError("Bad instruction")


for line in inputs:
    lhs, rhs = line.split(" -> ")
    outputs[rhs] = lhs


print(get_wire("a"))

outputs["b"] = get_wire("a")
get_wire.cache_clear()
print(get_wire("a"))
