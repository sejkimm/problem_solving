from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        if k < 1 or len(nums) == 1:
            return

        temp_nums: List[int] = nums[((-1) * k) :]
        nums[k:] = nums[: len(nums) - k]
        nums[0:k] = temp_nums
