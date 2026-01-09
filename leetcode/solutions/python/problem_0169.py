from collections import defaultdict
from typing import Dict, List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurrences: Dict[int, int] = defaultdict(int)

        for _, num in enumerate(nums):
            occurrences[num] += 1

        for key, value in occurrences.items():
            if value >= ((len(nums) + 1) // 2):
                return key
