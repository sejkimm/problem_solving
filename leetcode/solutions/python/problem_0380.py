from typing import Dict, List
from random import randint


class RandomizedSet:

    def __init__(self):
        self._hashmap: Dict[int, int] = {}
        self._indexed_list: List[int] = []

    def insert(self, val: int) -> bool:
        if val in self._hashmap:
            return False

        self._hashmap[val] = len(self._indexed_list)
        self._indexed_list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self._hashmap:
            return False

        index = self._hashmap[val]
        last_val = self._indexed_list[-1]

        self._indexed_list[index] = last_val
        self._hashmap[last_val] = index

        _ = self._indexed_list.pop()
        _ = self._hashmap.pop(val)

        return True

    def getRandom(self) -> int:
        rand_index: int = randint(0, len(self._indexed_list) - 1)

        return self._indexed_list[rand_index]
