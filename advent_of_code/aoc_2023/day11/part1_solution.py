import os
from typing import List, Tuple


def get_expanded_universe(universe: List[List[str]]) -> List[List[str]]:
    expanded_universe: List[List[str]] = []

    for row in universe:
        expanded_universe.append(row)
        if all([cell == "." for cell in row]):
            expanded_universe.append(row)

    transposed_universe: List[List[str]] = list(zip(*expanded_universe))
    expanded_transposed_universe: List[List[str]] = []

    for col in transposed_universe:
        expanded_transposed_universe.append(col)

        if all([cell == "." for cell in col]):
            expanded_transposed_universe.append(col)

    return list(zip(*expanded_transposed_universe))


def solve(input_lines: List[str]) -> int:
    answer: int = 0

    universe: List[List[str]] = [list(line.strip()) for line in input_lines]
    expanded_universe: List[List[str]] = get_expanded_universe(universe)
    galaxies: List[Tuple[int, int]] = [
        (row_idx, col_idx)
        for row_idx, row in enumerate(expanded_universe)
        for col_idx, elem in enumerate(row)
        if elem == "#"
    ]

    for idx, galaxy in enumerate(galaxies):
        other_galaxies: List[Tuple[int, int]] = galaxies[(idx + 1) :]

        for other_galaxy in other_galaxies:
            answer += abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])

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
