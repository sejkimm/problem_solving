import os


def get_digits_from_string(input_string: str) -> list[int]:
    digits: list[int] = []

    for character in input_string:
        if character.isdigit():
            digits.append(int(character))

    return digits


def solve(input_strings: list[str]) -> int:
    calibration: int = 0

    for input_string in input_strings:
        digits: list[int] = get_digits_from_string(input_string)

        first_digit = digits[0]
        last_digit = digits[-1]

        two_digit = first_digit * 10 + last_digit

        calibration += two_digit

    return calibration


def main():
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    answer: int = 0

    with open(input_file_path, "r") as input_file:
        answer = solve(input_file.read().splitlines())

    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
