from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations: List[int] = sorted(citations, reverse=True)
        h_index: int = 0

        for idx, citation in enumerate(citations):
            if idx > citation:
                break

            h_index = min(idx + 1, citation)

        return h_index
