import os
import typing

MAX_RED: int = 12
MAX_GREEN: int = 13
MAX_BLUE: int = 14


def parse_color(color_strings: str) -> typing.Dict[str, int]:
    each_color: list[str] = color_strings.split(",")

    colors: typing.Dict[str, int] = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for color in each_color:
        if "green" in color:
            colors["green"] = int(color.split("green")[0])
        elif "blue" in color:
            colors["blue"] = int(color.split("blue")[0])
        elif "red" in color:
            colors["red"] = int(color.split("red")[0])

    return colors


def solve(input_lines: list[str]) -> int:
    answer: int = 0

    for input_line in input_lines:
        input_line_split: list[str] = input_line.split("Game ")[1].split(":")
        game_number: int = int(input_line_split[0])
        color_strings: list[str] = input_line_split[1].split(";")

        is_valid: bool = True

        for color_string in color_strings:
            color_parsed: typing.Dict[str, int] = parse_color(color_string)

            if (
                color_parsed["red"] > MAX_RED
                or color_parsed["green"] > MAX_GREEN
                or color_parsed["blue"] > MAX_BLUE
            ):
                is_valid = False
                break

        if is_valid:
            answer += game_number

    return answer


def main():
    input_file_name = "input.txt"
    input_file_path = os.path.join(os.path.dirname(__file__), input_file_name)

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        input_lines: list[str] = input_file.readlines()

        answer: int = solve(input_lines)

        print(f"answer : {answer}")


if __name__ == "__main__":
    main()
