struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <stack>
// #include <unordered_map>
using namespace std;

// class Solution {
// public:
//     bool isValidBST(TreeNode* root) {
//     TreeNode* curr; 
//     stack<TreeNode *> s;
//     s.push(root);
//     unordered_map<TreeNode*, TreeNode*> nodeToParent;
//     unordered_map<TreeNode*, bool> visitedNode;

//     while (!s.empty()) {
//         if (curr->right != nullptr) {
//             s.push(curr->right);
//             nodeToParent[curr->right] = curr;
//             visitedNode[curr->right] = false;
//         }
//         if (curr->left != nullptr) {
//             s.push(curr->left);
//             nodeToParent[curr->left] = curr;
//         }
//         if (curr->left != nullptr) {
//             s.push(curr->left);
//         }

//         // leaf node? 
//         if ((curr->left != nullptr && curr->right != nullptr)
//             || (visitedNode.at())) {
            
//         }
//     }

//     }
// };

// Was not able to figure out how to consider parent node's
// value when building tree from bottom-up.

// NeetCode Solution
// O(n) time and O(n) space
// Notes: Inorder traversal is the clear solution here.
//      For any BST, an inorder traversal should yield a sorted
//      list of keys. So you can just check if this upholds
//      to validate the BST.

// Recursive sol'n. They keep track of bounds by setting
// the initial bounds to the LONG_MIN and LONG_MAX.
// When recursing, the logical upper bound is set when
// traversing down the left child, while the logical lower bound
// is set when traversing down the right child.

// Therefore, if any node in the left subtree exceeds the
// upper bound, or vice versa with the right subtree, it
// invalidates the BST.
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return helper(root, LONG_MIN, LONG_MAX);
    }
private:
    bool helper(TreeNode* root, long left, long right){
        if (!root)
            return true;
        if (root->val < right && root->val > left){
            return helper(root->left, left, root->val) && helper(root->right, root->val, right);
        }
        return false;
    }
};

// Iterative, inorder traversal
// Basically, it first travels all the way down left,
// then backs up to the parent node of the leftmost,
// then compares for inorder (if left child < parent).
// After that, it goes one right of the parent, then
// travels all the way down that subtree.
// Repeat until entire tree is validated.
class IterativeSolution {
public:
    bool isValidBST(TreeNode* root) {
        stack<TreeNode*> stk;
        TreeNode* prev = NULL;
        
        while (!stk.empty() || root != NULL) {
            while (root != NULL) { // travel all the way
                stk.push(root);    // down leftside
                root = root->left;
            }
            root = stk.top();
            stk.pop();
            
            if (prev != NULL && prev->val >= root->val) {
                return false;       // invalidate condition
            }
            
            prev = root;
            root = root->right;     // shift right one
        }
        
        return true;
    }
};