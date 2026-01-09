from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = list()

        for char in s:
            if char in ["{", "(", "["]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if not (
                    (top == "{" and char == "}")
                    or (top == "[" and char == "]")
                    or (top == "(" and char == ")")
                ):
                    return False

        return len(stack) == 0
