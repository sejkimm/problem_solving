class Solution:
    def isPalindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1

        while left < right:
            while not s[left].isalnum():
                left += 1

                if left >= len(s) - 1:
                    return True

            while not s[right].isalnum():
                right -= 1

                if right <= 0:
                    return True

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
