#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        memo.resize(m, vector<char>(n, 0b000));
        vector<vector<int>> res;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (s_dfs(heights, i, j, m, n) & 0b110 
                        == 0b110) { // empties to both?
                    res.push_back({i, j});
                }
            }
        }
        return res;
    }

private:
    vector<vector<char>> memo;

    /**
     * bit 0 - visited?
     *     1 - empties -> Atlantic?
     *     2 - empties -> Pacific?
    */
    char s_dfs(vector<vector<int>>& heights, int r, int c, int m, int n) {
        stack< pair<int, int> > S; // coords to visit
        S.push({r, c});
        int prevHeight = heights[r][c];
        char rv = 0b000;
        while (!S.empty()) {
            int i = S.top().first, j = S.top().second;
            if (i < 0 || j < 0) {
                rv = 0b100;
                S.pop();
                continue;
            }
            if (i >= m || j >= n) {
                rv = 0b010;
                S.pop();
                continue;
            }
            if (heights[i][j] > prevHeight) {
                rv = 0b000;
                S.pop();
                continue;
            }
            if (memo[i][j] & 0b001) { // already visited?
                rv = memo[i][j];
                S.pop();
                continue;
            }
            memo[i][j] |= 0b001
                | dfs(heights, heights[i][j], i+1, j, m, n)
                | dfs(heights, heights[i][j], i-1, j, m, n)
                | dfs(heights, heights[i][j], i, j+1, m, n)
                | dfs(heights, heights[i][j], i, j-1, m, n);
            return memo[i][j];
        }
    }

    // char dfs(vector<vector<int>>& heights, int prevHeight, int i, int j, int m, int n) {
    //     if (i < 0 || j < 0) {
    //         return 0b100;
    //     }
    //     if (i >= m || j >= n) {
    //         return 0b010;
    //     }
    //     if (heights[i][j] > prevHeight) {
    //         return 0b000;
    //     }
    //     if (memo[i][j] & 0b001) { // already visited?
    //         return memo[i][j];
    //     }
    //     memo[i][j] |= 0b001
    //         | dfs(heights, heights[i][j], i+1, j, m, n)
    //         | dfs(heights, heights[i][j], i-1, j, m, n)
    //         | dfs(heights, heights[i][j], i, j+1, m, n)
    //         | dfs(heights, heights[i][j], i, j-1, m, n);
    //     return memo[i][j];
    // }
};