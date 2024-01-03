#include <vector>
#include <string>
using namespace std;

// My Original Solution
// Time: O(n * 2^n) , Space: O(n)
// Worst case string: "aaaaaaaaaaaa"
// Palindrome partitioning is just the power set of this string,
// hence 2^n possibilities visited timewise.
// Spacewise, each possibility has an associated `substr` variable
// which expands up to the string s (size n).

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<string> curr;
        vector<vector<string>> result;
        dfs(s, 0, curr, result);
        return result;
    }

private:
    bool isPalindrome(string s) {
        size_t N = s.size();
        for (size_t i = 0; i <= (N-1)/2; ++i) {
            if (s[i] != s[N - 1 - i]) {
                return false;
            }
        }
        return true;
    }

    void dfs(string& s, int start, vector<string>& curr,
             vector<vector<string>>& result) {
        if (start == s.size()) {
            result.push_back(curr);
            return;
        }
        string substr;
        for (int i = start; i < s.size(); ++i) {
            substr += s[i];
            if (!isPalindrome(substr)) {
                continue;
            }
            curr.push_back(substr);
            dfs(s, i+1, curr, result);
            curr.pop_back();
        }
    }
};

// NeetCode Solution
// Pretty much the exact same solution as mine, with the substrings
// and all, they just chose to implement palindrome checking slightly
// differently.
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<string> curr;
        vector<vector<string>> result;
        dfs(s, 0, curr, result);
        return result;
    }
private:
    void dfs(string s, int start, vector<string>& curr, vector<vector<string>>& result) {
        if (start == s.size()) {
            result.push_back(curr);
            return;
        }
        for (int i = start; i < s.size(); i++) {
            if (isPalindrome(s, start, i)) {
                string str = s.substr(start, i - start + 1);
                curr.push_back(str);
                dfs(s, i + 1, curr, result);
                curr.pop_back();
            }
        }
    }
    bool isPalindrome(string s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};