from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createTreeNode(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        root: TreeNode = TreeNode(val=nums[len(nums) // 2])
        root.left = self.createTreeNode(nums[0 : len(nums) // 2])
        root.right = self.createTreeNode(nums[len(nums) // 2 + 1 :])

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        return self.createTreeNode(nums)
