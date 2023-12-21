#include <algorithm>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// My Original Solution
// I don't know why -- but I'm way too allergic to creating
// helper functions. I keep thinking every problem can be
// solved with just a single recursive function call, without
// taking into account what result I need to keep track of
// between recursive calls.
// class Solution {
// public:
//     int diameterOfBinaryTree(TreeNode* root) {
//         if (root == nullptr)
//             return 0;
//         // if (root->left == nullptr && root->right == nullptr)
//         //     return 1;
//         // int maxDiam = max(
//         //     diameterOfBinaryTree(root->left),
//         //     diameterOfBinaryTree(root->right)
//         // );
//         int leftDiam = diameterOfBinaryTree(root->left);
//         leftDiam -= (leftDiam > 0);
//         int rightDiam = diameterOfBinaryTree(root->right);
//         rightDiam  -= (rightDiam > 0);
//         return (root->left != nullptr) + (root->right != nullptr)
//             + leftDiam + rightDiam;
//     }
// };


// NeetCode Solution - O(n) time & space
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int result = 0;
        dfs(root, result);
        return result;
    }
private:
    int dfs(TreeNode* root, int& result) {
        if (root == NULL) {
            return 0;
        }
        
        int left = dfs(root->left, result);
        int right = dfs(root->right, result);
        
        result = max(result, left + right);
        return 1 + max(left, right);
    }
};