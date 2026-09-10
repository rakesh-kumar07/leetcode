# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def postorder(node):
            nonlocal count
            if not node:
                return 0, 0  # (sum, total_nodes)

            left_sum, left_count = postorder(node.left)
            right_sum, right_count = postorder(node.right)

            subtree_sum = node.val + left_sum + right_sum
            subtree_count = 1 + left_count + right_count

            if subtree_sum // subtree_count == node.val:
                count += 1

            return subtree_sum, subtree_count

        postorder(root)
        return count        