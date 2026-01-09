from typing import Set


class Solution:
    ## Optimal Soltuion (O(n) time complexity)
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length: int = 0
        occurrences: Set[str] = set()

        window_begin_idx = 0

        for window_end_idx, _ in enumerate(s):
            while s[window_end_idx] in occurrences:
                occurrences.remove(s[window_begin_idx])
                window_begin_idx += 1

            occurrences.add(s[window_end_idx])
            max_length = max(max_length, window_end_idx - window_begin_idx + 1)

        return max_length

    ## Suboptimal Solution (O(n^2) time complexity)
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     max_length: int = 0
    #     s_length: int = len(s)

    #     for start_idx in range(s_length):
    #         occurrences: Set[str] = set()
    #         cursor_idx: int = start_idx

    #         while cursor_idx <= s_length:
    #             if cursor_idx == s_length or s[cursor_idx] in occurrences:
    #                 max_length = max(max_length, len(occurrences))
    #                 break

    #             occurrences.add(s[cursor_idx])
    #             cursor_idx += 1

    #     return max_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring(""))
