#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

// My Original Solution - 51 minutes
// Horrible time + space complexity due to board state copying, but I'm just happy I did it
// first try and had the right backtracking idea.
// That + marking spaces as visitable also consumes unnecessary space, better maybe to just
// leave it as dots and then determine placeability of Queens.
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '#')); // hashes = available queen slot
        vector<vector<string>> result;
        dfs(board, 0, 0, n, result);
        return result;
    }

private:
    void placeQueen(vector<string>& board, int i, int j) {
        board[i][j] = 'Q';
        for (int ii = 0; ii < board.size(); ii++) {
            if (ii == i) {
                continue;
            }
            board[ii][j] = '.';
            int offset = i - ii;
            int l = j - offset, r = j + offset;
            if (l >= 0 && l < board.size()) {
                board[ii][l] = '.';
            }
            if (r >= 0 && r < board.size()) {
                board[ii][r] = '.';
            }
        }
        for (int jj = 0; jj < board.size(); jj++) {
            if (jj == j) {
                continue;
            }
            board[i][jj] = '.';
        }
    }
    void dfs(vector<string>& board, int i0, int j0, int n, vector<vector<string>>& result) {
        if (n == 0) { // no queens left to place
            for (int r = 0; r < board.size(); r++) {
                for (int c = 0; c < board.size(); c++) {
                    if (board[r][c] == '#') {
                        board[r][c] = '.'; // clean up
                    }
                }
            }
            result.push_back(board);
            return;
        }
        int j = j0;
        for (int i = i0; i < board.size(); i++) {
            for (; j < board.size(); j++) {
                if (board[i][j] != '#') {
                    continue;
                }
                vector<string> prevBoard(board); // major copying slowdown
                placeQueen(board, i, j);
                dfs(board, i, j+1, n-1, result);
                board = prevBoard;
            }
            j = 0;
        }
        
    }
};


// NeetCode Solution 
/**
 * Uses the heuristic that no two queens can be on the same row, column, or diagonal.
 * Uses sets to keep track of which Queens occupy which col, pos and neg diagonals.
 * Pretty clever usage of (row - col) to index the neg diagonals, and (row + col) to index
 * the positive diagonals.
 */

/*
    N-Queens: place n queens such that no 2 queens atk each other, return all soln's

    Place queens per row, try all possibilities & validate for further rows, backtrack

    Time: O(n!)
    Space: O(n^2)
*/

class NeetCodeSolution {
private:
    unordered_set<int> cols;     //for Columns
    unordered_set<int> negDiag;  //for negative diagnals R-C
    unordered_set<int> posDiag;  //for positive diagnals R+C
    
    void backtrack(int n, int row, vector<vector<string>>& res, vector<string>& board){
        if(row==n){
            res.push_back(board);
            return ; 
        }
        
        for(int col = 0; col < n; col++){   //Shifting through each col
            if( cols.find(col) != cols.end() or //if queen alread placed in this col
                negDiag.find(row - col) != negDiag.end() or //if queen in negDiag
                posDiag.find(row + col) != posDiag.end()    //if queen in posDiag
              )
                continue;
            
            cols.insert(col);
            negDiag.insert(row - col);
            posDiag.insert(row + col);
            board[row][col] = 'Q';
            
            backtrack(n, row +1, res, board);
            
            cols.erase(col);
            negDiag.erase(row - col);
            posDiag.erase(row + col);
            board[row][col] = '.';
        }
    }
   
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> board(n, string(n,'.'));
        backtrack(n, 0, res, board);
        return res;
    }
};

// But it's still not the fastest (not above 50% runtime/space).
// So instead I'm going to analyze this super fast bitmasking solution from here next time:
// https://leetcode.com/problems/n-queens/solutions/19808/accepted-4ms-c-solution-use-backtracking-and-bitmask-easy-understand/
/**
 * The fundamental idea behind this super fast solution is the exact same as the NC solution above.
 * Just, instead of keeping track of which cols/diags are occupied via sets, it uses a presized
 * vector of ints. vector<bool> is not actually an STL container, so should be avoided at all costs.
 * Since vector/array accesses are much faster, it performs better than sets.
 */
class SuperFastSolution {
public:
    std::vector<std::vector<std::string> > solveNQueens(int n) {
        std::vector<std::vector<std::string> > res;
        std::vector<std::string> nQueens(n, std::string(n, '.'));
        std::vector<int> flag_col(n, 1), flag_45(2 * n - 1, 1), flag_135(2 * n - 1, 1);
        solveNQueens(res, nQueens, flag_col, flag_45, flag_135, 0, n);
        return res;
    }
private:
    void solveNQueens(std::vector<std::vector<std::string> > &res, std::vector<std::string> &nQueens, std::vector<int> &flag_col, std::vector<int> &flag_45, std::vector<int> &flag_135, int row, int &n) {
        if (row == n) {
            res.push_back(nQueens);
            return;
        }
        for (int col = 0; col != n; ++col)
            if (flag_col[col] && flag_45[row + col] && flag_135[n - 1 + col - row]) {
                flag_col[col] = flag_45[row + col] = flag_135[n - 1 + col - row] = 0;
                nQueens[row][col] = 'Q';
                solveNQueens(res, nQueens, flag_col, flag_45, flag_135, row + 1, n);
                nQueens[row][col] = '.';
                flag_col[col] = flag_45[row + col] = flag_135[n - 1 + col - row] = 1;
            }
    }
};
