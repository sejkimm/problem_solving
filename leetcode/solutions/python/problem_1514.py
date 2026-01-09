from collections import defaultdict
from heapq import heappop, heappush
from typing import Dict, List, Tuple, Set


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj_list: Dict[int, List[Tuple[int, float]]] = defaultdict(list)
        max_prob: Dict[int, float] = defaultdict(int)
        visited_node: Set[int] = set()

        for idx, edge in enumerate(edges):
            adj_list[edge[0]].append((edge[1], succProb[idx]))
            adj_list[edge[1]].append((edge[0], succProb[idx]))

        max_heap = [(-1.0, start_node)]
        max_prob[start_node] = 1.0

        while max_heap:
            current_prob, current_node = heappop(max_heap)
            current_prob = current_prob * (-1)

            if current_node == end_node:
                return current_prob

            if current_node in visited_node:
                continue

            visited_node.add(current_node)

            for next_node, edge_prob in adj_list[current_node]:
                if next_node not in visited_node:
                    next_prob = current_prob * edge_prob

                    if max_prob[next_node] < next_prob:
                        max_prob[next_node] = next_prob
                        heappush(max_heap, (next_prob * (-1), next_node))

        return max_prob[end_node]
