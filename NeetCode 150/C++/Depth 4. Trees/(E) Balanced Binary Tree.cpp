#include <cmath>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// My Original Solution - O(n) time & space
// Proud of this, because I applied exactly what I learned in the
// previous "Diameter of Binary Tree" problem, with the tracking of
// two separate results -- one required for the DFS to track height
// properly, and the other final evaluation of the thing I needed.
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        bool res = true;
        dfs(root, res);
        return res;
    }

private:
    int dfs(TreeNode* root, bool& result) {
        if (root == nullptr || result == false)
            return 0;
        
        int leftHeight = dfs(root->left, result);
        int rightHeight = dfs(root->right, result);

        if (abs(leftHeight - rightHeight) > 1) {
            result = false;
            return 0;
        }
        
        return 1 + max(leftHeight, rightHeight);
    }
};

// NeetCode Solution - O(n) time & space
// An important observation here is that they chose to use the
// return value as the problem's answer, and the reference paramter
// as the height tracker. It's cool how I did the exact opposite
// and yet both solutions are doing the same thing. Good to know
// that I can swap them around for the future.
class NeetCodeSolution {
public:
    bool isBalanced(TreeNode* root) {
        int height = 0;
        return dfs(root, height);
    }
private:
    bool dfs(TreeNode* root, int& height) {
        if (root == NULL) {
            height = -1;
            return true;
        }
        
        int left = 0;
        int right = 0;
        
        if (!dfs(root->left, left) || !dfs(root->right, right)) {
            return false;
        }
        if (abs(left - right) > 1) {
            return false;
        }
        
        height = 1 + max(left, right);
        return true;
    }
};
