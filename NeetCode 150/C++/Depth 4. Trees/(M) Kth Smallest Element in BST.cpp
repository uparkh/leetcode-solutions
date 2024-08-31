struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <stack>
using namespace std;
// My Solution
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> S;
        TreeNode* prev = nullptr;
        
        // inorder traversal
        while (!S.empty() || root != nullptr) {
            while (root != nullptr) {
                S.push(root);
                root = root->left;
            }
            root = S.top();
            S.pop();

            // process nodes here
            k--;
            if (k == 0) {
                return root->val;
            }

            // shift right for inorder
            root = root->right;
        }
        return -1; // k > n
    }
};
// It worked, but I'm not sure it's the most optimal.
// Takes log n steps to get to leftmost, k steps to find
// kth smallest. So O(log n + k) time, O(log n) space for the
// stack, which can only grow as large as the height of
// the tree.

// NeetCode solution was also an inorder, but recursive.
class NC_Recursive_Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int result = 0;
        inorder(root, k, result);
        return result;
    }
private:
    void inorder(TreeNode* root, int& k, int& result) {
        if (root == NULL) {
            return;
        }
        inorder(root->left, k, result);
        k--;
        if (k == 0) {
            result = root->val;
            return;
        }
        inorder(root->right, k, result);
    }
};