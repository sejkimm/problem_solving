class Solution:
    def reverseBits(self, n: int) -> int:
        output: int = 0

        for digit in range(31, -1, -1):
            output += (n % 2) * (2**digit)
            digit -= 1
            n //= 2

        return output

    # More Bitwise solution
    # n = (n >> 16) | (n << 16)

    # n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
    # n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
    # n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
    # n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
