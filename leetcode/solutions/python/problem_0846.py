from collections import defaultdict
from typing import List, Dict
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        hand_count: Dict = defaultdict(int)
        for card in hand:
            hand_count[card] += 1

        cards = list(hand_count.keys())
        heapq.heapify(cards)

        while cards:
            lowest_card = cards[0]

            for target_card in range(lowest_card, lowest_card + groupSize):
                if hand_count[target_card] < 1:
                    return False

                hand_count[target_card] -= 1

                if hand_count[target_card] < 1:
                    if target_card != cards[0]:
                        return False
                    heapq.heappop(cards)

        return True
