from typing import Tuple

class Solution:
    @staticmethod
    def compressedString(word: str) -> str:
        cursor: Tuple[str, int] = (word[0], 1)
        comp: str = ""

        for current_char in word[1:]:
            if current_char == cursor[0] and cursor[1] < 9:
                cursor = (cursor[0], cursor[1] + 1)
                continue
                
            comp += f"{cursor[1]}{cursor[0]}"
            cursor = (current_char, 1)
            
        comp += f"{cursor[1]}{cursor[0]}"
        return comp


def main():
    assert Solution.compressedString("abcde") == "1a1b1c1d1e"
    assert Solution.compressedString("aaaaaaaaaaaaaabb") == "9a5a2b"

if __name__ == "__main__":
    main()