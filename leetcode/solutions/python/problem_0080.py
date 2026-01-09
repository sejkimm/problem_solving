from typing import List, Dict, Optional


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cursor: int = 0
        indicator: bool = True
        prev_nums: Dict[bool, Optional[int]] = {True: None, False: None}

        for _, num in enumerate(nums):
            nums[cursor] = num

            if not (prev_nums[indicator] is not None and prev_nums[indicator] == num):
                cursor += 1

            prev_nums[indicator] = num
            indicator = not indicator

        return cursor
