import os
import typing

ADJACENT_X: typing.List[int] = [-1, -1, -1, 0, 0, 1, 1, 1]
ADJACENT_Y: typing.List[int] = [-1, 0, 1, -1, 1, -1, 0, 1]


def solve(machine_map: typing.List[typing.List[str]]) -> int:
    answer: int = 0

    buffer: typing.List[str] = []

    for cursor_y, target_row in enumerate(machine_map):
        buffer = []
        is_symbol_adjacent: bool = False

        for cursor_x, target_char in enumerate(target_row):
            if target_char.isdigit():
                buffer.append(target_char)

                for search_idx in range(8):
                    search_x = cursor_x + ADJACENT_X[search_idx]
                    search_y = cursor_y + ADJACENT_Y[search_idx]

                    try:
                        adjacent_char: str = machine_map[search_y][search_x]

                        if not adjacent_char.isdigit() and adjacent_char != ".":
                            is_symbol_adjacent = True
                            break
                    except IndexError:
                        pass

            else:
                if len(buffer) > 0 and is_symbol_adjacent:
                    answer += int("".join(buffer))
                buffer = []
                is_symbol_adjacent = False

    return answer


def main():
    input_file_name = "input.txt"
    # input_file_name = "part1-input-example.txt"
    input_file_path = os.path.join(os.path.dirname(__file__), input_file_name)

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        machine_map: typing.List[typing.List[str]] = []

        input_lines: list[str] = input_file.readlines()

        for input_line in input_lines:
            machine_map.append(list(input_line.strip()))

        answer: int = solve(machine_map)

        print(f"answer : {answer}")


if __name__ == "__main__":
    main()
