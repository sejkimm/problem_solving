from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search_and_replace(self, word: str):
        node = self.root

        for idx, char in enumerate(word):
            if char not in node.children:
                return word

            node = node.children[char]

            if node.is_end:
                return word[: (idx + 1)]

        return None


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        replaced_sentence_list = []

        for word in sentence.split():
            replaced_word = trie.search_and_replace(word)
            replaced_sentence_list.append(replaced_word if replaced_word else word)

        return " ".join(replaced_sentence_list)
