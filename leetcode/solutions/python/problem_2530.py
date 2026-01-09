import heapq

from typing import List


class Solution:
    @staticmethod
    def maxKelements(nums: List[int], k: int) -> int:
        score: int = 0
        max_heap = list(map(lambda x: (-1) * x, nums))
        heapq.heapify(max_heap)

        for _ in range(k):
            max_value = (-1) * heapq.heappop(max_heap)
            score += max_value
            heapq.heappush(max_heap, (-1) * (max_value // 3 + (1 if max_value % 3 != 0 else 0)))

        return score


if __name__ == "__main__":
    assert Solution.maxKelements([10, 10, 10, 10, 10], 5) == 50
    assert Solution.maxKelements([1, 10, 3, 3, 3], 3) == 17
    assert Solution.maxKelements([1], 3) == 3
    assert (
        Solution.maxKelements(
            [
                881784984,
                829998714,
                730002802,
                56524562,
                120336848,
                548306998,
                801116106,
                828640251,
                519131180,
                819176153,
                476262254,
                15904939,
                540793851,
                53572296,
                259044378,
                491129827,
                561147559,
                205793082,
                967833729,
            ],
            16,
        )
        == 9888530217
    )
