#include <limits>
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


// My Original Solution - O(n) spacetime 
// Pretty proud of being able to do this Hard in 34 min, 28 sec.
// Applied everything I learned so far with DFS and result/logic value tracking.
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int result = numeric_limits<int>::min(); // "- infinity"
        dfs(root, result);
        return result;
    }

private:
    // return int = the node's max path sum
    // &max_path = reference to highest max path result found
    int dfs(TreeNode* root, int &max_path) {
        if (root == nullptr) 
            return 0;
        
        int left = dfs(root->left, max_path);
        int right = dfs(root->right, max_path);

        int node_max = root->val + max(0, max(left, right));
        max_path = max(node_max, max(max_path, root->val + left + right));
        return node_max;
    }
};


// NeetCode Solution - O(n) spacetime
// Their solution is almost identical to mine, but slightly more optimized in
// that they choose to 'discard' the left or right subtree max paths by maxing out with
// 0 earlier. Results in a lot cleaner code.
class NeetCodeSolution {
public:
    int maxPathSum(TreeNode* root) {
        int maxPath = INT_MIN;
        dfs(root, maxPath);
        return maxPath;
    }
private:
    int dfs(TreeNode* root, int& maxPath) {
        if (root == NULL) {
            return 0;
        }
        
        int left = max(dfs(root->left, maxPath), 0);
        int right = max(dfs(root->right, maxPath), 0);
        
        int curPath = root->val + left + right;
        maxPath = max(maxPath, curPath);
        
        return root->val + max(left, right);
    }
};
