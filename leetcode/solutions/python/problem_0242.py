from typing import Dict


class Solution:
    def count_occurrences(self, input_str: str) -> Dict[str, int]:
        occurrences: Dict[str, int] = {}

        for input_char in input_str:
            if input_char in occurrences:
                occurrences[input_char] += 1
            else:
                occurrences[input_char] = 1

        return occurrences

    def isAnagram(self, s: str, t: str) -> bool:
        s_occurrences: Dict[str, int] = self.count_occurrences(s)
        t_occurrences: Dict[str, int] = self.count_occurrences(t)

        return s_occurrences == t_occurrences
