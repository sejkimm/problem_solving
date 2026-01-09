import os
from typing import List, Dict, Tuple, Optional

INF: int = 1_000_000_000

Tile = Dict[str, Optional[List[Tuple[int, int]]]]

tile_type: Tile = {
    "S": [(1, 0), (0, 1), (-1, 0), (0, -1)],
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
}


def parse_tile_map(input_lines: List[str]) -> Tuple[List[List[Tile]], Tuple[int, int]]:
    tile_map: List[List[Tile]] = []

    for row_idx, input_line in enumerate(input_lines):
        stripped_line: str = input_line.strip()
        row: List[Tile] = []

        for col_idx, char in enumerate(stripped_line):
            row.append(tile_type[char])
            if char == "S":
                starting_point: Tuple[int, int] = (row_idx, col_idx)

        tile_map.append(row)

    return (tile_map, starting_point)


def solve(input_lines: List[str]) -> int:
    answer: int = 0

    tile_info: Tuple[List[List[Tile]], Tuple[int, int]] = parse_tile_map(input_lines)

    tile_map: List[List[Tile]] = tile_info[0]
    starting: Tuple[int, int] = tile_info[1]

    distance_from_starting: List[List[int]] = list(map(lambda col: [INF] * len(col), tile_map))
    distance_from_starting[starting[0]][starting[1]] = 0

    for starting_direction in tile_map[starting[0]][starting[1]]:
        if (starting[0] + starting_direction[0] < 0 or starting[1] + starting_direction[1] < 0) or (
            tile_map[starting[0] + starting_direction[0]][starting[1] + starting_direction[1]] == []
        ):
            continue

        bfs_queue: List[Tuple[int, int]] = [(starting[0] + starting_direction[0], starting[1] + starting_direction[1])]
        current_distance: int = 1

        while len(bfs_queue) > 0:
            current_node = bfs_queue.pop(0)
            distance_from_starting[current_node[0]][current_node[1]] = current_distance

            current_distance: int = current_distance + 1

            if current_node == starting:
                continue

            for direction in tile_map[current_node[0]][current_node[1]]:
                next_node: Tuple[int, int] = (current_node[0] + direction[0], current_node[1] + direction[1])

                try:
                    if current_distance < distance_from_starting[next_node[0]][next_node[1]]:
                        distance_from_starting[next_node[0]][next_node[1]] = current_distance
                        bfs_queue.append(next_node)
                except IndexError:
                    pass

    from pprint import pprint

    pprint(distance_from_starting)

    return answer


def main(**kwargs):
    input_file_path = os.path.join(os.path.dirname(__file__), kwargs["input_file_name"])

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        input_lines: List[str] = input_file.readlines()

        answer: int = solve(input_lines)

        print(f"answer : {answer}")

    return answer


if __name__ == "__main__":
    # INPUT_FILE_NAME: str = "input.txt"
    INPUT_FILE_NAME: str = "part2_example_input_1.txt"
    main(input_file_name=INPUT_FILE_NAME)
