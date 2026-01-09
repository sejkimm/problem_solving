from typing import List


class Solution:
    @staticmethod
    def isCircularSentence(sentence: str) -> bool:
        words: List[str] = sentence.split(" ")
        prev_last_char: str = words[0][-1]

        if words[0][0] != words[-1][-1]:
            return False

        for word in words[1:]:
            if word[0] != prev_last_char:
                return False

            prev_last_char = word[-1]

        return True


def main():
    assert Solution.isCircularSentence("leetcode exercises sound delightful") == True
    assert Solution.isCircularSentence("eetcode") == True
    assert Solution.isCircularSentence("Leetcode is cool") == False


if __name__ == "__main__":
    main()
