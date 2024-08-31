#include <vector>
#include <unordered_set>
using namespace std;

// My Original Solution
// O(n*n!) - permutation
// O(n*n!) - sets for each memory point
// Pretty bad memory usage
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> curr;
        unordered_set<int> free(nums.begin(), nums.end());
        vector<vector<int>> result;
        dfs(nums, curr, free, result);
        return result;
    }

private:
    void dfs(vector<int>& nums, vector<int>& curr, 
             unordered_set<int> free, vector<vector<int>>& result) {
        if (nums.size() == curr.size()) {
            result.push_back(curr);
            return;
        }
        unordered_set<int> next_free(free); // like what the fuck
        for (int val : free) {
            curr.push_back(val);
            next_free.erase(val);
            dfs(nums, curr, next_free, result);
            next_free.insert(val);
            curr.pop_back();
        }
    }
};

// This one is without sets, just simple O(n) time erasures from nums vector.
// This actually massively outperformed my first solution.
// The key insight here is that copying and creating all those new sets
// is actually much more expensive timewise AND spacewise than simply
// repurposing the &nums vector as a `free` vector. Set copy is also O(n).
// O(n^2 * n!) time - n! decision tree states, erase is O(n) * n iterations
// O(n!) space - `curr` only ever expands up to nums.size()
class NewSolution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> curr;
        vector<vector<int>> result;
        dfs(nums, curr, result, nums.size());
        return result;
    }

private:
    void dfs(vector<int>& nums, vector<int>& curr, 
             vector<vector<int>>& result, int perm_size) {
        if (curr.size() == perm_size) {
            result.push_back(curr);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            int val = nums[i];
            curr.push_back(val);
            nums.erase(nums.begin() + i);

            dfs(nums, curr, result, perm_size);

            nums.insert(nums.begin() + i, val);
            curr.pop_back();
        }
    }
};

// NeetCode Solution
// O(n * n!) time - n! decision tree states, iterate over n elems
// O(n!) space - n! decision tree states, each needs O(1) `start` variable

// Pretty clever, instead of using a curr array, just section off
// left part of nums as the permutation you are building, and section off
// the right part as the "free" elements that can be used to continue
// building the permutation.
// Also forgot from JJ's class, that swapping and shrinking index scope
// is O(1) "insert"/"removal" for a vector.
class NeetCodeSolution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        dfs(nums, 0, result);
        return result;
    }
private:
    void dfs(vector<int>& nums, int start, vector<vector<int>>& result) {
        if (start == nums.size()) {
            result.push_back(nums);
            return;
        }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[i], nums[start]);
            dfs(nums, start + 1, result);
            swap(nums[i], nums[start]);
        }
    }
};