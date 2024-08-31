#include <vector>
#include <array>
#include <queue>
#include <iostream>
using namespace std;

// My Original Solution
// Why am I using a set? Just keep a counter of all fresh oranges???
// Time: O(n * m) -- n = rows, m = cols
// Space: O(n * m)
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int min_elapsed = 0, fresh = 0;
        queue<vector<int>> rotten;
        int N = grid.size(), M = grid[0].size();
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (grid[i][j] == 2) {
                    rotten.push({i, j});
                } 
                fresh += (grid[i][j] == 1);
            }
        }
        int rotten_size = 0;
        vector<int> cur_rotten;
        array<vector<int>, 4> dirs;
        while (!rotten.empty()) {
            rotten_size = rotten.size();
            for (int _ = 0; _ < rotten_size; ++_) {
                cur_rotten = rotten.front();
                rotten.pop();
                dirs[0] = {cur_rotten[0] - 1, cur_rotten[1]};
                dirs[1] = {cur_rotten[0] + 1, cur_rotten[1]};
                dirs[2] = {cur_rotten[0], cur_rotten[1] - 1};
                dirs[3] = {cur_rotten[0], cur_rotten[1] + 1};
                for (vector<int> &dir : dirs) {
                    int i = dir[0], j = dir[1];
                    if (i < 0 || i >= N || j < 0 || j >= M) {
                        continue;
                    }
                    if (grid[i][j] == 1) {
                        grid[i][j] = 2;
                        --fresh;
                        rotten.push(dir);
                    }
                }
            }
            if (!rotten.empty()) {
                ++min_elapsed;
            }
        }
        if (fresh) { // any fresh oranges remaining?
            return -1;
        }
        return min_elapsed;
    }
};

// NeetCode Solution
/*
    Given grid: 0 empty cell, 1 fresh orange, 2 rotten orange
    Return min # of minutes until no cell has a fresh orange

    BFS: rotten will contaminate neighbors first, then propagate out

    Time: O(m x n)
    Space: O(m x n)
*/
class NCSolution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        // build initial set of rotten oranges
        queue<pair<int, int>> q;
        int fresh = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }
        // mark the start of a minute
        q.push({-1, -1});
        
        int result = -1;
        
        // start rotting process via BFS
        while (!q.empty()) {
            int row = q.front().first;
            int col = q.front().second;
            q.pop();
            
            if (row == -1) {
                // finish 1 minute of processing, mark next minute
                result++;
                if (!q.empty()) {
                    q.push({-1, -1});
                }
            } else {
                // rotten orange, contaminate its neighbors
                for (int i = 0; i < dirs.size(); i++) {
                    int x = row + dirs[i][0];
                    int y = col + dirs[i][1];
                    
                    if (x < 0 || x >= m || y < 0 || y >= n) {
                        continue;
                    }
                    
                    if (grid[x][y] == 1) {
                        // contaminate
                        grid[x][y] = 2;
                        fresh--;
                        // this orange will now contaminate others
                        q.push({x, y});
                    }
                }
            }
        }
        
        if (fresh == 0) {
            return result;
        }
        return -1;
    }
private:
    vector<vector<int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
};

int main() {
    vector<vector<int>> grid = {{2,1,1},{1,1,0},{0,1,1}};
    // // vector<vector<int>> grid = {{2,1,1},{1,1,0},{1,0,1}};
    // vector<vector<int>> grid = {{}};
    int min_elapsed = Solution().orangesRotting(grid);
    cout << "RV: " << min_elapsed << '\n';
}