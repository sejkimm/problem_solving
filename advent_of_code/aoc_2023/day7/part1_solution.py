import os
from enum import Enum
from typing import List, Type


class CardStrength(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


class Hand:
    def __init__(self, cards: List[int], bid: int):
        self.cards: List[int] = cards
        self.bid: int = bid

        self.card_strength: CardStrength = self.__get_card_strength(cards)

    @property
    def cards(self) -> List[int]:
        return self.__cards

    @cards.setter
    def cards(self, cards: List[int]) -> None:
        self.__cards = cards

    def __get_card_strength(self, cards: List[int]) -> CardStrength:
        card_counter = [0] * 15
        strength: CardStrength = None

        for card in cards:
            card_counter[card] += 1

        if max(card_counter) == 5:
            strength = CardStrength.FIVE_OF_A_KIND
        elif max(card_counter) == 4:
            strength = CardStrength.FOUR_OF_A_KIND
        elif max(card_counter) == 3:
            if 2 in card_counter:
                strength = CardStrength.FULL_HOUSE
            else:
                strength = CardStrength.THREE_OF_A_KIND
        else:
            match len(list(filter(lambda x: x == 2, card_counter))):
                case 2:
                    strength = CardStrength.TWO_PAIR
                case 1:
                    strength = CardStrength.ONE_PAIR
                case 0:
                    strength = CardStrength.HIGH_CARD

        return strength

    def __lt__(self, other: Type["Hand"]) -> bool:
        if self.card_strength.value < other.card_strength.value:
            return True
        elif self.card_strength.value > other.card_strength.value:
            return False
        else:
            for idx, card in enumerate(self.cards):
                if card < other.cards[idx]:
                    return True
                elif card > other.cards[idx]:
                    return False

    def __repr__(self) -> str:
        return f"{self.card_strength}, {self.cards}, {self.bid}"

def solve(card_inputs: List[str]) -> int:
    answer: int = 0

    hands: List[Hand] = []

    for card_input in card_inputs:
        cards: List[int] = []
        card_string: str
        bid_string: str

        card_string, bid_string = card_input.split(" ")

        for card in card_string:
            if card.isdigit():
                cards.append(int(card))
            if card == "T":
                cards.append(10)
            elif card == "J":
                cards.append(11)
            elif card == "Q":
                cards.append(12)
            elif card == "K":
                cards.append(13)
            elif card == "A":
                cards.append(14)

        hands.append(Hand(cards, int(bid_string)))

    for rank, hands in enumerate(sorted(hands, reverse=False)):
        # print(f"{rank + 1} : {hands}")
        answer += hands.bid * (rank + 1)

    return answer


def main(**kwargs):
    input_file_path = os.path.join(os.path.dirname(__file__), kwargs["input_file_name"])

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        card_inputs: List[str] = input_file.readlines()

        answer: int = solve(card_inputs)

        print(f"answer : {answer}")

    return answer


if __name__ == "__main__":
    INPUT_FILE_NAME: str = "input.txt"
    # INPUT_FILE_NAME: str = "example_input.txt"
    main(input_file_name=INPUT_FILE_NAME)
