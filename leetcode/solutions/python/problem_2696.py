from typing import List

class Solution:
    @staticmethod
    def minLength(s: str) -> int:
        s_stack: List[str] = []

        for c in s:
            if len(s_stack) == 0:
                s_stack.append(c)
            elif (s_stack[-1] == 'A' and c == 'B') or (s_stack[-1] == 'C' and c == 'D'):
                s_stack.pop()
            else:
                s_stack.append(c)
        
        return len(s_stack)


if __name__ == "__main__":
    assert 2 == Solution.minLength("ABFCACDB")
    assert 5 == Solution.minLength("ACBBD")
