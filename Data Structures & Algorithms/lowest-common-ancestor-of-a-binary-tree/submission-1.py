# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Findf the path down to p/q
        def findPath(node, target, path):
            if not node: 
                return False
            
            path.append(node)
            if node == target:
                return True
            
            if findPath(node.left, target, path) or findPath(node.right, target, path):
                return True
            
            path.pop()
            return False

        pathP, pathQ = [],[]
        findPath(root, p, pathP)
        findPath(root, q, pathQ)

                #Find the LCA
        lca = None
        for a, b in zip(pathP, pathQ):
            if a!= b:
                break
            lca = a
        return lca

        