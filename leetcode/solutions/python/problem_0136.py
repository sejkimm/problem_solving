from typing import List, Set


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occurrences: Set[int] = set()

        for num in nums:
            if num in occurrences:
                occurrences.remove(num)
            else:
                occurrences.add(num)

        return list(occurrences)[0]
    
        # More Bitwise Solution:
        # result = 0
        # for num in nums:
        #     result ^= num
        # return result