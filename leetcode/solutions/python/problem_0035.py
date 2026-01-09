from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_idx: int = 0
        end_idx: int = len(nums) - 1

        while start_idx <= end_idx:
            mid_idx: int = (start_idx + end_idx) // 2

            if nums[mid_idx] > target:
                end_idx = mid_idx - 1
            elif nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] < target:
                start_idx = mid_idx + 1

        return start_idx
