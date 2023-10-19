# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check_node_in_root(self, node, nodes):
        for existing_node in nodes:
            if existing_node.val == node.val:
                return True
        return False
        
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if not root or self.check_node_in_root(root, nodes):
            return root
        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right
        