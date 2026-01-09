from typing import List


class Solution:
    @staticmethod
    def getMaximumXor(nums: List[int], maximumBit: int) -> List[int]:
        maximizing_k_list: List[int] = []
        maximum_bit_value: int = 2**maximumBit - 1
        current_xor_num: int = 0

        for num in nums:
            current_xor_num = current_xor_num ^ num
            maximizing_k_list.append(current_xor_num ^ maximum_bit_value)

        return list(reversed(maximizing_k_list))


def main():
    assert Solution.getMaximumXor([0, 1, 1, 3], 2) == [0, 3, 2, 3]
    assert Solution.getMaximumXor([2, 3, 4, 7], 3) == [5, 2, 6, 5]
    assert Solution.getMaximumXor([0, 1, 2, 2, 5, 7], 3) == [4, 3, 6, 4, 6, 7]


if __name__ == "__main__":
    main()
