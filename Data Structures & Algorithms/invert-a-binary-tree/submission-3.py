# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
# [1] pop this node
# [2,3] -> [3,2]
# [3,2]
# Pop 2
# [4,5] -> 5,4
# [3,5,4]
# Pop 4 and 5 leaf nodes
# [3]
# Pop 3
# 6,7 -> 7, 6
# [7,6]
# Pop 6 and 7 leaf node
# []
# return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


        