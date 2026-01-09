from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return list()

        range_start: int = nums[0]
        prev: int = nums[0]

        answer: List[str] = list()

        for num in nums:
            if num > prev + 1:
                if range_start == prev:
                    answer.append(f"{range_start}")
                else:
                    answer.append(f"{range_start}->{prev}")

                range_start = num

            prev = num

        if range_start == prev:
            answer.append(f"{range_start}")
        else:
            answer.append(f"{range_start}->{prev}")

        return answer
