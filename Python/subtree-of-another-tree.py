# Time:  O(m * n), m is the number of nodes of s, n is the number of nodes of t
# Space: O(h), h is the height of s

# Given two non-empty binary trees s and t,
# check whether tree t has exactly the same structure and
# node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
#
#      3
#     / \
#   4   5
#   / \
#  1   2
# Given tree t:
#   4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#
#      3
#     / \
#   4   5
#   / \
#  1   2
#     /
#   0
# Given tree t:
#   4
#   / \
#  1   2
# Return false.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, b):
        if s == None:
            if b != None:
                return False
            else:
                return True
        else:
            return self.isSame(s, b) or (self.isSubtree(s.left, b) or self.isSubtree(s.right, b))
        
    def isSame(self, s, b):
        if s == None and b == None:
            return True
        if s != None and b != None:
            return s.val == b.val and self.isSame(s.left, b.left) and self.isSame(s.right, b.right)
        else:
            return False
        
        
    def
    
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val == y.val and \
                   isSame(x.left, y.left) and \
                   isSame(x.right, y.right)

        def preOrderTraverse(s, t):
            return s != None and \
                   (isSame(s, t) or \
                    preOrderTraverse(s.left, t) or \
                    preOrderTraverse(s.right, t))
        
        return preOrderTraverse(s, t)
