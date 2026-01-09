from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def largestCombination(candidates: List[int]) -> int:
        binary_digits_count = defaultdict(int)

        for candidate in candidates:
            temp_candidate = candidate

            digit = 0
            while temp_candidate > 0:
                if temp_candidate % 2 == 1:
                    binary_digits_count[digit] += 1
                temp_candidate = temp_candidate >> 1
                digit += 1

        try:
            answer = max(binary_digits_count.values())
        except ValueError:
            answer = 0

        return answer


def main():
    assert Solution.largestCombination([16, 17, 71, 62, 12, 24, 14]) == 4
    assert Solution.largestCombination([8, 8]) == 2
    assert Solution.largestCombination([8, 7]) == 1


if __name__ == "__main__":
    main()
