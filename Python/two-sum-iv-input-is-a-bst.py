# Time:  O(n)
# Space: O(h)

# Given a Binary Search Tree and a target number,
# return true if there exist two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
# Example 2:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        class BSTIterator(object):
            def __init__(self, root, forward):
                self.__node = root
                self.__forward = forward
                self.__s = []
                self.__cur = None
                self.next()

            def val(self):
                return self.__cur
            
            def next(self):
                while self.__node or self.__s:
                    if self.__node:
                        self.__s.append(self.__node)
                        self.__node = self.__node.left if self.__forward else self.__node.right
                    else:
                        self.__node = self.__s.pop()
                        self.__cur = self.__node.val
                        self.__node = self.__node.right if self.__forward else self.__node.left
                        break


        if not root:
            return False
        left, right = BSTIterator(root, True), BSTIterator(root, False)
        while left.val() < right.val():
            if left.val() + right.val() == k:
                return True
            elif left.val() + right.val() < k:
                left.next()
            else:
                right.next()
        return False

    
    
    
    
    
    
    
    
    
    
#inorder array two points    
class Solution {
    public boolean findTarget(TreeNode root, int k) {
        List<Integer> nodes = new ArrayList<>();
        inOrder(root, nodes);
        
        int i = 0;
        int j = nodes.size() - 1;
        while (i < j) {
            int left = nodes.get(i);
            int right = nodes.get(j);
            if (left + right < k) {
                i++;
            } else if (left + right == k) {
                return true;
            } else {
                j--;
            }
        }
        return false;
    }
    
    private void inOrder(TreeNode root, List<Integer> nodes) {
        if (root == null) {
            return;
        }
        
        inOrder(root.left, nodes);
        nodes.add(root.val);
        inOrder(root.right, nodes);
    }
}


#bfs
class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        if (!root) return false;
        unordered_set<int> s;
        queue<TreeNode*> q{{root}};
        while (!q.empty()) {
          auto t = q.front(); q.pop();
          if (s.count(k - t->val)) return true;
          s.insert(t->val);
          if (t->left) q.push(t->left);
          if (t->right) q.push(t->right);
        }
        return false;
    }
};

#dfs
class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        if (!root) return false;
        unordered_set<int> s;
        return helper(root, k, s);
    }
    bool helper(TreeNode* node, int k, unordered_set<int>& s) {
        if (!node) return false;
        if (s.count(k - node->val)) return true;
        s.insert(node->val);
        return helper(node->left, k, s) || helper(node->right, k, s);
    }
};
