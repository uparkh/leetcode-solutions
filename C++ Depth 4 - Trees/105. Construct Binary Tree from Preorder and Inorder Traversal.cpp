struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>
#include <stack>
using namespace std;
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, 
            vector<int>& inorder) {
        // for a full tree preorder, this would be enough
        // example: [3, 9, 4, 5, 20, 15, 7]
        TreeNode* prev = nullptr;
        TreeNode* curr = new TreeNode(preorder.back());

        for (int p = preorder.size()-1; p >= 0; p--) {
            TreeNode* curr = new TreeNode(preorder[p]);

        }

        // 

    }
};

// unfinished, could not figure out the exact relationship
// between preorder and inorder
// I think part of the difficulty comes from me trying to
// force an iterative solution
// Recursive pre/in/post traversals are much easier to
// implement

/*
Pre:
process data
recurse(left)
recurse(right)

In:
recurse(left)
process data
recurse(right)

Post:
recurse(left)
recurse(right)
process data
*/

// FUNDAMENTAL intuition from NC video:
// The first element in the preorder is ALWAYS root of a tree.
// That root, when located in the inorder,
//  - its left subtree will be to the left of the root inorder
//  - its right subtree wil be to the right of the root inorder

// The corresponding partition in the preorder array
// will have len(left subtree pre) = len(left subtree inorder)

// O(n) time, O(n) space
class NC_Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int index = 0;
        return build(preorder, inorder, index, 0, inorder.size() - 1);
    }
private:
    TreeNode* build(vector<int>& preorder, vector<int>& inorder, int& index, int i, int j) {
        if (i > j) {
            return NULL;
        }
        
        TreeNode* root = new TreeNode(preorder[index]);

        // find in inorder array 
        int split = 0;
        for (int i = 0; i < inorder.size(); i++) {
            if (preorder[index] == inorder[i]) {
                split = i;
                break;
            }
        }
        index++;

        // look how much simpler the recursive solution is
        // compared to the more complex iterative sol'n
        root->left = build(preorder, inorder, index, i, split - 1);
        root->right = build(preorder, inorder, index, split + 1, j);
        
        return root;
    }
};


