# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        
        # 1️⃣ Compute total sum
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        total = totalSum(root)
        self.max_product = 0
        
        # 2️⃣ DFS to compute subtree sums and max product
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            subtree_sum = node.val + left + right
            
            # try splitting here
            self.max_product = max(
                self.max_product,
                subtree_sum * (total - subtree_sum)
            )
            
            return subtree_sum
        
        dfs(root)
        return self.max_product % MOD
