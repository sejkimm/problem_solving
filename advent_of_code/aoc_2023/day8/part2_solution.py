import os
import re
import math
from typing import List, Tuple, Dict


def solve(input_lines: List[str]) -> int:
    answer: int = 0
    nodes: Dict[str, Tuple(str, str)] = {}
    min_step_to_final_node: Dict[str, int] = {}

    instructions: str = input_lines[0].strip()

    for input_line in input_lines[1:]:
        node_components: re.Match = re.findall(r"[0-9A-Z]{3}", input_line)

        if node_components:
            nodes[node_components[0]] = (node_components[1], node_components[2])

    start_nodes: List[str] = list(filter(lambda x: x[2] == "A", nodes.keys()))

    # while not all(map(lambda x: x[2] == "Z", current_nodes)):

    for start_node in start_nodes:
        current_node: str = start_node
        current_iteration_count: int = 0

        while current_node[2] != "Z":
            for instruction in instructions:
                if instruction == "L":
                    current_node = nodes[current_node][0]
                elif instruction == "R":
                    current_node = nodes[current_node][1]

                current_iteration_count += 1

        min_step_to_final_node[start_node] = current_iteration_count

    answer = math.lcm(*min_step_to_final_node.values())

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
    # INPUT_FILE_NAME: str = "part2_example_input.txt"
    main(input_file_name=INPUT_FILE_NAME)
