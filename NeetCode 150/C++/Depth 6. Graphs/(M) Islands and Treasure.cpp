// Note: Islands & Treasures is the NeetCode website version of the
//       LeetCode Premium problem "Walls and Gates"
#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;

class Solution {
private:
    vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    const int INF = 2147483647;
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        queue<pair<int, int> > Q;
        int N = grid.size(), M = grid[0].size();
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (grid[i][j] == 0) {
                    Q.push({i, j});
                }
            }
        }
        int Qsize = 0, distance = 1;
        while (!Q.empty()) {
            Qsize = Q.size();
            for (int _ = 0; _ < Qsize; ++_) {
                pair<int, int> front = Q.front();
                Q.pop();
                int r = front.first, c = front.second;
                for (auto &dir : dirs) {
                    int i = r + dir.first, j = c + dir.second;
                    if (i < 0 || i >= N || j < 0 || j >= M) {
                        continue;
                    }
                    if (grid[i][j] == -1) {
                        continue;
                    }
                    if (distance < grid[i][j]) {
                        grid[i][j] = distance;
                        Q.push({i, j});
                    }
                }
            }
            ++distance;
        }
    }
};

int main() {
    vector<vector<int>> grid = {
        {2147483647,-1,0,2147483647},
        {2147483647,2147483647,2147483647,-1},
        {2147483647,-1,2147483647,-1},
        {0,-1,2147483647,2147483647}
    };
    Solution().islandsAndTreasure(grid);
    int N = grid.size(), M = grid[0].size();
    for (int i = 0; i < N; ++i) {
        cout << "[ ";
        for (int j = 0; j < M; ++j) {
            cout << grid[i][j] << (j != M-1 ? ", " : " ");
        }
        cout << "]\n";
    }
}