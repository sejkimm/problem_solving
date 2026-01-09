from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        reachable_nums: List[int] = [idx + num for idx, num in enumerate(nums)]
        current_end: int = 0
        furthest: int = 0
        jump_count: int = 0

        for current_idx in range(len(nums) - 1):
            furthest = max(furthest, reachable_nums[current_idx])

            if current_idx == current_end:
                jump_count += 1
                current_end = furthest

                if current_end >= len(nums) - 1:
                    break

        return jump_count
