import os
import re
from typing import List, Dict, Type, Optional, Tuple


class Race:
    def __init__(self, time: int, distance: int):
        self.time: int = time
        self.distance: int = distance

    def __repr__(self):
        return f"Race(time: {self.time}, distance: {self.distance})"


def solve(race_inputs: List[str]) -> int:
    answer: int = 0

    time: int = int("".join(re.findall(r"(\d+)", race_inputs[0])))
    distance: int = int("".join(re.findall(r"(\d+)", race_inputs[1])))

    race = Race(time, distance)

    for push_time in range(race.time):
        if push_time * (race.time - push_time) > race.distance:
            answer += 1

    return answer


def main(**kwargs):
    input_file_path = os.path.join(os.path.dirname(__file__), kwargs["input_file_name"])

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        race_inputs: List[str] = input_file.readlines()

        answer: int = solve(race_inputs)

        print(f"answer : {answer}")

    return answer


if __name__ == "__main__":
    INPUT_FILE_NAME: str = "input.txt"
    # INPUT_FILE_NAME: str = "example_input.txt"
    main(input_file_name=INPUT_FILE_NAME)
