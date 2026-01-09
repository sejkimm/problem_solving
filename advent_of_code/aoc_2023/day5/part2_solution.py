import os
import re
from typing import List, Dict, Type, Optional


class SeedRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    @property
    def start(self) -> int:
        return self._start

    @start.setter
    def start(self, start: int) -> None:
        self._start = start

    def intersects(self, other: Type["SeedRange"]) -> bool:
        return self.start <= other.end and other.start <= self.end

    def fully_contains(self, other: Type["SeedRange"]) -> bool:
        return self.start <= other.start and other.end <= self.end

    def get_intersection(self, other: Type["SeedRange"]) -> Optional[Type["SeedRange"]]:
        if self.intersects(other):
            return SeedRange(max(self.start, other.start), min(self.end, other.end))
        else:
            return None

    def get_non_intersection(self, other: Type["SeedRange"]) -> Optional[List[Type["SeedRange"]]]:
        non_intersection: List[Type["SeedRange"]] = list()

        if self.intersects(other):
            intersection: Type["SeedRange"] = self.get_intersection(other)

            if other.start < intersection.start:
                non_intersection.append(SeedRange(other.start, intersection.start - 1))
            if intersection.end < other.end:
                non_intersection.append(SeedRange(intersection.end + 1, other.end))
        else:
            non_intersection.append(other)

        if len(non_intersection) == 0:
            return None
        else:
            return non_intersection

    def __repr__(self) -> str:
        return f"({self.start} ~ {self.end})"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, SeedRange):
            return self.start == __value.start and self.end == __value.end
        else:
            return False


class Mapping:
    def __init__(self, input_from: int, output_from: int, distance):
        self.input_range: SeedRange = SeedRange(input_from, input_from + distance - 1)
        self.output_range: SeedRange = SeedRange(output_from, output_from + distance - 1)

    def get_intersection_with_input_range(self, input_range: SeedRange) -> Type["SeedRange"]:
        return self.input_range.get_intersection(input_range)

    def get_non_intersection_with_input_range(self, input_range: SeedRange) -> List[Type["SeedRange"]]:
        return self.input_range.get_non_intersection(input_range)

    def get_mapped_output(self, input_range: SeedRange) -> SeedRange:
        output: SeedRange = SeedRange(
            (self.output_range.start - self.input_range.start) + input_range.start,
            (self.output_range.start - self.input_range.start) + input_range.end,
        )

        return output

    def __repr__(self) -> str:
        return f"Input Range: {self.input_range}, Output Range: {self.output_range}"


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
    seed_initial_ranges: List[int] = list()
    seed_current_ranges: List[SeedRange] = list()

    almanac, seed_initial_ranges = parse_almanac(almanac_lines)

    for idx in range(0, len(seed_initial_ranges), 2):
        seed_current_ranges.append(
            SeedRange(seed_initial_ranges[idx], seed_initial_ranges[idx] + seed_initial_ranges[idx + 1] - 1)
        )

    current_component: str = "seed"
    next_component: str = None

    while current_component != "location":
        next_component = list(almanac[current_component].keys())[0]
        seed_next_ranges: List[SeedRange] = list()

        while seed_current_ranges:
            seed_range: SeedRange = seed_current_ranges.pop(0)
            next_ranges: List[SeedRange] = list()
            is_mapped: bool = False

            for mapping in almanac[current_component][next_component]:
                mapped_output: SeedRange = None

                intersection_with_input_range: SeedRange = mapping.get_intersection_with_input_range(seed_range)

                if intersection_with_input_range:
                    mapped_output = mapping.get_mapped_output(intersection_with_input_range)
                    next_ranges.append(mapped_output)

                    non_intersection_with_input_range: List[SeedRange] = mapping.get_non_intersection_with_input_range(
                        seed_range
                    )
                    if non_intersection_with_input_range:
                        seed_current_ranges.extend(non_intersection_with_input_range)

                    is_mapped = True

            if not is_mapped:
                next_ranges.append(seed_range)

            seed_next_ranges += [next_range for next_range in next_ranges if next_range not in seed_next_ranges]

        current_component = next_component
        seed_current_ranges = seed_next_ranges

    answer = min(map(lambda seed_range: seed_range.start, seed_current_ranges))

    return answer


def main(**kwargs):
    input_file_path = os.path.join(os.path.dirname(__file__), kwargs["input_file_name"])

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        almanac_lines: List[str] = input_file.readlines()

        answer: int = solve(almanac_lines)

        print(f"answer : {answer}")

    return answer


if __name__ == "__main__":
    INPUT_FILE_NAME: str = "input.txt"
    # INPUT_FILE_NAME: str = "example_input.txt"
    main(input_file_name=INPUT_FILE_NAME)
