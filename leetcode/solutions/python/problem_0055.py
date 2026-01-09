from typing import List, Tuple


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step_ranges: List[Tuple[int, int]] = []

        for idx, num in enumerate(nums):
            step_ranges.append((idx, idx + num))

        step_ranges = sorted(step_ranges, key=lambda x: (x[1] * (-1), x[0]))
        effective_step_ranges: List[Tuple[int, int]] = [step_ranges[0]]

        for _, step_range in enumerate(step_ranges[1:]):
            if step_range[0] >= effective_step_ranges[-1][0] and step_range[1] <= effective_step_ranges[-1][1]:
                continue

            effective_step_ranges.append(step_range)

        effective_step_ranges = list(reversed(effective_step_ranges))
        prev_step_range = effective_step_ranges[0]

        for step_range in effective_step_ranges[1:]:
            if step_range[0] > prev_step_range[1]:
                return False

            prev_step_range = step_range

        return True
