from typing import List


class Solution:
    @staticmethod
    def countSquares(matrix: List[List[int]]) -> int:
        row_len, col_len = len(matrix), len(matrix[0])
        cache = [[0] * col_len for _ in range(row_len)]
        square_count = 0

        for row_idx in range(row_len):
            for col_idx in range(col_len):
                if matrix[row_idx][col_idx] == 1:
                    if row_idx == 0 or col_idx == 0:
                        cache[row_idx][col_idx] = 1
                    else:
                        cache[row_idx][col_idx] = (
                            min(
                                cache[row_idx - 1][col_idx],
                                cache[row_idx][col_idx - 1],
                                cache[row_idx - 1][col_idx - 1],
                            )
                            + 1
                        )

                    square_count += cache[row_idx][col_idx]

        return square_count


def main():
    assert Solution.countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]) == 15
    assert Solution.countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]) == 7


if __name__ == "__main__":
    main()
