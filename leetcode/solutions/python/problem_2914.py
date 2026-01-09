class Solution:
    @staticmethod
    def minChanges(s: str) -> int:
        changes: int = 0

        for idx in range(len(s) // 2):
            odd_idx: int = idx * 2 + 1
            even_idx: int = idx * 2

            if s[odd_idx] != s[even_idx]:
                changes += 1

        return changes


def main():
    assert Solution.minChanges("1001") == 2
    assert Solution.minChanges("10") == 1
    assert Solution.minChanges("0000") == 0


if __name__ == "__main__":
    main()
