from typing import List, Optional


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cursor: int = 0
        prev_num: Optional[int] = None

        for _, num in enumerate(nums):
            nums[cursor] = num

            if not (prev_num is not None and prev_num == num):
                cursor += 1

            prev_num = num

        return cursor
