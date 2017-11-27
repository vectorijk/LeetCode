# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example,
# Given
# 
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 思路：递归，设root左右子结点为L和R，先将L变为一条链，将root.right指向L，之后把R变为一条链，L最后一个元素指向R即可。
class MySolution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root: return
        L , R =root.left,root.right
        self.flatten(L)
        root.left=None
        root.right = L
        while root.right: root=root.right
        self.flatten(R)
        root.right = R

###
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        return self.flattenRecu(root, None)
        
    def flattenRecu(self, root, list_head):
        if root != None:
            list_head = self.flattenRecu(root.right, list_head)
            list_head = self.flattenRecu(root.left, list_head)
            root.right = list_head
            root.left = None
            return root
        else:
            return list_head
        
class Solution2:
    list_head = None
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root != None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.list_head
            root.left = None
            self.list_head = root
            return root
        
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = Solution().flatten(root)
    print result.val
    print result.right.val
    print result.right.right.val
    print result.right.right.right.val
    print result.right.right.right.right.val
    print result.right.right.right.right.right.val

    
    
    
# class Solution {
# public:
#     void flatten(TreeNode *root) {
#         if(!root) return;
#         vector<TreeNode*> allNodes;
#         preorder(root, allNodes);
#         int n = allNodes.size();
#         for(int i=0; i<n-1; i++) {
#             allNodes[i]->left = NULL;
#             allNodes[i]->right = allNodes[i+1];
#         }
#         allNodes[n-1]->left = allNodes[n-1]->right = NULL;
#     }
    
#     void preorder(TreeNode *root, vector<TreeNode*> &allNodes) {
#         if(!root) return;
#         allNodes.push_back(root);
#         preorder(root->left, allNodes);
#         preorder(root->right, allNodes);
#     }
# };



# flatten inorder
# 1:  TreeNode* flatten(TreeNode *root) {  
# 2:       if (root == NULL) return NULL;  
# 3:       TreeNode* rightTree = root->right;  
# 4:       TreeNode* newHead = root;  
# 5:       TreeNode* leftList = flatten(root->left);  
# 6:       if (leftList != NULL)  
# 7:       {  
# 8:            newHead = leftList;  
# 9:            TreeNode* tail = leftList->left;  
# 10:            tail->right = root;  
# 11:            root->left = tail;  
# 12:            leftList->left = root;  
# 13:       }  
# 14:       TreeNode* rightList = flatten(rightTree);  
# 15:       if (rightList != NULL)  
# 16:       {  
# 17:            root->right = rightList;  
# 18:            newHead->left = rightList->left;  
# 19:            rightList->left = root;  
# 20:       }  
# 21:       return newHead;  
# 22:  } 
