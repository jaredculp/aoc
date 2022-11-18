import json
from typing import Any, Dict, List, Optional, Union

input = json.loads(open("2015/inputs/12.txt").read())


def sum_json(
    input: Union[int, str, List[Any], Dict[str, Any]],
    skip_red: Optional[bool] = False,
) -> int:
    if isinstance(input, int):
        return input

    total = 0
    if isinstance(input, list):
        total += sum([sum_json(x, skip_red) for x in input])
    elif isinstance(input, dict):
        if skip_red and "red" in input.values():
            return 0

        for k, v in input.items():
            total += sum_json(v, skip_red)

    return total


print("part1: ", sum_json(input))
print("part2: ", sum_json(input, True))
