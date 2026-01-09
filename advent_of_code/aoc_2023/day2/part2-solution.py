import os
import typing


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
        max_green: int = 0
        max_blue: int = 0
        max_red: int = 0

        input_line_split: list[str] = input_line.split("Game ")[1].split(":")
        color_strings: list[str] = input_line_split[1].split(";")

        for color_string in color_strings:
            color_parsed: typing.Dict[str, int] = parse_color(color_string)

            max_green = max(max_green, color_parsed["green"])
            max_blue = max(max_blue, color_parsed["blue"])
            max_red = max(max_red, color_parsed["red"])

        answer += max_green * max_blue * max_red

    return answer


def main():
    input_file_name = "input.txt"
    # input_file_name = "part2-input-example.txt"
    input_file_path = os.path.join(os.path.dirname(__file__), input_file_name)

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        input_lines: list[str] = input_file.readlines()

        answer: int = solve(input_lines)

        print(f"answer : {answer}")


if __name__ == "__main__":
    main()
