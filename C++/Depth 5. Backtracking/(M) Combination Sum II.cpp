#include <vector>
using namespace std;

// My Original Solution
// O(2^n) time - Worst case = power set with 2^n elements
// O(n) space - curr only ever expands to candidate space
// Pretty much combinining duplicate skipping of '(M) Subsets II' and target-sum solution
// space exploration from '(M) Combination Sum"
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> curr;
        vector<vector<int>> result;
        sort(candidates.begin(), candidates.end());
        helper(candidates, 0, target, curr, result);
        return result;
    }

private:
    void helper(vector<int>& cands, int start, int target, vector<int>& curr,
                vector<vector<int>>& result) {
        if (target < 0) {
            return;
        }
        if (target == 0) {
            result.push_back(curr);
            return;
        }
        for (int i = start; i < cands.size(); i++) {
            if (i > start && cands[i] == cands[i-1]) {
                continue; // skip duplicates
            }
            curr.push_back(cands[i]);
            helper(cands, i+1, target - cands[i], curr, result);
            curr.pop_back();
        }
    }
};

// NeetCode Solution
// O(2^n) time, O(n) space
// Same fundamental solution as mine. But NOW they choose to use a sum counter lol.
// Doesn't make too much of a difference really.
class NeetCodeSolution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        
        vector<int> curr;
        vector<vector<int>> result;
        
        dfs(candidates, target, 0, 0, curr, result);
        return result;
    }
private:
    void dfs(vector<int>& candidates, int target, int sum, int start, vector<int>& curr, vector<vector<int>>& result) {
        if (sum > target) {
            return;
        }
        if (sum == target) {
            result.push_back(curr);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }
            curr.push_back(candidates[i]);
            dfs(candidates, target, sum + candidates[i], i + 1, curr, result);
            curr.pop_back();
        }
    }
};
