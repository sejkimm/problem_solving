from typing import List, Dict

class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.is_last_node: bool = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, new_folder: List[str]) -> None:
        current_node = self.root

        for folder_dir in new_folder:
            if folder_dir not in current_node.children:
                current_node.children[folder_dir] = TrieNode()

            current_node = current_node.children[folder_dir]
        
        current_node.is_last_node = True
    
    def is_subdir(self, target_folder: List[str]) -> bool:
        current_node = self.root
        
        for folder_dir in target_folder:
            if current_node.is_last_node:
                return True
            
            if folder_dir in current_node.children:
                current_node = current_node.children[folder_dir]
            else:
                return False
        
        return False


class Solution:
    @staticmethod
    def removeSubfolders(folder: List[str]) -> List[str]:
        trie = Trie()
        folder_lists: List[List[str]] = sorted(list(map(lambda x: x.split('/')[1:], folder)), key=lambda l: len(l))
        subfolder_removed: List[str] = []

        for folder_list in folder_lists:
            if not trie.is_subdir(folder_list):
                trie.insert(folder_list)
                subfolder_removed.append('/' + '/'.join(folder_list))
        
        return subfolder_removed

def main():
    assert set(Solution.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])) == set(["/a","/c/d","/c/f"])
    assert set(Solution.removeSubfolders(["/a","/a/b/c","/a/b/d"])) == set(["/a"])
    assert set(Solution.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])) == set(["/a/b/c","/a/b/ca","/a/b/d"])

if __name__ == "__main__":
    main()