#include <vector>
#include <unordered_set>
using namespace std;

// My Original Solution - exponential time
// It did not pass the last test case for nums.length = 10, and I didn't expect it to.
// But I was at 40 minutes and I didn't want to spend more time, because this is about
// as elegant of a solution as I can make, any more modifications would have led to a less
// elegant solution.
class Solution {
private:
    void backtrack(vector<int> nums, vector<vector<int>>& result) {
        vector<int> temp;
        for (int i = 0; i < nums.size(); i++) {
            temp.clear();
            for (int j = 0; j < nums.size(); j++) {
                if (i != j)
                    temp.push_back(nums[j]);
            }
            backtrack(temp, result);
        }
        for (vector<int> elem : result) {
            if (elem == nums)
                return;
        }
        result.push_back(nums);
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(nums, result);
        return result;
    }
};

// NeetCode Solution
// O(n * 2^n) runtime, each element has 2^n combinations
// O(n) space, `curr` vector only ever expands to at most `nums`
// Pretty clever how they avoid duplicates by keeping a leftmost value and only branching
// dfs to elements to the right.
// Check the `(M) Subsets.png` image for an illustration of how it works.
class NeetCodeSolution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> curr;
        vector<vector<int>> result;
        dfs(nums, 0, curr, result);
        return result;
    }
private:
    void dfs(vector<int>& nums, int start, vector<int>& curr, vector<vector<int>>& result) {
        result.push_back(curr);
        for (int i = start; i < nums.size(); i++) {
            curr.push_back(nums[i]);
            dfs(nums, i + 1, curr, result);
            curr.pop_back();
        }
    }
};
