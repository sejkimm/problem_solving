import os
import functools
from typing import List


def get_differences_at_each_step(sequences: List[int]) -> List[int]:
    differences_at_each_step: List[int] = []

    for index in range(1, len(sequences)):
        differences_at_each_step.append(sequences[index] - sequences[index - 1])

    return differences_at_each_step


def solve(input_lines: List[str]) -> int:
    answer: int = 0

    for input_line in input_lines:
        sequences: List[int] = list(map(int, input_line.strip().split(" ")))
        first_elements: List[int] = [sequences[0]]
        
        differences_at_each_step: List[int] = get_differences_at_each_step(sequences)
        first_elements.append(differences_at_each_step[0])

        while not all(map(lambda x: x == 0, differences_at_each_step)):
            differences_at_each_step: List[int] = get_differences_at_each_step(
                differences_at_each_step
            )
            first_elements.append(differences_at_each_step[0])

        answer += functools.reduce(lambda x, y: y - x, reversed(first_elements))

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
