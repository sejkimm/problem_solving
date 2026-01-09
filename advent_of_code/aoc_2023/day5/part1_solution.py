import os
import re
from typing import List, Dict, Tuple


class Mapping:
    def __init__(self, input_from: int, output_from: int, distance):
        self.input_range: Tuple[int, int] = (input_from, input_from + distance - 1)
        self.output_range: int = output_from

    def contains_seed(self, seed: int) -> bool:
        return self.input_range[0] <= seed <= self.input_range[1]

    def get_mapped_output(self, seed: int) -> int:
        if self.contains_seed(seed):
            return self.output_range + (seed - self.input_range[0])
        else:
            return None


def parse_almanac(
    almanac_lines: List[str],
) -> Dict[str, Dict[str, List[Mapping]]]:
    almanac: Dict[str, Dict[str, List[Mapping]]] = dict()
    seeds: List[int] = list(map(int, re.findall(r"\d+", almanac_lines[0])))
    source: str = None
    destination: str = None
    category_pattern: str = r"(\w+)-to-(\w+)"

    for almanac_line in almanac_lines[1:]:
        if almanac_line == "\n":
            continue

        category_pattern_matched: re.Match = re.search(category_pattern, almanac_line)

        if category_pattern_matched:
            source: str = category_pattern_matched.group(1)
            destination: str = category_pattern_matched.group(2)
            almanac[source] = dict({destination: []})
        else:
            parsed_value: re.Match = re.findall(r"(\d+)", almanac_line)

            output_from: int = int(parsed_value[0])
            input_index: int = int(parsed_value[1])
            distance: int = int(parsed_value[2])

            almanac[source][destination].append(Mapping(input_index, output_from, distance))

    return almanac, seeds


def solve(almanac_lines: List[str]) -> int:
    answer: int = 0
    almanac: Dict[str, Dict[str, List[Mapping]]] = dict()
    seeds: List[int] = list()

    almanac, seeds = parse_almanac(almanac_lines)

    seed_current_value: Dict[int, int] = dict({seed: seed for seed in seeds})

    current_component: str = "seed"
    next_component: str = None

    while current_component != "location":
        next_component = list(almanac[current_component].keys())[0]

        for seed, value in seed_current_value.items():
            for mapping in almanac[current_component][next_component]:
                if mapping.contains_seed(value):
                    seed_current_value[seed] = mapping.get_mapped_output(value)

        current_component = next_component

    answer = min(seed_current_value.values())

    return answer


def main(**kwargs):
    input_file_path = os.path.join(os.path.dirname(__file__), kwargs["input_file_name"])

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        almanac_lines: List[str] = input_file.readlines()

        answer: int = solve(almanac_lines)

        print(f"answer : {answer}")

    return answer


if __name__ == "__main__":
    # INPUT_FILE_NAME: str = "input.txt"
    INPUT_FILE_NAME: str = "example_input.txt"
    main(input_file_name=INPUT_FILE_NAME)
