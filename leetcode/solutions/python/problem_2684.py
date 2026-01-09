from typing import List

class Solution:
    @staticmethod
    def maxMoves(grid: List[List[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        cache: List[List[int]] = [[1 for _ in range(n)] for _ in range(m)]

        for current_col in reversed(range(0, n)):
            max_next_col_step: List[int] = [0 for _ in range(m)]
            for current_row in range(0, m):
                for step_indicator in [(-1, 1), (0, 1), (1, 1)]:
                    target_row: int = current_row-step_indicator[0]
                    target_col: int = current_col-step_indicator[1]

                    if ((target_row < 0)
                        or (target_col < 0)
                        or (target_row >= m)
                        or (target_col >= n)
                    ):
                        continue
                    
                    if grid[current_row][current_col] > grid[target_row][target_col]:
                        max_next_col_step[target_row] = max(max_next_col_step[target_row], cache[current_row][current_col])
            
            for row, max_step in enumerate(max_next_col_step):
                cache[row][current_col-1] += max_step

        max_move: int = max(row[0] for row in cache)

        return max_move - 1
        

def main():
    assert Solution.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]) == 3
    assert Solution.maxMoves([[3,2,4],[2,1,9],[1,1,7]]) == 0
    assert Solution.maxMoves([[2,625152,3,5],[625151,625152,9,3]]) == 1
    assert Solution.maxMoves([[19,13,5,10,30,19,28],[17,9,2,26,9,24,3],[1,12,13,21,18,12,8],[17,10,13,15,19,30,6],[14,5,24,24,17,22,6]]) == 6

if __name__ == "__main__":
    main()
