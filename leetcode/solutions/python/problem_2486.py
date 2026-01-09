class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_idx = 0
        t_idx = 0

        while t_idx < len(t) and s_idx < len(s):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                t_idx += 1
            else:
                s_idx += 1

        return len(t) - t_idx
