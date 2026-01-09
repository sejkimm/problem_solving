from typing import Set


class Solution:
    def sumDigitSquare(self, n: int) -> int:
        sumValue: int = 0

        while n != 0:
            sumValue += (n % 10) ** 2
            n //= 10

        return sumValue

    def isHappy(self, n: int) -> bool:
        seen: Set[int] = set()

        while n != 1:
            n = self.sumDigitSquare(n)

            if n in seen:
                return False

            seen.add(n)

        return True
