from typing import List, Set


class Solution:
    @staticmethod
    def longestSquareStreak(nums: List[int]) -> int:
        nums_set: Set[int] = set(nums)
        longest_length: int = 0

        for num in nums:
            current_length: int = 0
            cursor: int = num

            while cursor in nums_set:
                current_length += 1
                cursor = cursor ** 2

            longest_length = max(longest_length, current_length)
        

        return longest_length if longest_length > 1 else -1


def main():
    assert Solution.longestSquareStreak([4, 3, 6, 16, 8, 2]) == 3
    assert Solution.longestSquareStreak([2, 3, 5, 6, 7]) == -1

if __name__ == "__main__":
    main()
