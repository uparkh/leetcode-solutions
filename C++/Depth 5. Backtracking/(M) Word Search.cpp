#include <vector>
#include <string>
using namespace std;

// My Original Solution - 24 minutes
// Time: O(n * 3^l) - n = # of cells, l = len(word)
//      - Because for each of n cells visited, dfs in worst case visits entire length of word
//        before not finding a match, each previous match causes cell checks in 3 other directions.
// Space: O(l) - because `i,j,found` vars created for each length of word.
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (dfs(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

private:
    // @param found - word index where left of `found` has been found
    bool dfs(vector<vector<char>>& board, int i, int j, string& word, int found) {
        if ((i < 0 || i >= board.size()) || (j < 0 || j >= board[0].size())) { // bound checks
            return false;
        }
        if (board[i][j] == '#' || board[i][j] != word[found]) { // logical checks
            return false;
        }
        ++found;
        if (found == word.size()) {
            return true;
        }
        char curr = board[i][j];
        board[i][j] = '#';
        bool rv = dfs(board, i-1, j, word, found) ||
                  dfs(board, i+1, j, word, found) ||
                  dfs(board, i, j-1, word, found) ||
                  dfs(board, i, j+1, word, found);
        board[i][j] = curr;
        return rv;
    }
};

// NeetCode Solution
// Same idea as mine, but does not store current char, realizing that the `found` var
// tracks the current char from `word` anyway.
// AND does not do a check to make sure board[i][j] != '#'. Used spaces already have a char
// that won't match `word` anyway.
class NeetCodeSolution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, word, 0, i, j, m, n)) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
private:
    bool dfs(vector<vector<char>>& board, string word,
        int index, int i, int j, int m, int n) {
        
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[index]) {
            return false;
        }
        if (index == word.size() - 1) {
            return true;
        }
        
        board[i][j] = '#';
        
        if (dfs(board, word, index + 1, i - 1, j, m, n)
            || dfs(board, word, index + 1, i + 1, j, m, n)
            || dfs(board, word, index + 1, i, j - 1, m, n)
            || dfs(board, word, index + 1, i, j + 1, m, n)) {
            return true;
        }
        
        board[i][j] = word[index];
        return false;
    }
};
