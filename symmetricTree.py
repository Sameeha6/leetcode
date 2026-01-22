# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        def isMirror(left, right):
            # both null
            if not left and not right:
                return True

            # one null
            if not left or not right:
                return False

            # values differ
            if left.val != right.val:
                return False

            # check mirror children
            return isMirror(left.left, right.right) and \
                   isMirror(left.right, right.left)

        return isMirror(root.left, root.right)