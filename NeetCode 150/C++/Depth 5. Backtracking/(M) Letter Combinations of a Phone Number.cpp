#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

// My Original Solution
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) {
            return {};
        }
        string nummap[8] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> result;
        string curr;
        dfs(digits, 0, nummap, curr, result);
        return result;
    }

private:
    void dfs(string& digits, int i, string nummap[], string& curr, vector<string>& result) {
        if (i == digits.size()) {
            result.push_back(curr);
            return;
        }
        int key = digits[i] - '2'; // parse curr digit -> key
        for (char c : nummap[key]) {
            curr.push_back(c);
            dfs(digits, i+1, nummap, curr, result);
            curr.pop_back();
        }
    }
};

// NeetCode Solution 
/*
 * Exact same solution as mine, just used the map DS instead of an array. I'm not sure why the map
 * is faster, if I'm using the array for mapping purposes, but it is in this problem.
 * 
 * Time & Space: O(n * 4^n) - worst case = digits w/ 4 letters, iterate thru each digit
*/
class NeetCodeSolution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }
        
        unordered_map<char, string> m = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        string curr = "";
        vector<string> result;
        
        dfs(digits, 0, m, curr, result);
        return result;
    }
private:
    void dfs(string digits, int index, unordered_map<char, string>& m, string& curr, vector<string>& result) {
        if (index == digits.size()) {
            result.push_back(curr);
            return;
        }
        string str = m[digits[index]];
        for (int i = 0; i < str.size(); i++) {
            curr.push_back(str[i]);
            dfs(digits, index + 1, m, curr, result);
            curr.pop_back();
        }
    }
};
