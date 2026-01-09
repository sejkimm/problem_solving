from typing import List, Dict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remains_of_accumulated_sum: List = [
            0,
        ]

        for idx, num in enumerate(nums):
            remains_of_accumulated_sum.append((remains_of_accumulated_sum[idx] + num) % k)

        remains_occurred: Dict[int, int] = {}

        for idx, remain in enumerate(remains_of_accumulated_sum):
            if remain in remains_occurred:
                if remains_occurred[remain] + 1 < idx:
                    return True
            else:
                remains_occurred[remain] = idx

        return False
