class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(" ")):
            return False

        return len(set(pattern)) == len(set(s.split(" "))) == len(set(zip(list(pattern), s.split(" "))))
