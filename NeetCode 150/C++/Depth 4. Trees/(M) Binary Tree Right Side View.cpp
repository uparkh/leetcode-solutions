#include <vector>
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

// My Original Solution - O(n) time & space

// Had some difficulty in realizing that I needed to use BFS here, but then I realized
// that the problem revolves around different levels of the tree, so it's natural to do it
// like this.

// Another realization was how to process one thing per level of the tree by storing
// a level size variable. This is a much easier way to process each level than the convoluted
// method I did in JJ's Computer Science 2 class. If I were to rewrite the print_tree function
// I used for that class, I would just copy the BFS below but just add null nodes anyway.
// When printing, skip null nodes.
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr)
            return {};

        vector<int> result;
        queue<TreeNode*> Q;

        Q.push(root);
        while(!Q.empty()) {
            result.push_back(Q.front()->val);

            auto lvl_size = Q.size();
            for (int i = 0; i < lvl_size ; i++) {
                auto node = Q.front();
                Q.pop();

                if (node->right != nullptr)
                    Q.push(node->right);
                if (node->left != nullptr)
                    Q.push(node->left);
            }
        }
        return result;
    }
};

// NeetCode Solution is the same as mine, but actually just less readable.
// Not sure why they chose to do the weird ass count == i thing? Super redundant.
class NeetCodeSolution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if (root == NULL) {
            return {};
        }
        
        queue<TreeNode*> q;
        q.push(root);
        
        vector<int> result;
        
        while (!q.empty()) {
            int count = q.size();
            
            for (int i = count; i > 0; i--) {
                TreeNode* node = q.front();
                q.pop();
                
                if (i == count) {
                    result.push_back(node->val);
                }
                
                if (node->right != NULL) {
                    q.push(node->right);
                }
                if (node->left != NULL) {
                    q.push(node->left);
                }
            }
        }
        
        return result;
    }
};
