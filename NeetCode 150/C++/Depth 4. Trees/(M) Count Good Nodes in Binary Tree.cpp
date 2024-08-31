#include <queue>
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
// Really bad LC relative time and space performance, because of my Queue data structure.
class Solution {
public:
    int goodNodes(TreeNode* root) {
        if (root == nullptr)
            return 0;

        int result = 0;
        queue< pair<TreeNode*, int> > Q;
        Q.push(make_pair(root, root->val));

        while (!Q.empty()) {
            TreeNode* node = Q.front().first;
            int path_max = Q.front().second;
            Q.pop();

            if (node->val >= path_max) {
                ++result;
                path_max = node->val;
            }

            if (node->left != nullptr)
                Q.push(make_pair(node->left, path_max));
            if (node->right != nullptr)
                Q.push(make_pair(node->right, path_max));
        }
        return result;
    }
};

// NeetCode Solution
// Recursive w/DFS, faster because of no Queue data structure.
class NeetCodeSolution {
public:
    int goodNodes(TreeNode* root) {
        int result = 0;
        dfs(root, root->val, result);
        return result;
    }
private:
    void dfs(TreeNode* root, int maxSoFar, int& result) {
        if (root == NULL) {
            return;
        }
        
        if (root->val >= maxSoFar) {
            result++;
        }
        
        dfs(root->left, max(maxSoFar, root->val), result);
        dfs(root->right, max(maxSoFar, root->val), result);
    }
};
