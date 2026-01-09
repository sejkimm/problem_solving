from typing import Dict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map: Dict[str, str] = {}

        for idx, s_char in enumerate(s):
            if s_char in char_map:
                if char_map[s_char] != t[idx]:
                    return False
            else:
                if t[idx] in char_map.values():
                    return False

                char_map[s_char] = t[idx]

        return True

        # an elegant solution
        # return len(set(t)) == len(set(s)) == len(set(zip(s,t)))
