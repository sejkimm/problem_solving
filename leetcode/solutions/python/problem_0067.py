class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_reversed: str = a[::-1]
        b_reversed: str = b[::-1]

        binary_sum: str = ""
        carry: bool = False

        for idx in range(max(len(a_reversed), len(b_reversed))):
            a_val: str = "0" if idx >= len(a_reversed) else a_reversed[idx]
            b_val: str = "0" if idx >= len(b_reversed) else b_reversed[idx]

            if a_val == "1" and b_val == "1":
                binary_sum += "1" if carry else "0"
                carry = True
            elif a_val == "0" and b_val == "0":
                binary_sum += "1" if carry else "0"
                carry = False
            else:
                if carry:
                    binary_sum += "0"
                    carry = True
                else:
                    binary_sum += "1"
                    carry = False

        if carry:
            binary_sum += "1"

        return binary_sum[::-1]
