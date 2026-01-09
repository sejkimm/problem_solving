from typing import List, Set


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champion_candidates: Set[int] = set(range(n))

        for edge in edges:
            if edge[1] in champion_candidates:
                champion_candidates.remove(edge[1])

        if len(champion_candidates) != 1:
            return -1

        return list(champion_candidates)[0]
