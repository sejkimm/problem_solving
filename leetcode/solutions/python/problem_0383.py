from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        occurrences: defaultdict = defaultdict(int)

        for ransomChar in ransomNote:
            occurrences[ransomChar] += 1

        for magazineChar in magazine:
            if magazineChar in occurrences and occurrences[magazineChar] >= 1:
                occurrences[magazineChar] -= 1

        return sum(occurrences.values()) == 0
