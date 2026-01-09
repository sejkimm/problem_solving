class Solution:
    @staticmethod
    def makeFancyString(s: str) -> str:
        last_char: str = s[0]
        streak: int = 1
        fancy_string: str = s[0]

        for char in s[1:]:
            if char == last_char:
                streak += 1
            else:
                last_char = char
                streak = 1

            if streak < 3:
                fancy_string += char

        return fancy_string


def main():
    assert Solution.makeFancyString("leeetcode") == "leetcode"
    assert Solution.makeFancyString("aaabaaaa") == "aabaa"
    assert Solution.makeFancyString("aab") == "aab"


if __name__ == "__main__":
    main()
