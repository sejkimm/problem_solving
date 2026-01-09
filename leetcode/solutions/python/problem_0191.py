class Solution:
    def hammingWeight(self, n: int) -> int:
        n_setbit: int = 0

        while n > 0:
            n_setbit += n & 1

            # Slower operation:
            #   n_setbit += n % 2

            n >>= 1

        return n_setbit
