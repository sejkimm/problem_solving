from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # O(n^2)
        # for first_idx in range(len(nums)):
        # for second_idx in range(first_idx+1, len(nums)):
        # if (nums[first_idx] + nums[second_idx]) == target:
        # return [first_idx, second_idx]

        # O(n)
        occurrences: Dict[int, int] = {}

        for idx, num in enumerate(nums):
            if target - num in occurrences:
                return [occurrences[target - num], idx]

            occurrences[num] = idx
