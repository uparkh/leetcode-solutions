#include <vector>
using namespace std;

// My Original Solution
// O(2^target) time
// O(target) space - `curr` expands up to however many of lowest candidate to meet target
// Pretty much just reapplied the NeetCode algo from (M) Subsets.cpp.
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> curr;
        vector<vector<int>> result;
        dfs(curr, 0, 0, target, candidates, result);
        return result;
    }

private:
    void dfs(vector<int>& curr, int start, int sum, int target,
            vector<int>& candidates, vector<vector<int>>& result) {
        if (sum == target) {
            result.push_back(curr);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if (sum + candidates[i] <= target) {
                curr.push_back(candidates[i]);
                dfs(curr, i, sum + candidates[i], target, candidates, result);
                curr.pop_back();
            }
        }
    }
};


// NeetCode Solution
// Time: O(2^target)
// Space: O(target)

// Same fundamental idea as mine, but instead of adding to a sum counter, they subtract from
// the target counter.
// Also instead of using a loop, they go for pure functional programming route, and increment
// i with an argument instead. Otherwise, the pattern of accesses/checks is the same as mine.
class NeetCodeSolution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        std::vector<int> curr;
        std::vector<std::vector<int>> res;
        helper(candidates, target, 0, curr, res);
        return res;
    }
private:
    void helper(std::vector<int>& cands, int target, int i, std::vector<int>& curr,  std::vector<std::vector<int>>& res) {
        if (i >= cands.size() || target < 0)
            return;

        if (target == 0) {
            res.push_back(curr);
            return;
        }

        curr.push_back(cands[i]);
        
        helper(cands, target - cands[i], i, curr, res);

        curr.pop_back();

        helper(cands, target, i + 1, curr, res);
    }
};
