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

    races: List[Race] = list()

    times: List[int] = list(map(int, re.findall(r"(\d+)", race_inputs[0])))
    distances: List[int] = list(map(int, re.findall(r"(\d+)", race_inputs[1])))

    races = [Race(time, distance) for time, distance in zip(times, distances)]

    for race in races:
        possible_answer: int = 0

        for push_time in range(race.time):
            if push_time * (race.time - push_time) > race.distance:
                possible_answer += 1

        answer = answer * possible_answer if answer != 0 else possible_answer

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
