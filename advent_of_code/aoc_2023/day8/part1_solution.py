import os
import re
from typing import List, Tuple, Dict


def solve(input_lines: List[str]) -> int:
    answer: int = 0
    nodes: Dict[str, Tuple(str, str)] = {}

    instructions: str = input_lines[0].strip()

    for input_line in input_lines[1:]:
        node_components: re.Match = re.findall(r"[A-Z]{3}", input_line)

        if node_components:
            nodes[node_components[0]] = (node_components[1], node_components[2])

    current_node: str = "AAA"

    while current_node != "ZZZ":
        for instruction in instructions:
            if instruction == "L":
                current_node = nodes[current_node][0]
            elif instruction == "R":
                current_node = nodes[current_node][1]

            answer += 1

    return answer


def main(**kwargs):
    input_file_path = os.path.join(os.path.dirname(__file__), kwargs["input_file_name"])

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        input_lines: List[str] = input_file.readlines()

        answer: int = solve(input_lines)

        print(f"answer : {answer}")

    return answer


if __name__ == "__main__":
    INPUT_FILE_NAME: str = "input.txt"
    # INPUT_FILE_NAME: str = "example_input.txt"
    main(input_file_name=INPUT_FILE_NAME)
