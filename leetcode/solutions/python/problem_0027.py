from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cursor: int = 0

        for _, num in enumerate(nums):
            if num != val:
                nums[cursor] = num
                cursor += 1

        return cursor
