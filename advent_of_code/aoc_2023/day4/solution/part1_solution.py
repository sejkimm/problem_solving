import os
import re
from typing import List, Set


def solve(cards: List[str]) -> int:
    answer: int = 0

    for card in cards:
        card_without_index: List[str] = card.split(":")[1].split("|")

        winning_numbers: Set[int] = set(
            map(int, (re.findall(r"\d+", card_without_index[0])))
        )
        numbers_you_have: Set[int] = set(
            map(int, (re.findall(r"\d+", card_without_index[1])))
        )

        intersection_len = len(winning_numbers.intersection(numbers_you_have))

        answer += 2 ** (intersection_len - 1) if intersection_len > 0 else 0

    return answer


def main(**kwargs):
    input_file_path = os.path.join(os.path.dirname(__file__), kwargs["input_file_name"])

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        cards: List[str] = input_file.readlines()

        answer: int = solve(cards)

        print(f"answer : {answer}")

    return answer


if __name__ == "__main__":
    INPUT_FILE_NAME: str = "input.txt"
    main(input_file_name=INPUT_FILE_NAME)
