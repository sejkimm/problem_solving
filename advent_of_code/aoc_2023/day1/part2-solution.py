import typing
import os
import re

DIGITS_IN_LETTERS: dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_digits_index_from_string(input_string: str) -> list[typing.Tuple[int, int]]:
    digits_index: list[typing.Tuple[int, int]] = []

    for idx in range(len(input_string)):
        if input_string[idx].isdigit():
            digits_index.append((idx, int(input_string[idx])))

    for letter, digit in DIGITS_IN_LETTERS.items():
        for match in re.finditer(letter, input_string):
            digits_index.append((match.start(), digit))

    digit_index_sorted: list[typing.Tuple[int, int]] = sorted(
        digits_index, key=lambda x: x[0]
    )

    return digit_index_sorted


def solve(input_strings: list[str]) -> int:
    calibration: int = 0

    for input_string in input_strings:
        digits_index: list[typing.Tuple[int, int]] = get_digits_index_from_string(
            input_string
        )

        first_digit = digits_index[0][1]
        last_digit = digits_index[-1][1]

        two_digit = first_digit * 10 + last_digit

        calibration += two_digit

    return calibration


def main():
    # file_name: str = "part2-input-example.txt"
    file_name: str = "input.txt"
    input_file_path: os.path = os.path.join(os.path.dirname(__file__), file_name)

    answer: int = 0

    with open(input_file_path, "r") as input_file:
        answer = solve(input_file.read().splitlines())

    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
