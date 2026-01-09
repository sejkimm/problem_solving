from typing import List, Dict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occurrences: Dict[int, int] = dict()

        for idx, num in enumerate(nums):
            if num in occurrences:
                if idx - occurrences[num] <= k:
                    return True

            occurrences[num] = idx

        return False
