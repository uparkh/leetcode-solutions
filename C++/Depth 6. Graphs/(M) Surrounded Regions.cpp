#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// My 1st Solution -- Inside Out
// Search for Os on the inside to expand out to remembering that the only 
// way an O blob is not surrounded is if an O cell is on the perimeter of 
// the board.

// Does *not* pass all test cases. Edge case: if there is a fork in the road
// while traversing adjacent 'O's, the branches have no awareness of the
// others.
class InsideOutSolution {
private:
    vector<pair<int, int>> dirs = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    bool dfs(vector<vector<char>>& board, unordered_map<char *, bool>& visited,
            int i, int j, int N, int M) {
        char *curptr = &(board[i][j]);
        if (visited.count(curptr) != 0) {
            return visited[curptr];
        }
        visited[curptr] = true;
        // return false (not surrounded by X) i.f.f. this cell on the border
        if (i <= 0 || i >= N-1 || j <= 0 || j >= M-1) {
            visited[curptr] = false;
            return false;
        }
        bool surrounded = true;
        for (pair<int, int>& dir : dirs) {
            int r = i + dir.first, c = j + dir.second;
            if (board[r][c] == 'O') {
                surrounded = surrounded && dfs(board, visited, r, c, N, M);
            }
            if (!surrounded) {
                visited[curptr] = false;
                return false;
            }
        }
        if (surrounded) {
            *curptr = 'X';
        }
        return true;
    }
public:
    void solve(vector<vector<char>>& board) {
        int N = board.size(), M = board[0].size();
        unordered_map<char *, bool> visited;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (board[i][j] == 'O') {
                    dfs(board, visited, i, j, N, M);
                }
            }
        }
    }
};

// My 2nd Solution -- Outside In
// I realized it's just much simpler to DFS from the perimeter and mark
// which cells shouldn't be flipped, and then flip the ones that weren't marked.
// Time: O(m x n)
// Space: O(1)
class Solution {
private:
    vector<pair<int, int>> dirs = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    void dfs(vector<vector<char>>& board, int i, int j, int N, int M) {
        board[i][j] = '*';
        for (pair<int, int>& dir : dirs) {
            int r = i + dir.first, c = j + dir.second;
            if (r < 0 || r >= N || c < 0 || c >= M) {
                continue;
            }
            if (board[r][c] == 'O') {
                dfs(board, r, c, N, M);
            }
        }
    }
public:
    void solve(vector<vector<char>>& board) {
        int N = board.size(), M = board[0].size();
        for (int i = 0; i < N; ++i) {
            if (board[i][0] == 'O') {
                dfs(board, i, 0, N, M);
            }
            if (board[i][M-1] == 'O') {
                dfs(board, i, M-1, N, M);
            }
        }
        for (int j = 0; j < M; ++j) {
            if (board[0][j] == 'O') {
                dfs(board, 0, j, N, M);
            }
            if (board[N-1][j] == 'O') {
                dfs(board, N-1, j, N, M);
            }
        }
        // sub 'O'->'X', '*'->'O'
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == '*') {
                    board[i][j] = 'O';
                }
            }
        }
    }
};


// NeetCode Solution
// Pretty much the exact same as my 2nd Solution, just moved around some
// if statements.
/*
    Given a matrix, capture ('X') all regions that are surrounded ('O')

    Distinguish captured vs escaped, 'X' vs 'O' vs 'E'

    Time: O(m x n)
    Space: O(m x n)
*/

class NeetCodeSolution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();
        
        // marking escaped cells along the border
        for (int i = 0; i < m; i++) {
            dfs(board,i,0,m,n);
            dfs(board,i,n-1,m,n);
        }
        
        for (int j = 0; j < n; j++) {
            dfs(board,0,j,m,n);
            dfs(board,m-1,j,m,n);
        }
        
        // flip cells to correct final states
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
                if (board[i][j] == 'E') {
                    board[i][j] = 'O';
                }
            }
        }
    }
private:
    void dfs(vector<vector<char>>& board, int i, int j, int m, int n) {
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != 'O') {
            return;
        }
        
        board[i][j] = 'E';
        
        dfs(board, i - 1, j, m, n);
        dfs(board, i + 1, j, m, n);
        dfs(board, i, j - 1, m, n);
        dfs(board, i, j + 1, m, n);
    }
};


void print_board(const vector<vector<char>>& board) {
    int N = board.size(), M = board[0].size();
    for (int i = 0; i < N; ++i) {
        cout << "[ ";
        for (int j = 0; j < M; ++j) {
            cout << board[i][j] << (j != M-1 ? ", " : " ");
        }
        cout << "]\n";
    }
}
int main() {
    // vector<vector<char>> board = {
    //     {'X','X','X','X'},{'X','O','O','X'},{'X','X','X','X'},{'X','O','X','X'}
    // };
    vector<vector<char>> board = {{'X','X','X','X','O','X'},{'O','X','X','O','O','X'},{'X','O','X','O','O','O'},{'X','O','O','O','X','O'},{'O','O','X','X','O','X'},{'X','O','X','O','X','X'}};
    cout << "Board:\n";
    print_board(board);
    Solution().solve(board);
    cout << string(80, '-') << '\n';
    cout << "Output:\n";
    print_board(board);

    vector<vector<char>> expected = {{'X','X','X','X','O','X'},{'O','X','X','O','O','X'},{'X','O','X','O','O','O'},{'X','O','O','O','X','O'},{'O','O','X','X','X','X'},{'X','O','X','O','X','X'}};
    cout << string(80, '-') << '\n';
    cout << "Expected Output:\n";
    print_board(expected);
}