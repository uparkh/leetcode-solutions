#include <vector>
using namespace std;

// My Original Solution
// Only works for ordered sets that have duplicates. Could not figure out
// how to work with unordered sets with duplicates.
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> curr;
        vector<vector<int>> result;
        dfs(nums, curr, 0, result);
        return result;
    }

private:
    void dfs(vector<int>& nums, vector<int>& curr, int start,
             vector<vector<int>>& result) {
        result.push_back(curr);
        for (int i = start; i < nums.size(); i++) {
            curr.push_back(nums[i]);
            if (i == start || nums[i] != nums[i-1]) {
                dfs(nums, curr, i + 1, result);
            }
            curr.pop_back();
        }
    }
};

// NeetCode Solution
// O(n * 2^n) time - power set is 2^n elems, have to iterate through all elems
// O(n) space - curr only ever expands up to `nums`, i/start vars for each n

// OF COURSE, if it works with ordered sets and the original is not ordered,
// order it! LMAO
// Otherwise this solution is the exact same as mine in terms of the fundamental
// concepts applied.
// Bit more speed up by doing the duplicate condition check earlier, and 
// skipping that iteration entirely, no unnecessary push and pops on `curr`.
class NeetCodeSolution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        vector<int> curr;
        vector<vector<int>> result;
        
        dfs(nums, 0, curr, result);
        return result;
    }
private:
    void dfs(vector<int>& nums, int start, vector<int>& curr, vector<vector<int>>& result) {
        result.push_back(curr);
        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            curr.push_back(nums[i]);
            dfs(nums, i + 1, curr, result);
            curr.pop_back();
        }
    }
};
