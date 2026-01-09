from typing import List, Optional

# Kind of a verbal and suboptimal solution.


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag_string: List[List[Optional[str]]] = [[None for _ in range(len(s))] for _ in range(numRows)]

        in_zigzag_pattern: bool = False
        row_cursor: int = 0
        col_cursor: int = 0

        if numRows == 1:
            return s

        for char in s:
            zigzag_string[row_cursor][col_cursor] = char

            if in_zigzag_pattern:
                row_cursor -= 1
                col_cursor += 1

                if row_cursor <= 0:
                    in_zigzag_pattern = False
            else:
                row_cursor += 1

                if row_cursor == numRows - 1:
                    in_zigzag_pattern = True

        new_string: str = ""

        for row in zigzag_string:
            for char in row:
                if char is not None:
                    new_string += char

        return new_string
