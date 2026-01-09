class Solution:
    @staticmethod
    def rotateString(s: str, goal: str) -> bool:
        for idx in range(len(s)):
            if s == goal[idx:] + goal[0:idx]:
                return True

        return False


def main():
    assert Solution.rotateString("abcde", "cdeab") is True
    assert Solution.rotateString("abcde", "abced") is False


if __name__ == "__main__":
    main()
