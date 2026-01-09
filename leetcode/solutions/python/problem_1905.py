from typing import List, Tuple


class Solution:
    @staticmethod
    def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:

        num_island: int = 0
        m: int = len(grid1)
        n: int = len(grid1[0])

        directions: List[Tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def floodfill(row_idx: int, col_idx: int) -> bool:
            if row_idx < 0 or col_idx < 0 or row_idx >= m or col_idx >= n:
                return True

            if grid2[row_idx][col_idx] == 0:
                return True

            grid2[row_idx][col_idx] = 0

            return_value: bool = True

            for direction in directions:
                return_value = (
                    floodfill(row_idx + direction[0], col_idx + direction[1])
                    and return_value
                )

            if grid1[row_idx][col_idx] == 0:
                return_value = False

            return return_value

        for row_idx in range(m):
            for col_idx in range(n):
                if grid2[row_idx][col_idx] == 1:
                    if floodfill(row_idx, col_idx):
                        num_island += 1

        return num_island


if __name__ == "__main__":
    assert 3 == Solution.countSubIslands(
        grid1=[
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1],
        ],
        grid2=[
            [1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 1, 0, 0, 0],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0],
        ],
    )

    assert 2 == Solution.countSubIslands(
        grid1=[
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
        ],
        grid2=[
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1],
        ],
    )
