class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_cursor: int = 0
        s_cursor: int = 0

        while t_cursor < len(t):
            if s_cursor >= len(s):
                return True

            if t[t_cursor] == s[s_cursor]:
                s_cursor += 1

            t_cursor += 1

        if s_cursor == len(s):
            return True
        else:
            return False
