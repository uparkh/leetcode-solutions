#include <array>
#include <unordered_set>
#include <vector>
#include <iostream>
using namespace std;

// My Solution
// Doesn't work, 3 cases only
class Solution {
private:
    struct pair_hash {
        inline std::size_t operator()(const std::pair<int,int> &v) const {
            return v.first*31+v.second;
        }
    };
    pair<bool, bool> simulate_flow(vector<vector<int> > &heights,
                                    int _i, int _j) {
        const size_t N = heights.size(), M = heights[0].size();
        unordered_set<pair<int, int>, pair_hash> paths, visited;
        vector<pair<int, int>> to_remove, to_insert;
        bool pacific{false}, atlantic{false};
        paths.insert(make_pair(_i, _j));
        while (!paths.empty() && (!pacific || !atlantic)) {
            for (auto c : paths) {
                int curheight = heights[c.first][c.second];
                array<pair<int, int>, 4> directions = {
                    make_pair(c.first-1, c.second), 
                    make_pair(c.first+1, c.second),
                    make_pair(c.first, c.second-1), 
                    make_pair(c.first, c.second+1)
                };
                for (auto &dir : directions) {
                    if (visited.count(dir) != 0) {
                        continue;
                    }
                    bool skip = false;
                    if (dir.first < 0 || dir.second < 0) {
                        pacific = true; skip = true;
                    } else if (dir.first >= N || dir.second >= M) {
                        atlantic = true; skip = true;
                    }
                    if (skip) { continue; }
                    if (heights[dir.first][dir.second] <= curheight) {
                        to_insert.push_back(dir);
                    }
                }
                to_remove.push_back(c);
                visited.insert(c);
            }
            for (auto c : to_remove) {
                paths.erase(c);
            }
            to_remove.clear();
            for (auto dir : to_insert) {
                paths.insert(dir);
            }
            to_insert.clear();
        }
        return make_pair(pacific, atlantic);
    }
public:
    vector<vector<int> > pacificAtlantic(vector<vector<int> >& heights) {
        vector<vector<int> > rv;
        for (int i = 0; i < heights.size(); ++i) {
            for (int j = 0; j < heights.size(); ++j) {
                pair<bool, bool> res = simulate_flow(heights, i, j);
                bool pacific = res.first, atlantic = res.second;
                if (pacific && atlantic) {
                    rv.push_back({i, j});
                }
            }
        }
        return rv;
    }
};

// NeetCode Solution
/*
    Top & left pacific, bottom & right atlantic, determine spots that flow to both
    Instead go outside in, from oceans to spots where rain could flow from
    Faster bc avoids repeated work: cells along a path can also reach that ocean
    Time: O(m x n)
    Space: O(m x n)
*/

class NCSolution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        
        vector<vector<bool>> pacific(m, vector<bool>(n));
        vector<vector<bool>> atlantic(m, vector<bool>(n));
        
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0, m, n);
            dfs(heights, atlantic, i, n - 1, m, n);
        }
        
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j, m, n);
            dfs(heights, atlantic, m - 1, j, m, n);
        }
        
        vector<vector<int>> result;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }
        
        return result;
    }
private:
    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited,
        int i, int j, int m, int n) {
        
        visited[i][j] = true;
        
        if (i > 0 && !visited[i - 1][j] && heights[i - 1][j] >= heights[i][j]) {
            dfs(heights, visited, i - 1, j, m, n);
        }
        if (i < m - 1 && !visited[i + 1][j] && heights[i + 1][j] >= heights[i][j]) {
            dfs(heights, visited, i + 1, j, m, n);
        }
        if (j > 0 && !visited[i][j - 1] && heights[i][j - 1] >= heights[i][j]) {
            dfs(heights, visited, i, j - 1, m, n);
        }
        if (j < n - 1 && !visited[i][j + 1] && heights[i][j + 1] >= heights[i][j]) {
            dfs(heights, visited, i, j + 1, m, n);
        }
    }
};


int main() {
    vector<vector<int> > heights = {
        {1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}
    };
    auto rv = Solution().pacificAtlantic(heights);
    for (int i = 0; i < rv.size(); ++i) {
        int r = rv[i][0], c = rv[i][1];
        cout << "C" << i << ": (" << r << ", " << c << ")\n";
    }
}